from agents import *
from rich.console import Console
from rich.markdown import Markdown
import argparse

console = Console(width=150)

parser = argparse.ArgumentParser()
parser.add_argument("--agent", default="helpful_assistant")
args = parser.parse_args()

try:
    agent = globals()[args.agent]
except KeyError:
    console.print(f"Unknown agent '{args.agent}'. Using default 'helpful_assistant'.")
    agent = helpful_assistant

while True:
    user_input = input("> ")
    if len(user_input) == 0:
        continue
    response = agent.message(user_input)
    console.print(Markdown(f"< {response}"))
