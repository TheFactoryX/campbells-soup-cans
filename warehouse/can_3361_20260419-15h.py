"""
Campbell's Soup Can #3361
Produced: 2026-04-19 15:54:24
Worker: Elephant (openrouter/elephant-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# Woody Allen style philosophical quote
quote = (
    "I'm not afraid of death; I just don't want to be there when it happens.\n"
    "It's like showing up late to a party you weren't invited to in the first place."
)

# ANSI color codes
class Colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# ASCII Art - Woody Allen's brain
woody_brain = r"""
      .-''''''''''-._
     /                    \
    /  (o     o    o)    \
   /    '  (,  ,`)  '      \
  /       '---'          \
 /        .---.           \
|        /   o \           |
|       /     \           |
|      |       |          |
|      |  () ()  |          .--.
|       \  ^  /           .'    '.
 \        /   \         .'        '.
  \      /     \       /            \
   '.    |       |    /              '.
     '-._|       |_.'                  '-.
       /                                \
      /                                  \
     /                                    \
    '-._                                 _.'
      '-.__                           __.'
           '-._                   _.'
               '-._             _.'
                   '-.___ _ _ __'
                        (___)
"""

def print_box(text, color=Colors.PURPLE):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    border = '+' + '-' * (max_len + 2) + '+'
    
    print(f"\n{color}{border}{Colors.RESET}")
    for line in lines:
        print(f"{color}| {line.ljust(max_len)} |{Colors.RESET}")
    print(f"{color}{border}{Colors.RESET}\n")

def typewriter_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print("\n" * 2)
    
    # Title with animation
    title = "WOODY ALLEN'S PHILOSOPHICAL INQUIRY"
    print(f"{Colors.BOLD}{Colors.UNDERLINE}{Colors.PURPLE}")
    for i in range(len(title)):
        print(title[:i+1], end='\r')
        time.sleep(0.05)
    print(f"{Colors.RESET}\n")
    
    # ASCII Art with color
    print(f"{Colors.CYAN}{woody_brain}{Colors.RESET}")
    time.sleep(1)
    
    # Animated quote presentation
    print(f"\n{Colors.YELLOW}Preparing your existential crisis...{Colors.RESET}")
    time.sleep(1)
    
    print(f"\n{Colors.DARK_RED}{Colors.BOLD}")
    typewriter_effect(quote)
    print(f"{Colors.RESET}")
    
    # Final philosophical box
    print_box(
        "The universe is indifferent.\n"
        "So are most people.\n"
        "You should really work on your relationship with\n"
        "the void... and your mother.",
        Colors.GREEN
    )
    
    # Footer
    print(f"{Colors.BOLD}{Colors.UNDERLINE}{Colors.PURPLE}Existentialism: now with 200% more anxiety!{Colors.RESET}\n")

if __name__ == "__main__":
    main()