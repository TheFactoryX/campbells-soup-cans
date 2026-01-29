"""
Campbell's Soup Can #1931
Produced: 2026-01-29 20:47:52
Worker: OpenAI: GPT-3.5 Turbo (openai/gpt-3.5-turbo)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def display_quote():
    print("\033[1;33;40m")
    print("#"*50)
    print("#"*5 + " " * 40 + "#"*5)
    print("#"*5 + "  I'm not afraid of death;             " + "#"*5)
    print("#"*5 + "  I just don't want to be there        " + "#"*5)
    print("#"*5 + "  when it happens.                     " + "#"*5)
    print("#"*5 + "                                      " + "#"*5)
    print("#"*5 + "                - Woody Allen           " + "#"*5)
    print("#"*5 + "                                      " + "#"*5)
    print("#"*5 + " " * 40 + "#"*5)
    print("#"*50)
    print("\033[0;0;0m")

def animate_quote():
    width = 50
    message = "Enjoy the neurotic wisdom..."

    for i in range(width - len(message) + 1):
        print("#"*50)
        print("#"*5 + " " + " " * i + message + " "*(width-len(message)-i) + " " + "#"*5)
        print("#"*50)
        time.sleep(0.1)

if __name__ == "__main__":
    display_quote()
    animate_quote()