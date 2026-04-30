"""
Campbell's Soup Can #3512
Produced: 2026-04-30 22:09:33
Worker: Poolside: Laguna M.1 (free) (poolside/laguna-m.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI color codes
GREEN = '\033[32m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
RED = '\033[31m'
BOLD = '\033[1m'
RESET = '\033[0m'

def animate_text(text, color=RESET, delay=0.05):
    """Animate text character by character with optional color"""
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def print_quote_box():
    quote_lines = [
        f"{YELLOW}I don't fear death,{RESET}",
        f"{CYAN}but I do hope it's not on a Tuesday—{RESET}",
        f"{RED}I have yoga.{RESET}"
    ]
    
    max_width = max(len(line) for line in quote_lines) + 4
    border = f"{GREEN}═{RESET}" * (max_width)
    
    # Top border with animation
    print(f"\n{GREEN}  ╔═{RESET}", end='')
    for _ in range(max_width-4):
        print(f"{GREEN}═{RESET}", end='', flush=True)
        time.sleep(0.02)
    print(f"═╗{RESET}\n")
    
    # Quote lines with animation
    for line in quote_lines:
        print(f"{GREEN}  ║{RESET} ", end='')
        animate_text(line.center(max_width-4), color=RESET, delay=0.03)
        print(f"{GREEN} ║{RESET}")
    
    # Bottom border
    print(f"{GREEN}  ╚═{RESET}", end='')
    for _ in range(max_width-4):
        print(f"{GREEN}═{RESET}", end='', flush=True)
        time.sleep(0.02)
    print(f"═╝{RESET}\n")

def artistic_exclamation():
    print(f"""
{CYAN}    __      __   _                           {RESET}
{CYAN}    \\ \\    / //  | |                          {RESET}
{CYAN}     \\ \\  / //__ | | ___  _   _ _ __   __ _   {RESET}
{YELLOW}      \\ \\/ // _ \\| |/ _ \\| | | | '_ \\ / _` |  {RESET}
{YELLOW}       \\  //  __/| | (_) | |_| | | | | (_| |  {RESET}
{RED}        \\// \\___||_|\\___/ \\__,_|_| |_|\\__, |  {RESET}
{RED}                                       __/ |  {RESET}
{RED}                                      |___/   {RESET}

{GREEN}         A Philosophical Quote by Woody Allen{RESET}
""")

if __name__ == "__main__":
    artistic_exclamation()
    print_quote_box()
    
    # Final flourish
    print(f"{CYAN}  ( •_•)  ╭͈■͈╮\n  ( つ  ͈╭͈■͈╮ )  ", end='')
    time.sleep(0.5)
    print(f"{YELLOW}"Oh my god..."{RESET}\n")