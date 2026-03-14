"""
Campbell's Soup Can #2761
Produced: 2026-03-14 11:38:29
Worker: Qwen: Qwen3.5-27B (qwen/qwen3.5-27b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI Escape Codes for Colors and Styles
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
GREEN = "\033[92m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
GRAY = "\033[90m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, color=WHITE, delay=0.03):
    """Prints text with a typewriter effect and specified color."""
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(text, width=60):
    """Draws a decorative ASCII box around text."""
    border = CYAN + "╔" + "═" * (width - 2) + "╗" + RESET
    print(border)
    # Center the text
    padding = (width - 4 - len(text)) // 2
    print(f"{CYAN}║{RESET}{' ' * padding}{text}{' ' * (width - 4 - padding - len(text))}{CYAN}║{RESET}")
    print(border)

def draw_glasses():
    """ASCII Art of Woody Allen's iconic glasses."""
    art = [
        f"{YELLOW}      .--.  .--.{RESET}",
        f"{YELLOW}     /    \\/    \\{RESET}",
        f"{YELLOW}    |      |      |{RESET}",
        f"{YELLOW}    \\      /      /{RESET}",
        f"{YELLOW}     '----'  '----'{RESET}"
    ]
    for line in art:
        print(line)

def main():
    clear_screen()
    
    # ASCII Art Header
    print(f"{MAGENTA}\n      .--------------------------.{RESET}")
    print(f"{MAGENTA}      |  THE WOODY ALLEN QUOTE   |{RESET}")
    print(f"{MAGENTA}      '--------------------------'{RESET}\n")
    
    draw_glasses()
    print(f"\n{GRAY}      (Thinking...){RESET}\n")
    
    # The Quote
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying. But mostly, I just want to find my keys."
    
    # Visual Box for Quote
    print(f"{BOLD}{CYAN}╔════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║{RESET} {YELLOW}  (Neurotic Thought Bubble)  {RESET}{BOLD}{CYAN}║{RESET}")
    print(f"{BOLD}{CYAN}╚════════════════════════════════════════════════════════╝{RESET}")
    print()
    
    # Typewriter Effect with Color Variation
    words = quote.split()
    colors = [YELLOW, CYAN, GREEN, MAGENTA, RED, WHITE]
    
    for i, word in enumerate(words):
        color = colors[i % len(colors)]
        type_writer(f"{word} ", color, delay=0.05)
        if word.endswith('.'):
            break
    
    print()
    time.sleep(0.5)
    
    # Signature
    print(f"{GRAY}      — W. Allen (Probably){RESET}\n")
    
    # Footer
    print(f"{BOLD}{RED}╔════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{RED}║{RESET} {WHITE}  Existence is a mistake, but the coffee is good.      {RESET}{BOLD}{RED}║{RESET}")
    print(f"{BOLD}{RED}╚════════════════════════════════════════════════════════╝{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Interrupted. Existence cancelled.{RESET}")
        sys.exit(0)