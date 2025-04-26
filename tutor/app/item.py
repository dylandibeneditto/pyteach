from textual.app import ComposeResult
from textual.widgets import Label
from textual.containers import Vertical, Horizontal
from textual.widget import Widget
from textual.color import Color
from app.theme import theme
from loader import is_completed
import random

class ChallengeItem(Widget):
    def __init__(self, challenge: dict, index: int):
        super().__init__()
        self.challenge = challenge
        self.index = index
        self.id = f"{self.challenge['id']}_{self.index}_{random.randint(0, 1000)}"

    def compose(self) -> ComposeResult:
        with Vertical(id="challenge-item"):
            with Horizontal(id="challenge-header"):
                yield Label("✅ " if is_completed(self.challenge["id"]) else "❌ ", id="status")
                yield Label(self.challenge["title"], id="title")
                yield Label(f" - Unit {self.challenge['unit']}", id="unit")
            yield Label(self.challenge["description"], id="description")

    def on_mount(self):
        self.query_one("#title").styles.color = theme["text"]
        self.query_one("#description").styles.color = theme["ter"]
        self.query_one("#unit").styles.color = theme["sec"]