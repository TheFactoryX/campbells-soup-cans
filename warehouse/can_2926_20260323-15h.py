"""
Campbell's Soup Can #2926
Produced: 2026-03-23 15:15:29
Worker: OpenAI: GPT-3.5 Turbo 16k (openai/gpt-3.5-turbo-16k)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def print_colorful_quote(quote):
    colors = ['\033[95m', '\033[94m', '\033[92m', '\033[93m', '\033[91m']
    end_color = '\033[0m'
    
    print('\n' + '*' * 50)
    
    for i, line in enumerate(quote.split('\n')):
        color = colors[i % len(colors)]
        formatted_line = f'{color}{line}{end_color}'
        print(' ' * 10 + formatted_line.center(30))
        
    print('\n' + '*' * 50)
    

quote = """
I'm not afraid of death; 
I just don't want to be there when it happens.
"""

print_colorful_quote(quote)

time.sleep(2)

quote = """
Life is full of misery, loneliness, and suffering - 
and it's all over much too soon.
"""

print_colorful_quote(quote)

time.sleep(2)

quote = """
I don't want to achieve immortality through my work; 
I want to achieve it through not dying.
"""

print_colorful_quote(quote)