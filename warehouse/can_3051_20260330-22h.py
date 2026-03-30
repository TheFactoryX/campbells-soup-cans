"""
Campbell's Soup Can #3051
Produced: 2026-03-30 22:56:08
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# woody_allen_quote.py
import time

# ANSI escape codes for colors and styles
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
END = "\033[0m"

def print_woody_quote():
    quote = [
        f"{BOLD}{YELLOW}Woody Allen once said:{END}",
        "",
        f"{BLUE}I don't want to achieve immortality through my work;",
        f"I want to achieve it through not dying.{END}",
        "",
        f"{GREEN}Also, I'm not afraid of death;",
        f"I just don't want to be there when it happens.{END}",
        "",
        f"{RED}Life is full of misery, loneliness, and suffering -",
        f"and it's all over much too soon.{END}",
        "",
        f"{MAGENTA}I took a speed-reading course and read War and Peace in twenty minutes.",
        f"It involves Russia.{END}",
        "",
        f"{CYAN}I believe there is something out there watching us.",
        f"Unfortunately, it's the government.{END}",
        "",
        f"{UNDERLINE}{BOLD}My one regret in life is that I am not someone else.{END}"
    ]

    # Print each line with a slight delay for dramatic effect
    for line in quote:
        print(line)
        time.sleep(0.5)

    # Add a funny footer
    print("\n" + "="*50)
    print(f"{BOLD}{RED}Brought to you by: Existential Dread Inc.{END}")
    print("="*50)

if __name__ == "__main__":
    print_woody_quote()