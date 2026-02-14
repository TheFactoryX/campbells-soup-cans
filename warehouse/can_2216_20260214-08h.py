"""
Campbell's Soup Can #2216
Produced: 2026-02-14 08:50:02
Worker: OpenAI: GPT-5.2 Chat (openai/gpt-5.2-chat)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import shutil

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

quote = ("I don't mind that the universe is expanding—"
         "I just wish it wouldn't do it while I'm trying "
         "to figure out what I had for breakfast and "
         "whether it had meaning.")

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    width = shutil.get_terminal_size((80, 20)).columns
    box_width = min(len(quote) + 6, width - 4)
    horizontal_border = MAGENTA + "╔" + "═" * (box_width - 2) + "╗" + RESET

    print("\n" * 2)
    print(horizontal_border)

    wrapped_quote = []
    words = quote.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= box_width - 4:
            line += (" " if line else "") + word
        else:
            wrapped_quote.append(line)
            line = word
    if line:
        wrapped_quote.append(line)

    for line in wrapped_quote:
        padding = box_width - 4 - len(line)
        print(MAGENTA + "║ " + RESET + CYAN + BOLD, end="")
        typewriter(line + " " * padding, 0.02)
        print(MAGENTA + "║" + RESET)

    print(MAGENTA + "╚" + "═" * (box_width - 2) + "╝" + RESET)
    print("\n" + YELLOW + ITALIC + "— a deeply concerned neurotic" + RESET)
    print("\n")

if __name__ == "__main__":
    main()