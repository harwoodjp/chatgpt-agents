from agents.helpful_assistant import helpful_assistant
from rich.console import Console
from rich.markdown import Markdown

console = Console(width=150)

while True:
    user_input = input("> ")
    if len(user_input) == 0:
        continue
    response = helpful_assistant.message(user_input)
    console.print(Markdown(f"< {response}"))
