"""
Campbell's Soup Can #3071
Produced: 2026-04-01 09:35:50
Worker: OpenAI: GPT-3.5 Turbo (openai/gpt-3.5-turbo)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def print_color_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
    }
    end_color = "\033[0m"
    print(colors[color] + text + end_color)

quote = """
         __      __  _________   ___        ________    ____  _______ .______      
        /  \    /  \/   _____/  /   \      /  _____/   /   /  \      \|   _  \     
        \   \/\/   /\_____  \  /  ^  \    /   \  ___   /    |  /   |   \  |_)  |    
         \        / /        \/   /_\  \   \    \_\  \ /     | /    |    \   _  <     
          \__/\  / /_______  \  /_____    \  \______    \____  |____|_  /_|_  \_\   
               \/          \/       \__\          \_/          \/   \/    

"I don't want to achieve immortality through my work; 
 I want to achieve it through not dying." - Woody Allen
"""

print_color_text(quote, "blue")
time.sleep(2)

print("\nIn the end, nothing really matters...¯\\_(ツ)_/¯")