"""
Campbell's Soup Can #4954
Produced: 2026-09-13 06:11:06
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI escape codes
class C:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    RESET = '\033[0m'
    BG_DARK = '\033[40m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewrite(text, color=C.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def flash_text(text, color, times=3):
    for _ in range(times):
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(0.05)
        sys.stdout.write('\r' + text)
        sys.stdout.flush()
        time.sleep(0.05)

def main():
    clear()
    
    # ASCII Art - Woody Allen neurotic face
    art = f"""
{C.RED}     _____
{C.RED}    /     \\
{C.RED}   | o   o |
{C.RED}   |   >   |
{C.RED}    \\_____/
{C.RED}     |   |{C.RESET}
"""
    print(art)
    time.sleep(0.3)

    # Title
    title = f"{C.YELLOW}{C.BOLD}╔{'═'*58}╗{C.RESET}"
    print(title)
    print(f"{C.YELLOW}{C.BOLD}║{C.CYAN}{C.BOLD}{'  🎭  Woody Allen\'s Existential Crisis Generator  🎭  ':^56}{C.YELLOW}{C.BOLD}║{C.RESET}")
    print(title)
    print()

    # Quote box
    border = f"{C.MAGENTA}{C.BOLD}┌{'─'*62}┐{C.RESET}"
    print(border)
    
    quote_lines = [
        "I'm not afraid of death. I just don't want to be there",
        "when it happens. Also, the afterlife has no WiFi and",
        "the seating is terrible. I asked God about the seating",
        "arrangement and He said 'thou shalt not complain.'",
        "So here I am, complaining. It's therapeutic.",
    ]
    
    for line in quote_lines:
        padded = f"{C.WHITE}{C.BOLD}│{C.GREEN} {line:<60} {C.WHITE}{C.BOLD}│{C.RESET}"
        print(padded)
        time.sleep(0.15)
    
    print(border)
    print()

    # Funny footnotes
    footnotes = [
        f"{C.DIM}{C.ITALIC}- Sigmund Freud (probably){C.RESET}",
        f"{C.DIM}{C.ITALIC}- Me, circa 3 AM{C.RESET}",
        f"{C.DIM}{C.ITALIC}- Also me, eating white bread{C.RESET}",
    ]
    for fn in footnotes:
        print(f"  {fn}")
        time.sleep(0.2)
    
    print()
    
    # Final punchline with flash
    punchline = f"{C.RED}{C.BOLD}   💀 LIFE: A FOOL'S ERRAND. AT LEAST THE TICKET IS CHEAP. 💀{C.RESET}"
    flash_text(punchline, C.RED, times=5)
    print()
    print()
    
    # Random existential stats
    stats = [
        f"{C.CYAN}  ▸ Meanings found today: 0{C.RESET}",
        f"{C.CYAN}  ▸ Anxiety level: Maximum{C.RESET}",
        f"{C.CYAN}  ▸ Therapy copay: $200{C.RESET}",
        f"{C.CYAN}  ▸ Reason to continue: ???{C.RESET}",
    ]
    for s in stats:
        print(f"      {s}")
        time.sleep(0.15)
    
    print()
    typewrite(f"  {C.MAGENTA}Press Enter to contemplate your own existence...{C.RESET}", C.MAGENTA, 0.02)
    input()
    
    # Final message
    clear()
    print()
    print(f"  {C.YELLOW}{C.BOLD}   You're still here. That's either courage or denial.{C.RESET}")
    print(f"  {C.DIM}   Either way, the bread is stale.{C.RESET}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}Too existential? Me too.{C.RESET}")
        sys.exit(0)