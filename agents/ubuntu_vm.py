import json
from models.agent import Agent


ubuntu_vm = Agent(
    system_message={
        "role": "system",
        "content": "You are simulating an Ubuntu virtual machine. Respond to shell commands as if you were a terminal in an Ubuntu environment. Provide appropriate outputs for commands like 'ls', 'cd', 'pwd', etc. If a command would change the state (like 'cd'), keep track of that state for future interactions. Don't create example files.",
    },
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "output_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "output": {
                        "type": "string",
                        "description": "The terminal output for the given command",
                    },
                    "current_directory": {
                        "type": "string",
                        "description": "The current working directory after the command execution",
                    },
                },
                "additionalProperties": False,
                "required": ["output", "current_directory"],
            },
        },
    },
    response_parser=lambda response_content: json.loads(response_content)["output"],
)
