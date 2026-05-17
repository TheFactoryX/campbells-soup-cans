"""
Campbell's Soup Can #3704
Produced: 2026-05-17 00:08:44
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

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

def slow_print(text, delay=0.03):
    """Print text character by character for dramatic effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    print("\033[2J\033[H", end="")

def draw_thinking_man():
    """ASCII art of a neurotic thinker"""
    man = f"""
{CYAN}        {BOLD}o{RESET}{CYAN}
       /|\\
        |
       / \\
    {DIM}_____________{RESET}
    """
    return man

def draw_existence_box():
    """Draw a philosophical box"""
    box = f"""
{YELLOW}╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   {WHITE}{BOLD}ON EXISTENCE{RESET}{YELLOW}                                                    ║
║                                                                  ║
║   {WHITE}"I finally made peace with the universe.                  {RESET}{YELLOW}║
║   {WHITE} Turns out it doesn't care."{RESET}{YELLOW}                                ║
║                                                                  ║
║   {DIM}{WHITE}— Me, after 47 years of therapy{RESET}{YELLOW}                                ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
    """
    return box

def draw_coffee_cup():
    """Draw a coffee cup for that New York intellectual vibe"""
    cup = f"""
{CYAN}      )  (
     (   ) )
      ) ( (
    _______)_
   |         |
   |  {BOLD}COFFEE{RESET}{CYAN}  |
   |_________|
    \\_______/{RESET}
    """
    return cup

def main():
    clear_screen()
    
    # Title sequence
    print(f"\n{BG_BLUE}{WHITE}{BOLD}{'='*70}{RESET}")
    print(f"{BG_BLUE}{WHITE}{BOLD}  🎬 WOODY ALLEN PHILOSOPHY GENERATOR 🎬{RESET}")
    print(f"{BG_BLUE}{WHITE}{BOLD}{'='*70}{RESET}\n")
    
    # Dramatic pause
    time.sleep(0.5)
    
    # Show the thinker
    print(draw_thinking_man())
    time.sleep(0.3)
    
    # Thinking animation
    print(f"{YELLOW}  Contemplating the void", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print(f"{RESET}\n")
    time.sleep(0.3)
    
    # The main quote with dramatic reveal
    quote_lines = [
        f"{BOLD}{WHITE}\"I've come to terms with my mortality,{RESET}",
        f"{WHITE} but my therapist says I'm still{RESET}",
        f"{WHITE} in denial about my credit score.\"{RESET}",
    ]
    
    # Print with dramatic effect
    print(f"{MAGENTA}  ╭{'─'*60}╮{RESET}")
    print(f"{MAGENTA}  │{RESET}{' '*60}{MAGENTA}│{RESET}")
    
    for line in quote_lines:
        padding = 60 - len(line.replace(BOLD, '').replace(WHITE, '').replace(RESET, '').replace(MAGENTA, '').replace(DIM, '').replace(ITALIC, '').replace(UNDERLINE, '').replace(BLINK, '').replace(RED, '').replace(GREEN, '').replace(YELLOW, '').replace(BLUE, '').replace(CYAN, '').replace(BG_BLACK, '').replace(BG_RED, '').replace(BG_GREEN, '').replace(BG_YELLOW, '').replace(BG_BLUE, '').replace(BG_MAGENTA, '').replace(BG_CYAN, '').replace(BG_WHITE, ''))
        print(f"{MAGENTA}  │{RESET}  {line}{' '*(padding-2)}{MAGENTA}│{RESET}")
    
    print(f"{MAGENTA}  │{RESET}{' '*60}{MAGENTA}│{RESET}")
    print(f"{MAGENTA}  ╰{'─'*60}╯{RESET}\n")
    
    # Attribution
    print(f"{DIM}{ITALIC}  — Woody Allen (probably, if he had worse credit){RESET}\n")
    
    # Bonus existential coffee
    print(draw_coffee_cup())
    
    # Footer
    print(f"\n{GREEN}  ✓ Philosophy delivered. Existential dread included.{RESET}")
    print(f"{DIM}  Side effects may include: anxiety, overthinking, and{RESET}")
    print(f"{DIM}  an inexplicable urge to move to Paris.{RESET}\n")
    
    # Final dramatic exit
    print(f"{RED}{BOLD}  THE END{RESET}")
    print(f"{DIM}  (or is it?){RESET}\n")

if __name__ == "__main__":
    main()