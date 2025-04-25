from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Vertical, Horizontal
from textual.widget import Widget
from textual.color import Color
from app.theme import theme

class ChallengeItem(Widget):
    def __init__(self, challenge: dict, index: int):
        super().__init__()
        self.challenge = challenge
        self.index = index
        self.id = f"c{self.index}"

    def compose(self) -> ComposeResult:
        with Vertical(id="challenge-item"):
            yield Label(f"Unit {self.challenge['unit']}: {self.challenge['title']}", id="title")
            yield Label(self.challenge['description'], id="description")
            yield Label("Header:", id="header-label")
            yield Label(self.challenge['header'], id="header")
            #yield Label("Test Cases:", id="cases-label")
            #with Vertical(id="cases"):
            #    for case in self.challenge['cases']:
            #        with Horizontal(id="case"):
            #            yield Label(f"Input: {case['input']}", id="case-input")
            #            yield Label(f"Output: {case['output']}", id="case-output")

    def on_mount(self):
        self.query_one("#title").styles.color = theme["text"]
        self.query_one("#description").styles.color = theme["text"]
        self.query_one("#header-label").styles.color = theme["sec"]
        self.query_one("#header").styles.color = theme["sec"]
        #self.query_one("#cases-label").styles.color = theme["ter"]
        #for case_widget in self.query("#cases #case"):
        #    case_widget.styles.color = theme["text"]