"""
Campbell's Soup Can #3778
Produced: 2026-05-24 21:11:20
Worker: Owl Alpha (openrouter/owl-alpha)
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
import os

# ANSI escape code utilities
class ANSI:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    
    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright foreground colors
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    
    @staticmethod
    def move_up(n=1):
        return f"\033[{n}A"
    
    @staticmethod
    def move_down(n=1):
        return f"\033[{n}B"
    
    @staticmethod
    def move_right(n=1):
        return f"\033[{n}C"
    
    @staticmethod
    def move_left(n=1):
        return f"\033[{n}D"
    
    @staticmethod
    def clear_screen():
        return "\033[2J\033[H"
    
    @staticmethod
    def clear_line():
        return "\033[2K\r"
    
    @staticmethod
    def save_cursor():
        return "\033[s"
    
    @staticmethod
    def restore_cursor():
        return "\033[u"
    
    @staticmethod
    def hide_cursor():
        return "\033[?25l"
    
    @staticmethod
    def show_cursor():
        return "\033[?25h"


def slow_print(text, delay=0.03, color=None):
    """Print text character by character with optional color."""
    for char in text:
        if color:
            sys.stdout.write(f"{color}{char}{ANSI.RESET}")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def center_text(text, width=80):
    """Center text within a given width."""
    return text.center(width)


def create_box(text, width=70, color=ANSI.CYAN, title=None):
    """Create a decorative box around text."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    box_width = max_len + 4
    
    result = []
    
    # Top border
    if title:
        title_str = f" {title} "
        title_pos = (box_width - len(title_str)) // 2
        top = f"{color}╔{'═' * title_pos}{ANSI.BRIGHT_WHITE}{title_str}{color}{'═' * (box_width - title_pos - len(title_str))}╗{ANSI.RESET}"
    else:
        top = f"{color}╔{'═' * box_width}╗{ANSI.RESET}"
    result.append(top)
    
    # Empty line
    result.append(f"{color}║{' ' * box_width}║{ANSI.RESET}")
    
    # Content lines
    for line in lines:
        padding = box_width - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        result.append(f"{color}║{' ' * left_pad}{ANSI.BRIGHT_WHITE}{line}{color}{' ' * right_pad}║{ANSI.RESET}")
    
    # Empty line
    result.append(f"{color}║{' ' * box_width}║{ANSI.RESET}")
    
    # Bottom border
    bottom = f"{color}╚{'═' * box_width}╝{ANSI.RESET}"
    result.append(bottom)
    
    return '\n'.join(result)


def create_thought_bubble(text, width=60):
    """Create a thought bubble."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    result = []
    
    # Top border
    result.append(f"  {'_' * (max_len + 2)}")
    
    # Content
    for i, line in enumerate(lines):
        if i == 0:
            result.append(f" ( {line}{' ' * (max_len - len(line))} )")
        else:
            result.append(f" ( {line}{' ' * (max_len - len(line))} )")
    
    # Bottom border
    result.append(f"  {'‾' * (max_len + 2)}")
    
    return '\n'.join(result)


def animate_loading(duration=2.0, message="Contemplating existence..."):
    """Show a loading animation."""
    frames = ["◐", "◓", "◑", "◒"]
    end_time = time.time() + duration
    i = 0
    
    while time.time() < end_time:
        frame = frames[i % len(frames)]
        sys.stdout.write(f"\r{ANSI.YELLOW}{frame}{ANSI.RESET} {message}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    
    sys.stdout.write(f"\r{ANSI.GREEN}✓{ANSI.RESET} {message} Done!{ANSI.RESET}\n")


def get_terminal_width():
    """Get terminal width, default to 80 if not available."""
    try:
        return os.get_terminal_size().columns
    except:
        return 80


def main():
    # Hide cursor for cleaner output
    sys.stdout.write(ANSI.hide_cursor())
    sys.stdout.flush()
    
    # Clear screen
    sys.stdout.write(ANSI.clear_screen())
    sys.stdout.flush()
    
    # Get terminal width
    term_width = get_terminal_width()
    
    # The quote
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    
    # Author
    author = "— Woody Allen"
    
    # Show loading animation
    animate_loading(1.5, "Accessing existential dread database...")
    time.sleep(0.5)
    
    # Clear screen
    sys.stdout.write(ANSI.clear_screen())
    sys.stdout.flush()
    
    # Print top margin
    print("\n" * 3)
    
    # Print the main quote in a decorative box
    quote_box = create_box(quote, title="EXISTENTIAL WISDOM")
    print(quote_box)
    
    print()
    
    # Print author attribution
    author_line = f"  {ANSI.ITALIC}{ANSI.DIM}{author}{ANSI.RESET}"
    print(author_line)
    
    print()
    
    # Print a decorative separator
    separator = f"{ANSI.CYAN}{'─' * 70}{ANSI.RESET}"
    print(separator)
    
    print()
    
    # Print some "analysis" of the quote
    analysis = [
        f"{ANSI.BRIGHT_CYAN}Analysis:{ANSI.RESET}",
        f"  {ANSI.YELLOW}•{ANSI.RESET} Contains {ANSI.BRIGHT_WHITE}2{ANSI.RESET} contradictory desires",
        f"  {ANSI.YELLOW}•{ANSI.RESET} References mortality {ANSI.BRIGHT_WHITE}1{ANSI.RESET} time",
        f"  {ANSI.YELLOW}•{ANSI.RESET} Implies work is {ANSI.BRIGHT_WHITE}not{ANSI.RESET} the answer",
        f"  {ANSI.YELLOW}•{ANSI.RESET} Suggests death is {ANSI.BRIGHT_WHITE}optional{ANSI.RESET} (it's not)",
    ]
    
    for line in analysis:
        print(line)
        time.sleep(0.1)
    
    print()
    
    # Print a thought bubble with a follow-up thought
    follow_up = "But what if my work IS me not dying?"
    bubble = create_thought_bubble(follow_up)
    print(bubble)
    
    print()
    
    # Print a final message
    final_msg = f"{ANSI.BRIGHT_MAGENTA}Remember: The universe is expanding, and so is your anxiety.{ANSI.RESET}"
    print(final_msg)
    
    print()
    
    # Print bottom margin
    print("\n" * 3)
    
    # Show cursor again
    sys.stdout.write(ANSI.show_cursor())
    sys.stdout.flush()


if __name__ == "__main__":
    main()