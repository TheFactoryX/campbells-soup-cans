"""
Campbell's Soup Can #5091
Produced: 2026-10-10 22:32:55
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic digital existential crisis, one quote at a time.
Run this and question everything (especially your career choices).
"""

import sys
import time
import shutil

# Get terminal width for centering
TERMINAL_WIDTH = shutil.get_terminal_size().columns

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    
    # Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright variants
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    
    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"


def print_boxed(text, color=Colors.BRIGHT_YELLOW, width=60, padding=1):
    """Print text in a colorful boxed frame."""
    border_top = "┌" + "─" * (width - 2) + "┐"
    border_bottom = "└" + "─" * (width - 2) + "┘"
    side = "│" + " " * (width - 2) + "│"
    
    print(f"\n{color}{Colors.BOLD}{border_top}{Colors.RESET}")
    
    for _ in range(padding):
        print(f"{color}{Colors.BOLD}{side}{Colors.RESET}")
    
    # Print the text, wrapped to fit
    lines = []
    words = text.split()
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    # Pad lines to center
    inner_width = width - 4
    for line in lines:
        padding_left = (inner_width - len(line)) // 2
        padding_right = inner_width - len(line) - padding_left
        print(f"{color}{Colors.BOLD}│ {' ' * padding_left}{line}{' ' * padding_right} │{Colors.RESET}")
    
    for _ in range(padding):
        print(f"{color}{Colors.BOLD}{side}{Colors.RESET}")
    
    print(f"{color}{Colors.BOLD}{border_bottom}{Colors.RESET}")


def typewriter_effect(text, delay=0.04):
    """Print text one character at a time with typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def animated_quote(quote, author="— Woody Allen (probably)"):
    """Display the quote with a dramatic animated reveal."""
    
    # Clear screen a bit
    print("\n" * 3)
    
    # Cycling color for "thinking" dots
    thinking_colors = [
        Colors.BRIGHT_RED, Colors.BRIGHT_MAGENTA, 
        Colors.BRIGHT_CYAN, Colors.BRIGHT_YELLOW
    ]
    
    # Phase 1: Existential contemplation
    print(f"{Colors.DIM}{'🌌'.center(TERMINAL_WIDTH // 2)}{Colors.RESET}")
    time.sleep(0.8)
    
    # Phase 2: Neurotic build-up
    buildup_lines = [
        f"{Colors.BRIGHT_RED}{Colors.DIM}...{Colors.RESET}",
        f"{Colors.BRIGHT_MAGENTA}*adjusts glasses*{Colors.RESET}",
        f"{Colors.BRIGHT_CYAN}Umm...{Colors.RESET}",
        f"{Colors.BRIGHT_YELLOW}Well,{Colors.RESET}",
        f"{Colors.BRIGHT_RED}it's like this:{Colors.RESET}"
    ]
    
    for i, line in enumerate(buildup_lines):
        print(f"{line:^{TERMINAL_WIDTH}}")
        time.sleep(0.4 + (i * 0.1))
    
    time.sleep(0.6)
    
    # Phase 3: The actual quote reveal with typewriter effect
    print("\n")
    
    # Color cycling for the quote
    quote_colors = [
        Colors.BRIGHT_YELLOW, Colors.BRIGHT_CYAN, 
        Colors.BRIGHT_MAGENTA, Colors.BRIGHT_GREEN
    ]
    
    # Print quote character by character with color shifts
    color_index = 0
    for char in quote:
        if char not in (" ", "\n", "—"):
            color = quote_colors[color_index % len(quote_colors)]
            sys.stdout.write(f"{color}{Colors.BOLD}{char}{Colors.RESET}")
            color_index += 1
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    
    # Author attribution with shrinking effect
    print("\n")
    time.sleep(0.5)
    
    # Create a wavy underline effect
    for wave in range(3):
        underline = "~" * len(quote)
        offset = wave * 2
        print(f"{Colors.DIM}{' ' * offset}{underline}{Colors.RESET}")
        time.sleep(0.15)
    
    # Author attribution
    print(f"{Colors.BRIGHT_BLACK}{Colors.ITALIC}{author}{Colors.RESET}")
    time.sleep(0.5)
    
    # Phase 4: Existential aftermath
    print(f"\n{Colors.DIM}{'🤔'.center(TERMINAL_WIDTH // 2)}{Colors.RESET}")
    time.sleep(0.7)
    
    # Final boxed wisdom
    print_boxed("Then you die. And then what?", color=Colors.BRIGHT_MAGENTA)


def main():
    # Original Woody Allen-style quote (neurotic, existential, self-deprecating)
    quote = (
        "I've had a terribly anxious day. This morning I woke up, "
        "I looked in the mirror, and I saw my face. That was bad enough. "
        "Then I realized it's going to get worse—because eventually, "
        "I won't even be around to see it get worse. So I'm anxious about "
        "anxious-ness. It's anxiety all the way down, like a cosmic joke "
        "where the punchline is: you."
    )
    
    # Print a header
    header = f"{Colors.BRIGHT_CYAN}{Colors.BOLD}"
    header += "=" * TERMINAL_WIDTH + "\n"
    header += "  WOODY ALLEN'S DIGITAL ANXIETY CLINIC".center(TERMINAL_WIDTH)
    header += f"\n{'=' * TERMINAL_WIDTH}{Colors.RESET}"
    
    print(header)
    
    # Add a subtitle
    subtitle = f"{Colors.BRIGHT_MAGENTA}{Colors.ITALIC}"
    subtitle += "  Existential Therapy Session #42 - No Cure Guaranteed".center(TERMINAL_WIDTH)
    subtitle += f"{Colors.RESET}"
    print(subtitle)
    
    # Show the animated quote
    animated_quote(quote)
    
    # Bottom footer
    print(f"\n{Colors.DIM}{'=' * TERMINAL_WIDTH}{Colors.RESET}")
    print(f"{Colors.BRIGHT_BLACK}  Remember: You are a speck of stardust having an anxiety attack "
          f"{Colors.RESET}")
    print(f"{Colors.BRIGHT_BLACK}  about whether the speck of stardust cares about the anxiety. "
          f"{Colors.RESET}")
    print(f"{Colors.DIM}{'=' * TERMINAL_WIDTH}{Colors.RESET}")


if __name__ == "__main__":
    main()