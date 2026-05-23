"""
Campbell's Soup Can #3761
Produced: 2026-05-23 14:02:15
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
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

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    ITALIC = '\033[3m'
    BG_PURPLE = '\033[45m'

def typewriter(text, delay=0.03, color=Colors.CYAN):
    """Simulate typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Colors.END + '\n')
    sys.stdout.flush()

def print_frame():
    """Print a decorative ASCII frame"""
    frame = [
        "╔══════════════════════════════════════════════════════════════════════════════════════╗",
        "║                                                                                        ║",
        "║                                                                                        ║",
        "║                                                                                        ║",
        "║                                                                                        ║",
        "╚══════════════════════════════════════════════════════════════════════════════════════╝"
    ]
    
    for line in frame:
        typewriter(line, delay=0.01, color=Colors.YELLOW)

def print_quote():
    """Print the Woody Allen style quote with formatting"""
    quote = """
    I tried to find meaning in life once, but I got lost on the way to the therapist's office.
    """
    
    author = "                                — Woody Allen"
    
    # Print quote in a box with different colors
    typewriter("\n    ", delay=0.05, color=Colors.ITALIC)
    typewriter(quote, delay=0.02, color=Colors.CYAN)
    typewriter("\n    ", delay=0.05, color=Colors.ITALIC)
    
    # Author line with different style
    typewriter(author, delay=0.02, color=Colors.BOLD)
    
    # Add a philosophical footer
    footer = [
        "",
        "   LIFE TIP: If you can't find meaning, at least find a good Italian restaurant.",
        "             That's what existential dread is for... to be drowned in carbs."
    ]
    
    for line in footer:
        typewriter(line, delay=0.02, color=Colors.GREEN)

def main():
    """Main function to run the program"""
    # Clear screen (works in most terminals)
    print("\033[2J\033[H", end="")
    
    # Print title
    title = " Woody Allen's Existential Corner "
    typewriter(f"\n{Colors.BOLD}{Colors.YELLOW}{title.center(80)}{Colors.END}\n")
    
    # Print decorative frame
    print_frame()
    
    # Print quote
    print_quote()
    
    # Final message
    typewriter("\n\n" + " Press any key to exit... ", delay=0.02, color=Colors.RED)
    input()

if __name__ == "__main__":
    main()