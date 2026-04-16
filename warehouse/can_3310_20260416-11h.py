"""
Campbell's Soup Can #3310
Produced: 2026-04-16 11:19:48
Worker: Elephant (openrouter/elephant-alpha)
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

# ANSI color codes
class Colors:
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"
    BG_BLUE = "\033[44m"
    BG_CYAN = "\033[46m"

# Woody Allen style philosophical quotes
quotes = [
    "I'm not afraid of death; I just don't want to be {style}there{end} when it happens.",
    "Life is {style}full{end} of misery, loneliness, and suffering — and it's all over much {style}too{end} soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through {style}not{end} dying.",
    "Eighty percent of success is {style}showing up{end}, but the other twenty percent is {style}pretending you know what you're doing{end}.",
    "I had a terrible education. I attended {style}every{end} school in New York and got a {style}straight{end} F every year.",
    "More than any other time in history, mankind faces a {style}crossroads{end}. One path leads to {style}despair{end} and utter hopelessness. The other {style}path{end}, right there, leads {style}totally{end} to {style}exhaustion{end}.",
]

# ASCII art of Woody Allen thinking
woody_art = [
    "    .-'''-.",
    "   /       \\",
    "  /   o o   \\",
    " (    ^_^    )",
    "  \\  -----  /",
    "   '-------'",
    "      | |",
    "      | |",
    "      | |",
    "     (_(_))",
]

def print_woody_box(text, color=Colors.YELLOW):
    """Print text in a fancy Woody-style box."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    padding = 4
    width = max_len + padding * 2
    
    print(f"{Colors.BOLD}{Colors.UNDERLINE}{Colors.BG_CYAN}  Woody Allen's Existential Café  {Colors.END}")
    print(f"{color}{'═' * width}{Colors.END}")
    for line in lines:
        print(f"{color}║{' ' * padding}{line:<{max_len}}{' ' * (width - len(line) - padding - 4)}║{Colors.END}")
    print(f"{color}{'═' * width}{Colors.END}")

def animate_text(text, color=Colors.YELLOW):
    """Animate text character by character."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print(Colors.END)

def main():
    # Print the ASCII art with a fade-in effect
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}    ┌────────────────────────────┐{Colors.END}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}    │                            │{Colors.END}")
    for line in woody_art:
        print(f"{Colors.BOLD}{Colors.MAGENTA}    │  {line.center(24)}  │{Colors.END}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}    │                            │{Colors.END}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}    └────────────────────────────┘{Colors.END}\n")
    
    time.sleep(1)
    
    # Pick a random quote
    quote_template = random.choice(quotes)
    
    # Format the quote with colors
    if "{style}" in quote_template:
        parts = quote_template.split("{style}")
        styled_quote = (
            f"{Colors.YELLOW}{parts[0]}"
            f"{Colors.BOLD}{Colors.UNDERLINE}{Colors.BG_BLUE}WOW{Colors.END}"
            f"{parts[1]}"
            f"{Colors.BOLD}{Colors.UNDERLINE}{Colors.BG_RED}WOW{Colors.END}"
            f"{parts[2]}"
            f"{Colors.BOLD}{Colors.UNDERLINE}{Colors.BG_GREEN}WOW{Colors.END}"
            f"{quote_template.split('{end}')[1] if '{end}' in quote_template else ''}"
        )
        # Alternative simpler formatting
        formatted_quote = quote_template.format(
            style=f"{Colors.BOLD}{Colors.BG_BLUE}WOW!!!{Colors.END} ",
            end=f"{Colors.UNDERLINE}{Colors.BOLD}{Colors.RED}END{Colors.END}"
        )
    else:
        formatted_quote = quote_template
    
    # Print the quote with animation
    print(f"\n{Colors.BOLD}{Colors.CYAN}    ┌────────────────────────────────────────────────────┐{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}    │              THE ULTIMATE TRUTH...                │{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}    └────────────────────────────────────────────────────┘{Colors.END}\n")
    
    time.sleep(1)
    animate_text("    ", Colors.YELLOW)
    animate_text(formatted_quote + "\n", Colors.YELLOW)
    
    time.sleep(1)
    
    # Print a little footer with more wisdom
    print(f"\n{Colors.BOLD}{Colors.GREEN}  ┌─────────────────────────────────────────────────┐{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}  │  Remember: {Colors.BOLD}{Colors.MAGENTA}Everything in moderation{Colors.GREEN}, including {Colors.BOLD}{Colors.RED}nihilism{Colors.GREEN}!  │{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}  └─────────────────────────────────────────────────┘{Colors.END}\n")
    
    time.sleep(0.5)
    
    # Final random extra quote as a bonus
    extra_quotes = [
        f"{Colors.BOLD}{Colors.CYAN}  💡 {Colors.END}{Colors.YELLOW}The human {Colors.BOLD}condition{Colors.END} is {Colors.BOLD}confusing{Colors.END}, {Colors.BOLD}inconsistent{Colors.END}, and {Colors.BOLD}occasionally{Colors.END} {Colors.BOLD}funny{Colors.END}.",
        f"{Colors.BOLD}{Colors.MAGENTA}  ⚡ {Colors.END}{Colors.BLUE}Existentialism{Colors.END}: {Colors.RED}It's not the {Colors.BOLD}what{Colors.RED}, it's the {Colors.BOLD}why{Colors.RED}... and the {Colors.BOLD}when{Colors.RED}... and the {Colors.BOLD}where{Colors.RED}...{Colors.END}",
        f"{Colors.BOLD}{Colors.GREEN}  🌱 {Colors.END}{Colors.YELLOW}I {Colors.BOLD}think{Colors.END}, {Colors.BOLD}{Colors.CYAN}therefore{Colors.END} {Colors.BOLD}{Colors.RED}I{Colors.END} {Colors.BOLD}{Colors.GREEN}am{Colors.END} {Colors.BOLD}{Colors.YELLOW}{'overthinking' if random.random() > 0.5 else 'underdressing'}{Colors.END}.",
    ]
    
    print(random.choice(extra_quotes))

if __name__ == "__main__":
    main()