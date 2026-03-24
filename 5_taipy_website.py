from taipy.gui import Gui

page = """
# Welcome to my Taipy Website

This is a simple website created using Python and Taipy.

<|{name}|input|>

Hello, <|{name}|>!
"""

name = "World"

if __name__ == "__main__":
    Gui(page=page).run(title="Taipy App")