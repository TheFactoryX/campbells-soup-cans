"""
Campbell's Soup Can #3387
Produced: 2026-04-21 14:08:24
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.05, color=Colors.WHITE):
    """Simulate a typewriter effect with colored text"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.END)
    print()

def print_frame(text, border_char='*'):
    """Print text in a decorative frame"""
    lines = text.split('\n')
    max_width = max(len(line) for line in lines)
    
    # Top border with animation
    for i in range(3):
        print(Colors.YELLOW + " " + border_char * (max_width + 2) + " " + Colors.END)
        time.sleep(0.1)
    
    # Content
    for i, line in enumerate(lines):
        if i == 0 or i == len(lines) - 1:
            print(f"{Colors.YELLOW}{border_char}{Colors.BOLD} {line} {Colors.YELLOW}{border_char}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}{border_char} {Colors.WHITE}{line} {Colors.YELLOW}{border_char}{Colors.END}")
    
    # Bottom border with animation
    for i in range(3):
        print(Colors.YELLOW + " " + border_char * (max_width + 2) + " " + Colors.END)
        time.sleep(0.1)

def animate_quote_appearance(text):
    """Create a simple animation for the quote appearance"""
    print("\n")
    lines = text.split('\n')
    for i, line in enumerate(lines):
        typewriter(line, delay=0.03)
        if i < len(lines) - 1:
            print(Colors.CYAN + " |" + Colors.END)
    print("\n")

def main():
    # Woody Allen style quote
    quote = """I'm not afraid of death; I just don't want to be there when it happens.
You know, I've often wondered if life is just one big cosmic joke,
and I'm the punchline. I mean, here I am, worrying about whether
I should have the chocolate mousse or the sorbet, while somewhere
in the universe, a star is exploding. It's enough to make you
want to become a librarian. At least the books don't judge you."""
    
    clear_screen()
    
    # Print header with typewriter effect
    print(Colors.MAGENTA + "\n" + "=" * 70 + "\n")
    typewriter("\t\tWOODY ALLEN ON EXISTENTIAL DREAD", delay=0.03, color=Colors.CYAN)
    print(Colors.MAGENTA + "=" * 70 + "\n" + Colors.END)
    
    # Print Woody Allen ASCII art
    woody_art = [
        "      .--.",
        "     |o_o |",
        "     |:_/ |",
        "     //   \\ \\",
        "   (|     | )",
        "  /'\\_   _/`\\",
        "  \\___)=(___/"
    ]
    
    print(Colors.YELLOW + "\n".join(woody_art) + Colors.END + "\n")
    
    # Print the quote with animation
    animate_quote_appearance(quote)
    
    # Add a footer with Woody Allen's signature
    typewriter("\n\t\t- Woody Allen", delay=0.1, color=Colors.CYAN)
    
    # Add a small philosophical note
    note = "\n\n\t" + Colors.BOLD + "P.S. If you're not terrified, you're not paying attention." + Colors.END
    typewriter(note, delay=0.03, color=Colors.GREEN)
    
    # Add a final thought with typewriter effect
    final_thought = "\n\n\t" + Colors.ITALIC + "PPS. I'm not a pessimist, I'm just a realist with a sense of humor." + Colors.END
    typewriter(final_thought, delay=0.03, color=Colors.RED)

if __name__ == "__main__":
    main()