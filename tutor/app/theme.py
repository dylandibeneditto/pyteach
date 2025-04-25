from textual.color import Color

themes = {
    "dark": {
        "bg": Color(16, 16, 16),
        "text": Color(241, 241, 241),
        "sec": Color(113, 113, 113),
        "ter": Color(85, 85, 85),
        "selected_bg": Color(21, 21, 21),
    },
    "light": {
        "bg": Color(245,245,245),
        "text": Color(16,16,16),
        "sec": Color(142,142,142),
        "ter": Color(170,170,170),
        "selected_bg": Color(235, 235, 235),
    }
}

theme = themes["dark"]