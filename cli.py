from agents.helpful_assistant import helpful_assistant


while True:
  user_input = input('> ')
  print(f'< {helpful_assistant.message(user_input)}')
