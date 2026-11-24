"""
Campbell's Soup Can #5274
Produced: 2026-11-24 21:11:25
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
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

# ANSI color codes
class C:
    R = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

WOODY_QUOTE = (
    "I don't believe in an afterlife, "
    "but I'm bringing a change of underwear "
    "just in case.\n"
    "You never know — eternity might have a dress code."
)

WOODY_GLASSES = r"""
      .--.      .--.
     /    \    /    \
    |  __  |  |  __  |
    | |  | |  | |  | |
    | |__| |  | |__| |
     \____/    \____/
"""

THOUGHT_BUBBLE = r"""
        .--.
       /    \
      |  :)  |
       \    /
        '--'
         \
          \
           \
            \
             \
              \
               \
                \
"""

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=C.WHITE, delay=0.03, newline=True):
    for char in text:
        print(f"{color}{char}{C.R}", end='', flush=True)
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def blink_text(text, color=C.YELLOW, times=3, interval=0.4):
    for _ in range(times):
        print(f"\r{color}{text}{C.R}", end='', flush=True)
        time.sleep(interval)
        print(f"\r{' ' * len(text)}", end='', flush=True)
        time.sleep(interval)
    print(f"\r{color}{text}{C.R}")

def draw_box(content_lines, border_color=C.CYAN, title="", title_color=C.BRIGHT_YELLOW):
    max_len = max(len(line) for line in content_lines)
    if title:
        max_len = max(max_len, len(title) + 4)
    
    top = f"{border_color}╔{'═' * (max_len + 2)}╗{C.R}"
    bottom = f"{border_color}╚{'═' * (max_len + 2)}╝{C.R}"
    
    lines = [top]
    
    if title:
        title_line = f"{border_color}║{C.R} {title_color}{title.center(max_len)}{C.R} {border_color}║{C.R}"
        lines.append(title_line)
        lines.append(f"{border_color}╠{'═' * (max_len + 2)}╣{C.R}")
    
    for line in content_lines:
        padded = line.ljust(max_len)
        lines.append(f"{border_color}║{C.R} {padded} {border_color}║{C.R}")
    
    lines.append(bottom)
    return '\n'.join(lines)

def neurotic_loading():
    thoughts = [
        "Analyzing mortality...",
        "Checking if stove is off...",
        "Replaying awkward moment from 2003...",
        "Wondering if God charges roaming fees...",
        "Calculating probability of existential dread...",
        "Verifying underwear packing protocol...",
    ]
    for thought in thoughts:
        print(f"\r{C.DIM}[{C.BRIGHT_CYAN}...{C.DIM}] {C.YELLOW}{thought}{C.R}", end='', flush=True)
        time.sleep(random.uniform(0.3, 0.6))
    print(f"\r{C.DIM}[{C.BRIGHT_GREEN}OK{C.DIM}] {C.GREEN}Neurosis calibrated successfully.{C.R}")
    time.sleep(0.5)

def main():
    hide_cursor()
    try:
        clear_screen()
        
        # Intro animation
        print(f"{C.BRIGHT_MAGENTA}{C.BOLD}")
        print("  ╔══════════════════════════════════════════════════════════════╗")
        print("  ║                                                            ║")
        print("  ║    A WOODY ALLEN MOMENT OF EXISTENTIAL PANIC™             ║")
        print("  ║                                                            ║")
        print("  ╚══════════════════════════════════════════════════════════════╝")
        print(f"{C.R}")
        time.sleep(0.8)
        
        # Glasses ASCII
        print(f"{C.CYAN}{WOODY_GLASSES}{C.R}")
        time.sleep(0.5)
        
        # Neurotic loading
        print()
        neurotic_loading()
        print()
        
        # The quote in a fancy box
        quote_lines = WOODY_QUOTE.split('\n')
        box = draw_box(
            quote_lines,
            border_color=C.BRIGHT_BLUE,
            title=" ★ PHILOSOPHICAL ANXIETY ★ ",
            title_color=C.BRIGHT_YELLOW + C.BOLD
        )
        print(box)
        print()
        
        # Typewriter effect for the quote
        print(f"{C.BOLD}{C.BRIGHT_WHITE}  Internal monologue:{C.R}")
        print()
        for i, line in enumerate(quote_lines):
            if i == 0:
                typewriter(f"  {line}", color=C.BRIGHT_CYAN, delay=0.04)
            else:
                typewriter(f"  {line}", color=C.BRIGHT_YELLOW, delay=0.05)
        print()
        
        # Thought bubble with neurotic afterthoughts
        afterthoughts = [
            "Wait — is 'eternity' business casual?",
            "What if they only have white? I look terrible in white.",
            "Should I pack socks? Eternal feet get cold.",
            "Does the afterlife have dry cleaning?",
            "My mother would say: 'You're worried about underwear? What about your SOUL?'",
            "She's right. My soul definitely needs ironing.",
        ]
        
        print(f"{C.DIM}  {THOUGHT_BUBBLE}{C.R}")
        for thought in afterthoughts:
            print(f"  {C.DIM}{thought}{C.R}")
            time.sleep(0.25)
        
        print()
        # Final sign-off
        signoff = "— Your neurotic narrator, signing off to check the stove for the 47th time"
        blink_text(f"  {signoff}", color=C.BRIGHT_MAGENTA, times=2)
        print()
        print(f"  {C.DIM}Press Ctrl+C to exist... or don't. The universe is indifferent either way.{C.R}")
        
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        print(f"\n{C.R}")

if __name__ == "__main__":
    main()