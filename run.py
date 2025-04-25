from challenge import reverse

from rich.console import Console
from rich.panel import Panel
import traceback

c = Console(highlight=False)


def run_tests():
    test_cases = [
        (["hello"], "olleh"),
        (["world"], "dlrow"),
        ([""], ""),
        (["12345"], "54321"),
        (["a"], "a"),
        (["ab"], "ba"),
        (["abc"], "cba"),
    ]
    
    c.clear()

    for i, (input_str, expected_output) in enumerate(test_cases):
        exc = False
        try:
            result = reverse(*input_str)
        except Exception as e:
            result = e
            exc = True

        if result != expected_output:
            c.print(f"[bold red]Test case {i+1} failed: ({i+1}/{len(test_cases)})[/]")
            if exc:
                c.print(Panel(f"{''.join(traceback.format_exception(result))}", title="Runtime Error", style="red"))
            c.print(f"[bright_black]\nCase:[/]")

            repr_input = [repr(x) for x in input_str]
            c.print(f"[code on black]reverse({', '.join(repr_input)})[/]")
            c.print(f"[white on dark_green]{repr(expected_output)}[/white on dark_green]")
            if not exc:
                c.print(f"\n[bright_black]Your result:[/bright_black]\n[white on dark_red]{repr(result)}[/]\n")
            return False
    
    c.print(f"[bold green]All test cases passed! ({len(test_cases)}/{len(test_cases)})[/]")
            
            

if __name__ == "__main__":
    run_tests()