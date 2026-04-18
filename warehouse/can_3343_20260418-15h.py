"""
Campbell's Soup Can #3343
Produced: 2026-04-18 15:54:32
Worker: Elephant (openrouter/elephant-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys

def print_woody_quote():
    # ANSI color codes
    cyan = "\033[36m"
    yellow = "\033[33m"
    magenta = "\033[35m"
    bold = "\033[1m"
    reset = "\033[0m"
    dim = "\033[2m"
    
    # Woody Allen style quote
    quote = (
        "I’m not terrified of death—"
        "I just resent having to cancel my plans "
        f"{dim}at the last second{dim}... "
        f"{magenta}Eternity{reset} is such a {bold}inconvenient{reset} commitment."
    )
    
    # ASCII "thought bubble" around the quote
    lines = quote.split(' ')
    max_width = 78
    wrapped = []
    current_line = ""
    for word in lines:
        if len(current_line) + len(word) + 1 <= max_width:
            current_line += (" " if current_line else "") + word
        else:
            wrapped.append(current_line)
            current_line = word
    if current_line:
        wrapped.append(current_line)
    
    bubble_top = " " + "╭" + "─" * (max_width + 2) + "╮"
    bubble_mid_prefix = "  │ "
    bubble_mid_suffix = " │"
    bubble_bot_prefix = "  ╰ "
    bubble_bot_suffix = "  ╯"
    
    # Print with animation
    for i, line in enumerate(wrapped):
        if i == 0:
            print(bubble_top)
        print(bubble_mid_prefix + line.ljust(max_width) + bubble_mid_suffix)
    
    # Bottom of bubble
    padding = " " * (max_width - len(wrapped[-1]))
    print(bubble_mid_prefix + wrapped[-1] + padding + " │")
    print(bubble_bot_prefix + "─" * (max_width - 2) + bubble_bot_suffix)
    
    # Woody's little disclaimer
    print()
    print(f"{yellow}*{reset} This existential crisis brought to you by late-night {cyan}coffee{reset} "
          f"and {magenta}dodging responsibilities{reset}.")
    print(f"{dim}  (Cue the saxophone solo...){reset}")

if __name__ == "__main__":
    # Subtle fade-in effect
    quote_parts = [
        "I’m not terrified of death—",
        "I just resent having to cancel my plans ",
        "at the last second... ",
        "Eternity is such a inconvenient commitment."
    ]
    
    for part in quote_parts:
        sys.stdout.write(part)
        sys.stdout.flush()
        time.sleep(0.07)
    
    print("\n")
    print_woody_quote()
    
    # Final deep thought
    time.sleep(1)
    print("\n" + f"{bold}{cyan}After all, {yellow}if{reset} it doesn’t scare you, "
          f"{magenta}maybe it’s not{reset} {bold}your{reset} {yellow}death.{reset}")

if __name__ == "__main__":
    print_woody_quote()