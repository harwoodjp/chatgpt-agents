from models.agent import Agent


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
