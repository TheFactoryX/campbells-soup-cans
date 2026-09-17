"""
Campbell's Soup Can #4978
Produced: 2026-09-17 18:14:53
Worker: inclusionAI: Ling 3.0 Flash Fin (free) (inclusionai/ling-3.0-flash-fin:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
import os

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
BG_BLACK = "\033[40m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03, color=WHITE, bold=False):
    """Print text with a typewriter effect."""
    prefix = BOLD if bold else ""
    for char in text:
        if char == '\n':
            sys.stdout.write(RESET + "\n" + prefix + color)
        else:
            sys.stdout.write(prefix + color + char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.005, 0.01))
    sys.stdout.write(RESET + "\n")

def flash_text(text, color=YELLOW, iterations=3):
    """Blink a piece of text."""
    for _ in range(iterations):
        sys.stdout.write(f"\r{color}{BOLD}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{DIM}{color}{text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write(f"\r{color}{BOLD}{text}{RESET}\n")

def ascii_banner():
    """Print a decorative ASCII banner."""
    banner = f"""
{RED}╔══════════════════════════════════════════════════════╗
{RED}║                                                      ║
{RED}║   {CYAN}★ {YELLOW}╔══════════════════════╗ {CYAN}★                    ║
{RED}║   {CYAN}★ {YELLOW}║  THE EXISTENTIAL    ║ {CYAN}★                    ║
{RED}║   {CYAN}★ {YELLOW}║  CRISIS MACHINE    ║ {CYAN}★                    ║
{RED}║   {CYAN}★ {YELLOW}║  v2.0 (unstable)   ║ {CYAN}★                    ║
{RED}║   {CYAN}★ {YELLOW}╚══════════════════════╝ {CYAN}★                    ║
{RED}║                                                      ║
{RED}╚══════════════════════════════════════════════════════╝
"""
    for line in banner.split('\n'):
        if line.strip():
            sys.stdout.write(line + "\n")
            time.sleep(0.05)
    time.sleep(0.5)

def spiral_decoration():
    """Print a little spiral art."""
    spiral = f"""
{MAGENTA}          .-~~~-.
{MAGENTA}        .'       '.
{MAGENTA}       /  o   o   \
{MAGENTA}      |    _    |
{MAGENTA}       \  '~~~'  /
{MAGENTA}        '-.   .-'
{MAGENTA}           '~~~'
{RESET}"""
    print(spiral)

def main():
    clear_screen()
    
    # Print banner with delay
    ascii_banner()
    time.sleep(0.3)
    
    # Print philosophical question with typewriter
    sys.stdout.write(f"\n{BLUE}{BOLD}")
    print()
    typewriter("       A Question of Importance:", delay=0.05, color=CYAN, bold=True)
    time.sleep(0.5)
    
    print()
    
    # The quote itself - typewriter effect with color cycling
    quote = (
        "I refuse to join any club that would have me as a member.\n"
        "But more importantly —\n"
        "I'm not afraid of death; I just don't want to be there\n"
        "when it happens. And even THEN, I'll probably worry\n"
        "about whether I'm dressed appropriately for the afterlife.\n"
        "\n"
        "As Woody once whispered into a mirror:\n"
        f"  {YELLOW}“The universe is under no obligation\n"
        f"   to make sense to you —\n"
        f"   but wouldn't it be nice if it at least\n"
        f"   made sense to someone else?”"
    )
    
    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
    lines = quote.split('\n')
    
    for i, line in enumerate(lines):
        if line.strip() == "":
            print()
            time.sleep(0.2)
        elif line.startswith("  “"):
            typewriter(line, delay=0.04, color=YELLOW)
            time.sleep(0.3)
        elif "Woody" in line:
            flash_text(line.strip(), color=CYAN, iterations=2)
        else:
            color = colors[i % len(colors)]
            typewriter(line, delay=0.03, color=color)
        time.sleep(0.15)
    
    time.sleep(0.5)
    
    # Print existential despair with animation
    print()
    typewriter(
        f"{RED}{BOLD}⏳ Calculating the probability of happiness... "
        f"{DIM}(result: approximately 3%){RESET}",
        delay=0.08, color=RED
    )
    time.sleep(0.3)
    
    print()
    
    # Print footer with a wink
    footer = (
        f"{DIM}╭─────────────────────────────────╮\n"
        f"{DIM}│                                 │\n"
        f"{MAGENTA}│  {BOLD}“I’m not great at the advice.\n"
        f"{MAGENTA}│   {BOLD}Can I interest you in a sarcastic\n"
        f"{MAGENTA}│   {BOLD}comment?” — Woody Allen{RESET}{DIM}\n"
        f"{DIM}│                                 │\n"
        f"{DIM}╰─────────────────────────────────╯{RESET}"
    )
    print(footer)
    
    # Final blink
    time.sleep(0.5)
    flash_text(f"{BLINK}{YELLOW}{BOLD}  ★ You're alive. That's either brave or stupid. ★{RESET}", iterations=4)
    
    print()
    typewriter(f"{DIM}  [Press Ctrl+C to achieve inner peace... or just close the terminal]", delay=0.05, color=DIM)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}{BOLD}\n\nWell, that was awkward. 😏\n{RESET}")
        sys.exit(0)