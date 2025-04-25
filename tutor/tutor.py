import os
from app.main import MainView
from loader import load_challenges

def main():
    MainView(load_challenges()).run()

if __name__ == "__main__":
    main()