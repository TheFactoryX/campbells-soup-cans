"""
Campbell's Soup Can #4283
Produced: 2026-07-21 22:11:58
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Style Philosophical Quote Generator
A neurotic journey through existence, one colorful quote at a time.
"""

import sys
import time
import random

# ANSI color codes for maximum visual impact
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'

# Woody Allen's neurotic wisdom collection
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "More than any other time in history, mankind faces a crossroads. One path leads to despair and utter hopelessness, the other to total extinction. Let us have the wisdom to choose correctly.",
    "I've never been a millionaire, but I've always wanted to be one. I've never been a failure either, which is unusual for me.",
    "The ratio of successful people to total people is like the ratio of lightning to actual shit. It's very rare.",
    "I'm a great believer in luck, and I find the harder I work, the luckier I am. Unfortunately, my definition of 'hard work' is lying in bed worrying.",
    "I don't have a health problem. I have several. I have diabetes, high blood pressure, heart trouble, and occasional dizzy spells. But I don't have a health problem.",
    "I've had more intelligence than most people my age, and I've done nothing with it. That makes me very proud.",
    "I once stole a sign that said 'Watch for children' and I thought, that's a fair trade."
]

def print_with_delay(text, delay=0.03):
    """Print text character by character for dramatic effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_woody_allen_ascii():
    """Print Woody Allen ASCII art"""
    ascii_art = f"""
{Colors.YELLOW}    ╔══════════════════════════════════════╗
    ║     WOODY ALLEN PHILOSOPHICAL        ║
    ║         NEUROTIC WISDOM ™            ║
    ╚══════════════════════════════════════╝
{Colors.CYAN}
        .-""-.
       / - -  \\
      |  .-.  |
      |  \\o/  |
       \\  '   /
        '-.-'
{Colors.RESET}
    """
    print(ascii_art)

def animate_quote_display(quote):
    """Animate the quote display with colors and effects"""
    # Create a colorful border
    border_width = max(len(quote) + 10, 60)
    
    print(f"\n{Colors.MAGENTA}{'═' * border_width}")
    print(f"{'║':^{border_width}}")
    
    # Split quote into lines for better display
    words = quote.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + word) <= 50:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line.strip():
        lines.append(current_line.strip())
    
    # Print each line with animation
    for i, line in enumerate(lines):
        padding = (border_width - 4 - len(line)) // 2
        print(f"{'║':<{padding+1}}", end="")
        print_with_delay(f"{Colors.YELLOW}{line}{Colors.RESET}", 0.02)
        print(f"{'':<{padding+1}}{Colors.MAGENTA}║")
    
    print(f"{'║':^{border_width}}")
    print(f"{Colors.MAGENTA}{'═' * border_width}")

def print_neurotic_footer():
    """Print a neurotic footer"""
    footer_lines = [
        f"{Colors.DIM}─────────────────────────────────────────────{Colors.RESET}",
        f"{Colors.CYAN}As Woody Allen might say: 'Existence is absurd,'{Colors.RESET}",
        f"{Colors.CYAN}but at least the font looks good while we're{Colors.RESET}",
        f"{Colors.CYAN}contemplating our inevitable doom.{Colors.RESET}",
        f"{Colors.DIM}─────────────────────────────────────────────{Colors.RESET}"
    ]
    
    for line in footer_lines:
        time.sleep(0.3)
        print(line)

def main():
    """Main function to display Woody Allen wisdom"""
    # Clear screen (works on most terminals)
    print('\033[2J\033[H', end='')
    
    # Print the header
    print_woody_allen_ascii()
    
    # Dramatic pause
    time.sleep(1)
    
    # Select a random quote
    quote = random.choice(QUOTES)
    
    # Animate the quote
    animate_quote_display(quote)
    
    # Print neurotic footer
    print()
    print_neurotic_footer()
    
    # Final existential crisis
    print(f"\n{Colors.RED}{Colors.BOLD}Remember: You're just a speck of stardust{Colors.RESET}")
    print(f"{Colors.RED}{Colors.BOLD}having an existential crisis about being{Colors.RESET}")
    print(f"{Colors.RED}{Colors.BOLD}a speck of stardust. How meta!{Colors.RESET}")

if __name__ == "__main__":
    main()