from models.agent import Agent


helpful_assistant = Agent(
  system_message = {
    "role": "system",
    "content": "You are a helpful assistant. You respond to any inquiry with empathy and intellect."
  },
  response_format = None,
  response_parser = lambda response_content: response_content
)
