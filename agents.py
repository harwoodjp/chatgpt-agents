from dataclasses import dataclass, field
from openai import OpenAI
import json


class Agent:
  def __init__(
    self,
    system_message,
    response_format,
    response_parser,
    client = OpenAI(),
    model="gpt-4o-2024-08-06",
    messages = []
  ):
    self.system_message = system_message
    self.response_format = response_format
    self.response_parser = response_parser
    self.client = client
    self.model = model
    self.messages = [system_message]
  def message(self, content):
    self.messages.append({"role": "user", "content": content})
    response = self.client.chat.completions.create(
        model=self.model,
        messages=self.messages,
        response_format=self.response_format
    )
    response_content = response.choices[0].message.content
    self.messages.append({"role": "assistant", "content": response_content})
    return self.response_parser(response_content)
  @staticmethod
  def clone(agent):
    return Agent(
      agent.system_message,
      agent.response_format,
      agent.response_parser
    )



helpful_assistant = Agent(
  system_message = {
    "role": "system",
    "content": "You are a helpful assistant. You respond to any inquiry with empathy and intellect."
  },
  response_format = None,
  response_parser = lambda response_content: response_content
)

sentiment_analyst = Agent(
  system_message = {
    "role": "system",
    "content": "You are a sentiment analyst. You take text input and analyze the mood of the language. Your output is single words in an array."
  },
  response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "mood_schema",
        "schema": {
            "type": "object",
            "properties": {
                "mood": {
                    "description": "The detected mood in text input",
                    "type": "array",
                    "items": {
                        "$ref": "#"
                    }                    
                },
                "additionalProperties": False
            }
        }
      }
    },
    response_parser = lambda response_content: json.loads(response_content).get("mood", "")
)
