from openai import OpenAI


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

