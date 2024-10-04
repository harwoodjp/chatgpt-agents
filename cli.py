from agents import helpful_assistant

while True:
  agent = helpful_assistant 
  user_input = input('> ')
  print(f'< {agent.message(user_input)}')
