"""
Campbell's Soup Can #2291
Produced: 2026-02-18 07:16:49
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import textwrap

def main():
    YELLOW = '\033[33m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    GRAY = '\033[90m'

    quote = ("I'm not afraid of death; I'm afraid of arriving late to my own funeral. "
             "Then I'd miss the eulogy where everyone lies nicely about me. And let's be honest, "
             "I'd want to hear what they say about my hat collection.")
    
    wrapped_quote = textwrap.wrap(quote, width=55)
    max_width = max(len(line) for line in wrapped_quote) if wrapped_quote else 0
    
    head_lines = [
        GRAY + "   (o)(o)  " + RESET,
        GRAY + "     ||    " + RESET,
        GRAY + "    ====   " + RESET,
        GRAY + "   |    |  " + RESET,
        GRAY + "    \\__/   " + RESET,
        GRAY + "      \\    " + RESET,
        GRAY + "       \\   " + RESET,
        GRAY + "        \\  " + RESET
    ]

    for line in head_lines:
        print(line)
    
    print(YELLOW + "         .-" + "-" * (max_width + 2) + "-." + RESET)
    
    for line in wrapped_quote:
        centered = line.center(max_width)
        sys.stdout.write(YELLOW + "        / " + RESET)
        sys.stdout.flush()
        for char in centered:
            sys.stdout.write(WHITE + char + RESET)
            sys.stdout.flush()
            time.sleep(0.03)
        sys.stdout.write(YELLOW + " \\" + RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.1)
    
    print(YELLOW + "         '-" + "-" * (max_width + 2) + "-'" + RESET)
    
    print("\n" + YELLOW + "  ~ Woody's Wisdom: Existential dread with a punchline ~" + RESET)

if __name__ == "__main__":
    main()