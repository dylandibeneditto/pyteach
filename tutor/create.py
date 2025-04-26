import os
import shutil
import time

def create_challenge(challenge):
    history_folder = "history"
    os.makedirs(history_folder, exist_ok=True)

    if os.path.exists("challenge.py"):
        base_filename = os.path.join(history_folder, f"backup_{time.strftime('%H-%M-%S|%Y-%m-%d')}")
        filename = base_filename + ".py"
        counter = 1
        while os.path.exists(filename):
            filename = f"{base_filename}_{counter}.py"
            counter += 1

        shutil.move("challenge.py", filename)

    with open("challenge.py", "w") as f:
        f.write(challenge["header"])
    
    with open("run.py", "w") as f:
        f.write(
            """
from challenge import """ + challenge["function"] + """
from tutor.loader import add_completion

from rich.console import Console
from rich.panel import Panel
import traceback

c = Console(highlight=False)

def run_tests():
    test_cases = [
    """+"    "+
        "\n        ".join([f"({repr(case["input"])}, {repr(case["output"])})," for case in challenge["cases"]])
    +"""
    ]
    c.clear()

    for i, (input_str, expected_output) in enumerate(test_cases):
        exc = False
        try:
            result = """+challenge["function"]+"""(*input_str)
        except Exception as e:
            result = e
            exc = True

        if result != expected_output:
            c.print(f"[bold red]Test case {i+1} failed: ({i+1}/{len(test_cases)})[/]")
            if exc:
                c.print(Panel(f"{''.join(traceback.format_exception(result))}", title="Runtime Error", style="red"))
            c.print(f"[bright_black]\\nCase:[/]")

            repr_input = [repr(x) for x in input_str]
            c.print(f"[code on black]"""+challenge["function"]+"""({', '.join(repr_input)})[/]")
            c.print(f"[white on dark_green]{repr(expected_output)}[/white on dark_green]")
            if not exc:
                c.print(f"\\n[bright_black]Your result:[/bright_black]\\n[white on dark_red]{repr(result)}[/]\\n")
            return False
    
    c.print(f"[bold green]All test cases passed! ({len(test_cases)}/{len(test_cases)})[/]")
    add_completion("""+repr(challenge["id"])+""")


if __name__ == "__main__":
    run_tests()
            """
        )