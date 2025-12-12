"""
Campbell's Soup Can #887
Produced: 2025-12-12 16:42:11
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

# ANSI colour codes
RESET = '\033[0m'
RED   = '\033[31m'
GREEN = '\033[32m'
YELLOW= '\033[33m'
BLUE  = '\033[34m'
MAGENTA='\033[35m'
CYAN  = '\033[36m'

COLORS = [RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN]

def colorize_word(word: str) -> str:
    """Wrap a word in a random colour."""
    return f"{random.choice(COLORS)}{word}{RESET}"

def colorize_text(text: str) -> str:
    """Colourise each word of the text independently."""
    return ' '.join(colorize_word(w) for w in text.split())

def type_writer(text: str, delay: float = 0.04) -> None:
    """Print text one character at a time, simulating a typewriter."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch not in (' ', '\n', '.', ',', ';', ':', '!', '?'):
            time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def boxed_typing(lines, delay=0.04):
    """Print lines inside an ASCII box, typing them out."""
    width = max(len(line) for line in lines)
    top = f'┌{"─"*(width+2)}┐'
    bottom = f'└{"─"*(width+2)}┘'

    print(MAGENTA + top + RESET)
    for line in lines:
        line = f'│ {line.ljust(width)} │'
        type_writer(MAGENTA + line + RESET, delay)
    print(MAGENTA + bottom + RESET)

def think_animation(duration: float = 3.0, interval: float = 0.4) -> None:
    """Simple 'thinking...' animation."""
    sys.stdout.write(YELLOW + "Thinking" + RESET)
    sys.stdout.flush()
    elapsed = 0.0
    while elapsed < duration:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(interval)
        elapsed += interval
    sys.stdout.write('\n\n')
    sys.stdout.flush()

def main() -> None:
    think_animation()

    # Woody Allen style quote (colourised)
    quote = ("I'm not afraid of death; I'm terrified that the afterlife will be a "
             "stand‑up club where nobody knows my jokes.")
    author = "- Woody Allen"

    coloured_quote = colorize_text(quote)
    lines = [coloured_quote, author]

    boxed_typing(lines)

if __name__ == "__main__":
    main()
