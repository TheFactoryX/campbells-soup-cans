"""
Campbell's Soup Can #326
Produced: 2025-11-16 23:28:41
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36;1m"
YELLOW = "\033[33;1m"
MAGENTA = "\033[35;1m"

# Typing effect
def type_line(text, delay=0.005):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        if ch != '\n':
            time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def build_box():
    width = 63
    border_top = f"{CYAN}┌{'─'*width}┐{RESET}"
    border_bottom = f"{CYAN}└{'─'*width}┘{RESET}"
    # Quote lines
    lines_content = [
        "I don't think I have a soul.",
        "Only evidence is that each time I try to be rational,",
        "I end up being a neurotic, existential narcissist,",
        "who hates himself as much as he loves the universe."
    ]
    box_lines = [border_top]
    # Empty line inside
    box_lines.append(f"{CYAN}│{RESET} {MAGENTA}{'':width-2}{RESET}{CYAN}│{RESET}")
    for text in lines_content:
        padded = f"{YELLOW}{text:<{width-2}}{RESET}"
        box_lines.append(f"{CYAN}│{RESET} {padded}{CYAN}│{RESET}")
    # Empty line inside
    box_lines.append(f"{CYAN}│{RESET} {MAGENTA}{'':width-2}{RESET}{CYAN}│{RESET}")
    box_lines.append(border_bottom)
    return box_lines

def animate_loading():
    spinner = ['|', '/', '-', '\\']
    for _ in range(12):
        for ch in spinner:
            sys.stdout.write(f'\r{MAGENTA}Thinking{ch}{RESET}')
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 20 + '\r')

def main():
    box = build_box()
    for line in box:
        type_line(line, delay=0.005)
    # Slight pause before animation
    time.sleep(0.3)
    animate_loading()

if __name__ == "__main__":
    main()