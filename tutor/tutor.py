import os

def main():
    print("Welcome to Code Tutor\n")
    challenges = os.listdir("challenges")
    challenges = [c for c in challenges if os.path.isdir(os.path.join("challenges", c))]

    for i, name in enumerate(challenges):
        print(f"{i + 1}. {name.replace('_', ' ').title()}")

    choice = input("\nSelect a challenge number: ")
    try:
        index = int(choice) - 1
        if 0 <= index < len(challenges):
            os.system(f"python runner.py {challenges[index]}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a number.")

if __name__ == "__main__":
    main()