"""
Campbell's Soup Can #4877
Produced: 2026-08-31 20:05:44
Worker: MiniMax: MiniMax M3 (free) (minimax/minimax-m3:free)
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

# ANSI escape codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
BLINK = "\033[5m"
REVERSE = "\033[7m"

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"

# Backgrounds
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.04, color=WHITE):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def rainbow_typewriter(text, delay=0.03):
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    for i, char in enumerate(text):
        if char == ' ':
            sys.stdout.write(char)
        else:
            color = colors[i % len(colors)]
            sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(width, height, title=""):
    top = f"{YELLOW}╔{'═' * (width - 2)}╗{RESET}"
    bottom = f"{YELLOW}╚{'═' * (width - 2)}╝{RESET}"
    print(top)
    if title:
        title_line = f"{YELLOW}║{RESET}{BOLD}{MAGENTA}{title.center(width - 2)}{RESET}{YELLOW}║{RESET}"
        print(title_line)
        print(f"{YELLOW}╠{'═' * (width - 2)}╣{RESET}")
    for _ in range(height - (2 if title else 0)):
        print(f"{YELLOW}║{RESET}{' ' * (width - 2)}{YELLOW}║{RESET}")
    print(bottom)

def animate_thinking():
    thoughts = [
        f"{GRAY}(hmm...){RESET}",
        f"{GRAY}(well...){RESET}",
        f"{GRAY}(actually...){RESET}",
        f"{GRAY}(you know...){RESET}",
    ]
    for thought in thoughts:
        sys.stdout.write(f"\r{BOLD}{CYAN}Woody Allen is thinking {thought}{RESET}   ")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\r" + " " * 60 + "\r", end="")

def main():
    clear()

    # Header
    print(f"\n{BOLD}{YELLOW}{'═' * 70}{RESET}")
    print(f"{BOLD}{YELLOW}║{RESET}{BLINK}{RED}  ✦  P H I L O S O P H I C A L   N E U R O S I S   ✦  {RESET}{BOLD}{YELLOW}║{RESET}")
    print(f"{BOLD}{YELLOW}{'═' * 70}{RESET}\n")

    time.sleep(1)

    # Skull animation
    skull_frames = [
        f"""
        {GRAY}☠ ☠ ☠ ☠ ☠{RESET}
       {GRAY}☠{RESET}         {GRAY}☠{RESET}
      {GRAY}☠{RESET}  {WHITE}○   ○{RESET}  {GRAY}☠{RESET}
      {GRAY}☠{RESET}    {WHITE}▽{RESET}    {GRAY}☠{RESET}
       {GRAY}☠{RESET}  {WHITE}╲╱{RESET}  {GRAY}☠{RESET}
        {GRAY}☠ ☠ ☠ ☠ ☠{RESET}
        """,
    ]

    print(f"{DIM}{GRAY}*cue the anxious jazz music*{RESET}\n")
    time.sleep(1.5)

    # The quote with fancy presentation
    print(f"{YELLOW}{'─' * 70}{RESET}")
    print(f"{YELLOW}│{RESET}                                                                {YELLOW}│{RESET}")
    print(f"{YELLOW}│{RESET}                                                                {YELLOW}│{RESET}")

    quote_line_1 = "I'm not afraid of death..."
    quote_line_2 = "I just don't want to be there"
    quote_line_3 = "when it happens."

    # Animate the quote line by line
    print(f"{YELLOW}│{RESET}  {BOLD}{CYAN}\"{RESET}", end="")
    rainbow_typewriter(f"  {quote_line_1}  ", delay=0.035)
    print(f"{YELLOW}│{RESET}")

    sys.stdout.write(f"{YELLOW}│{RESET}  {BOLD}{CYAN}\"{RESET}  ")
    typewriter(quote_line_2, delay=0.04, color=ITALIC + WHITE)
    print(f"{YELLOW}│{RESET}")

    sys.stdout.write(f"{YELLOW}│{RESET}  {BOLD}{CYAN}\"{RESET}  ")
    typewriter(quote_line_3, delay=0.04, color=ITALIC + WHITE)
    print(f"{BOLD}{CYAN}\"{RESET}{YELLOW}│{RESET}")

    print(f"{YELLOW}│{RESET}                                                                {YELLOW}│{RESET}")
    print(f"{YELLOW}│{RESET}                  {DIM}{GRAY}— Woody Allen{RESET}                             {YELLOW}│{RESET}")
    print(f"{YELLOW}│{RESET}                                                                {YELLOW}│{RESET}")
    print(f"{YELLOW}{'─' * 70}{RESET}")

    time.sleep(1.5)

    # Existential panic
    print()
    animate_thinking()

    panic_messages = [
        f"{RED}{BOLD}Wait...{RESET} am I alive?",
        f"{YELLOW}Is my therapist awake at this hour?{RESET}",
        f"{MAGENTA}What if the universe is just my apartment?{RESET}",
        f"{CYAN}I should really call my mother more often.{RESET}",
        f"{GREEN}...or maybe not. She's exhausting.{RESET}",
    ]

    for msg in panic_messages:
        print(f"  {DIM}{GRAY}💭 {msg}{RESET}")
        time.sleep(0.8)

    # Animated final thought
    print()
    time.sleep(1)
    print(f"{BOLD}{YELLOW}┌{'─' * 50}┐{RESET}")
    print(f"{BOLD}{YELLOW}│{RESET}", end="")

    final_thought = " Tomorrow is a myth I keep postponing.  "
    rainbow_typewriter(final_thought, delay=0.03)
    print(f"{BOLD}{YELLOW}│{RESET}")
    print(f"{BOLD}{YELLOW}└{'─' * 50}┘{RESET}")

    # Footer
    print()
    time.sleep(0.5)
    print(f"{DIM}{GRAY}        ♪ ♫ ♪  *sad saxophone plays in the distance*  ♪ ♫ ♪{RESET}")
    print()
    print(f"{BOLD}{WHITE}                    — fin —{RESET}\n")
    print(f"{DIM}{GRAY}        (or as Allen would say: 'Why does fin rhyme with begin?'{RESET}")
    print(f"{DIM}{GRAY}         'Because everything ends just as it should continue.'){RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}Existence interrupted.{RESET}")