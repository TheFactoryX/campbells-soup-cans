"""
Campbell's Soup Can #2203
Produced: 2026-02-13 17:06:51
Worker: OpenAI: GPT-3.5 Turbo 16k (openai/gpt-3.5-turbo-16k)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# Function to print text in a stylized box
def print_in_box(text):
    print('\033[1;33;40m')
    print('*' * (len(text) + 8))
    print('*   ' + text + '   *')
    print('*' * (len(text) + 8))

# Woody Allen style philosophical quote
quote = "I'm not afraid of death; I just don't want to be there when it happens."

# Print quote in a visually interesting way
print('\033[1;36;40m')
print('''
  .  _________
 ()<| Woody   |
  || Allen   |
  ''')
time.sleep(0.5)
print_in_box(quote)