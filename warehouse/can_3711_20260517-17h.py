"""
Campbell's Soup Can #3711
Produced: 2026-05-17 17:14:53
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def glitch_effect(text, iterations=3):
    glitch_chars = "░▒▓█▄▀■□▪▫"
    for _ in range(iterations):
        glitched = ''.join(random.choice([c, random.choice(glitch_chars)]) for c in text)
        sys.stdout.write(f"\r{glitched}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"\r{text}")

def main():
    # ANSI color codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    
    # Foreground colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    
    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    
    # Clear screen
    print("\033[2J\033[H")
    
    # Title animation
    title = "WOODY ALLEN PRESENTS"
    print(f"\n{CYAN}{'═' * 60}{RESET}")
    time.sleep(0.3)
    print(f"{YELLOW}{BOLD}  🎬 {title} 🎬{RESET}")
    time.sleep(0.3)
    print(f"{CYAN}{'═' * 60}{RESET}\n")
    time.sleep(0.5)
    
    # Dramatic pause with loading dots
    print(f"{DIM}  Loading existential crisis", end="")
    for _ in range(5):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(f" ✓{RESET}\n")
    time.sleep(0.5)
    
    # The quote with typing effect
    quote_lines = [
        f"{BOLD}{WHITE}\"I'm not afraid of death;{RESET}",
        f"{BOLD}{WHITE} I just don't want to be there{RESET}",
        f"{BOLD}{WHITE} when it happens.\"{RESET}"
    ]
    
    print(f"  {DIM}│{RESET}")
    for line in quote_lines:
        print(f"  {DIM}│{RESET}  {line}")
        time.sleep(0.2)
    print(f"  {DIM}│{RESET}")
    time.sleep(0.3)
    
    # Attribution with glitch effect
    attribution = f"  {DIM}│{RESET}  {ITALIC}{MAGENTA}— Woody Allen{RESET}"
    glitch_effect(attribution)
    time.sleep(0.3)
    print(f"  {DIM}│{RESET}")
    print(f"  {DIM}└{'─' * 50}┘{RESET}")
    
    time.sleep(0.5)
    
    # Philosophical "analysis" box
    print(f"\n  {CYAN}┌{'─' * 48}┐{RESET}")
    print(f"  {CYAN}│{RESET} {BOLD}{YELLOW}PHILOSOPHICAL ANALYSIS:{RESET}{' ' * 24}{CYAN}│{RESET}")
    print(f"  {CYAN}│{RESET} {' ' * 46}{CYAN}│{RESET}")
    print(f"  {CYAN}│{RESET} {GREEN}• Fear of non-existence: {RED}HIGH{RESET}{' ' * 21}{CYAN}│{RESET}")
    print(f"  {CYAN}│{RESET} {GREEN}• Desire to witness own funeral: {RED}ABSURD{RESET}{' ' * 16}{CYAN}│{RESET}")
    print(f"  {CYAN}│{RESET} {GREEN}• Existential dread level: {RED}MAXIMUM{RESET}{' ' * 18}{CYAN}│{RESET}")
    print(f"  {CYAN}│{RESET} {' ' * 46}{CYAN}│{RESET}")
    print(f"  {CYAN}│{RESET} {DIM}Conclusion: Life is a brief interlude{RESET}{' ' * 12}{CYAN}│{RESET}")
    print(f"  {CYAN}│{RESET} {DIM}between two eternities of nothing.{RESET}{' ' * 13}{CYAN}│{RESET}")
    print(f"  {CYAN}└{'─' * 48}┘{RESET}")
    
    time.sleep(0.5)
    
    # Animated "THE END" with blinking effect
    print(f"\n  {DIM}Press any key to continue...{RESET}", end="", flush=True)
    input()
    
    print(f"\n  {BLINK}{RED}{BOLD}  ★ ★ ★  THE END  ★ ★ ★{RESET}")
    time.sleep(0.5)
    print(f"\n  {DIM}  (But the anxiety continues...){RESET}\n")

if __name__ == "__main__":
    main()