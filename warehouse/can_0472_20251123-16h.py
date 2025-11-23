"""
Campbell's Soup Can #472
Produced: 2025-11-23 16:36:27
Worker: AI21: Jamba Mini 1.7 (ai21/jamba-mini-1.7)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Single-file Python program that prints a single visual Woody Allen-style quote

# ANSI escape codes for colors
WHITE_ON_RED = "\033[37;41m"
DEFAULT_COLOR = "\033[0m"

def print_quote_with_style():
    quote = (
        f"{WHITE_ON_RED}"
        f" ──────────────────\n"
        f"   (╯ಠل͟ʖಠ)╯        \n"
        f"      ...         \n"
        f"   ...            \n"
        f"   ═╗╔╗╔╗╣║║♪♪♪♪        ┌┐┌┐┌┐\n"
        f"""     ...
   ~ Futility of life! 
           ~ Sentience is a trick! 
               ~ Why do I exist? ~
"""
        f"{DEFAULT_COLOR}\n"
        f"So I put my pants on, and then I became a philosopher. \n"
        f"It made me feel better. \n"
        f"But also frustrated. Life is short, why worry about pants-wearing?\n"
    )
    print(quote)

if __name__ == "__main__":
    print_quote_with_style()