"""
Campbell's Soup Can #3306
Produced: 2026-04-16 03:47:11
Worker: Qwen: Qwen3 VL 8B Thinking (qwen/qwen3-vl-8b-thinking)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def main():
    # Woody Allen-style quote: neurotic, funny, self-deprecating, existential
    quote = "I'm not sure if I'm alive. I think I'm dead. But if I'm dead, why am I writing this? So I must be alive. But if I'm alive, why am I afraid of living? Because I'm afraid of living. And that's why I'm writing this. And I'm not even sure if I'm writing this. I think I'm hallucinating!"
    
    # Split into lines and find max width for box
    lines = quote.splitlines()
    max_len = max(len(line) for line in lines)
    box_width = max_len + 4
    border = "\033[44m\033[97m"  # Blue background, white text
    
    # Print box with animation
    print(border + "+" * box_width + "\033[0m")
    time.sleep(0.1)
    
    for line in lines:
        padded = line.ljust(box_width - 2)
        print(border + "|" + padded + "|" + "\033[0m")
        time.sleep(0.1)
    
    print(border + "+" * box_width + "\033[0m")
    time.sleep(0.3)
    
    # Animated ghost reveal!
    ghost_art = [
        "  .-\"\"-.  ",
        " /      \\",
        " /        \\",
        "(  o    o  )",
        " \\        /",
        "  \\      /",
        "   '-..-'"
    ]
    
    for i, line in enumerate(ghost_art):
        if i == 3:  # Ghost's eyes pulse! (using ANSI colors for effect)
            print("\033[44m\033[33m" + line + "\033[0m")
            time.sleep(0.2)
        else:
            print("\033[44m\033[97m" + line + "\033[0m")
            time.sleep(0.1)

if __name__ == "__main__":
    main()