"""
Campbell's Soup Can #5162
Produced: 2026-10-24 23:15:39
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
Woody Allen-style Philosophical Quote Machine
A neurotic journey through existential dread, brought to you in glorious ANSI.
"""

import sys
import time
import os

# ANSI color codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, color=Colors.YELLOW, delay=0.04):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pulse_text(text, duration=2.0):
    """Make text pulse with alternating colors."""
    start = time.time()
    while time.time() - start < duration:
        elapsed = time.time() - start
        # Cycle through colors based on time
        intensity = (elapsed * 10) % 1
        if intensity < 0.5:
            color = Colors.MAGENTA
        else:
            color = Colors.CYAN
        sys.stdout.write(f"\r{Colors.BOLD}{color}{text}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def animated_dots(text, num_dots=3, cycles=3):
    """Animate dots appearing after text."""
    for _ in range(cycles):
        for i in range(num_dots + 1):
            dots = "." * i
            sys.stdout.write(f"\r{Colors.BOLD}{Colors.BLUE}{text}{dots}{Colors.RESET}    ")
            sys.stdout.flush()
            time.sleep(0.2)
    print()

def print_ascii_frame(quote_lines, width=65):
    """Print a decorative ASCII frame around the quote."""
    # Top border
    top_border = f"{Colors.GREEN}╔{'═' * width}╗{Colors.RESET}"
    bottom_border = f"{Colors.GREEN}╚{'═' * width}╝{Colors.RESET}"
    side = f"{Colors.GREEN}║{Colors.RESET}"
    
    print(top_border)
    for line in quote_lines:
        # Center the line within the frame
        padded = line.center(width)
        print(f"{side} {Colors.YELLOW}{padded}{Colors.RESET} {side}")
    print(bottom_border)

def spinning_thing(duration=1.5):
    """A little existential spinner."""
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    start = time.time()
    i = 0
    while time.time() - start < duration:
        sys.stdout.write(f"\r{Colors.MAGENTA}{Colors.BOLD} contemplating existence {spinner[i % len(spinner)]}{Colors.RESET}")
        sys.stdout.flush()
        i += 1
        time.sleep(0.1)
    print()

def main():
    clear_screen()
    
    # Title animation
    title = " WOODY ALLEN QUOTE GENERATOR v3.14159 "
    print(f"\n{Colors.CYAN}{'=' * 60}")
    type_writer(title.center(60), Colors.CYAN, 0.03)
    print(f"{'=' * 60}{Colors.RESET}")
    print()
    
    # Animated intro
    spinning_thing(1.5)
    print()
    
    # The quote - Woody Allen style, neurotic and existential
    quote_lines = [
        "I'm not afraid of death.",
        "I just don't want to be there when it happens.",
        "Which is ironic, because I'm also not",
        "really here right now – just a bunch of",
        "carbon and bad decisions waiting to",
        "turn back into stardust.",
        "",
        "At least the stardust part sounds fancy.",
        "– Me, probably, eventually"
    ]
    
    # Build the frame with typewriter effect
    width = 63
    top_border = f"{Colors.GREEN}╔{'═' * width}╗{Colors.RESET}"
    bottom_border = f"{Colors.GREEN}╚{'═' * width}╝{Colors.RESET}"
    side = f"{Colors.GREEN}║{Colors.RESET}"
    
    sys.stdout.write(top_border + "\n")
    sys.stdout.flush()
    
    for line in quote_lines:
        padded = f" {line} ".center(width)
        for char in padded:
            sys.stdout.write(f"{side}{Colors.YELLOW}{char}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.002)
        sys.stdout.write(f"{side}\n")
        sys.stdout.flush()
        time.sleep(0.3)
    
    sys.stdout.write(bottom_border + "\n")
    sys.stdout.flush()
    
    print()
    
    # Animated dots for dramatic effect
    animated_dots(" (pause for existential dread)", 3, 2)
    print()
    
    # Pulsing footer
    footer = " Remember: You're going to die. Isn't ASCII art beautiful? "
    pulse_text(footer, 2.0)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Interrupted by anxiety.{Colors.RESET}")
        sys.exit(0)