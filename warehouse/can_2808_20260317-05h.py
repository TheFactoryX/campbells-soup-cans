"""
Campbell's Soup Can #2808
Produced: 2026-03-17 05:03:03
Worker: Anthropic: Claude Sonnet 4 (anthropic/claude-sonnet-4)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def create_fancy_border(width=80):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    border = ""
    for i in range(width):
        color = random.choice(colors)
        border += f"{color}{'~' if i % 2 == 0 else '*'}"
    return border + '\033[0m'

def woody_allen_quote_display():
    clear_screen()
    
    # Color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    
    # Create animated title
    title_art = f"""
{YELLOW}{BOLD}
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║                                                                          ║
    ║              🎭 WOODY ALLEN'S WISDOM MACHINE 🎭                         ║
    ║                                                                          ║
    ╚══════════════════════════════════════════════════════════════════════════╝
{RESET}
    """
    
    print(title_art)
    time.sleep(1)
    
    # Animated dots
    print(f"{CYAN}Generating existential crisis", end="")
    for i in range(10):
        print(".", end="", flush=True)
        time.sleep(0.2)
    print(f" COMPLETE!{RESET}\n")
    
    # The quote
    quote = "I took a test in Existentialism. I left all the answers blank and got 100. But then I realized that meant I existed, which ruined my whole day."
    
    # Create fancy quote box with ASCII art
    print(f"{create_fancy_border()}")
    print(f"{PURPLE}║{RESET}")
    print(f"{PURPLE}║{WHITE}{BOLD}    💭 Today's Neurotic Nugget of Wisdom:{RESET}{PURPLE}                                    ║{RESET}")
    print(f"{PURPLE}║{RESET}")
    
    # Split quote into lines for better formatting
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(' '.join(current_line + [word])) <= 60:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    # Print quote with typewriter effect
    for line in lines:
        print(f"{PURPLE}║{GREEN}    \"{line}{GREEN}\"{RESET}{PURPLE}                                                     ║{RESET}"[:78] + f"{PURPLE}║{RESET}")
        time.sleep(0.5)
    
    print(f"{PURPLE}║{RESET}")
    print(f"{PURPLE}║{YELLOW}                                           - Definitely Woody Allen{RESET}{PURPLE}    ║{RESET}")
    print(f"{PURPLE}║{RESET}")
    print(f"{create_fancy_border()}")
    
    # Animated thinking face
    faces = ["🤔", "😅", "😰", "🤷‍♂️", "💭"]
    print(f"\n{CYAN}Contemplating the meaninglessness of it all: ", end="")
    
    for _ in range(15):
        face = random.choice(faces)
        print(f"\r{CYAN}Contemplating the meaninglessness of it all: {face}", end="", flush=True)
        time.sleep(0.3)
    
    print(f"\r{CYAN}Contemplating the meaninglessness of it all: ✨ ENLIGHTENED! ✨{RESET}")
    
    # Final flourish
    print(f"\n{BOLD}{RED}Remember: Life is a comedy for those who think, a tragedy for those who feel,")
    print(f"and a complete mystery for those who try to understand Woody Allen quotes!{RESET}\n")

if __name__ == "__main__":
    woody_allen_quote_display()