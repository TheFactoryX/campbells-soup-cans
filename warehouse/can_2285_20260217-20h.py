"""
Campbell's Soup Can #2285
Produced: 2026-02-17 20:56:35
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

def clear_screen():
    """Clear the terminal screen."""
    print("\033[2J\033[H", end="")

def neurotic_writer(text, color=WHITE, delay=0.03, anxiety=True):
    """Print text with Woody Allen's signature neurotic typing style."""
    for char in text:
        if anxiety and random.random() < 0.1:  # 10% chance of anxious pause
            time.sleep(0.2)
        print(f"{color}{char}{RESET}", end="", flush=True)
        time.sleep(delay + random.uniform(-0.01, 0.01))
    print()

def philosophical_fortune_cookie():
    """Generate a Woody Allen-style philosophical quote with dramatic presentation."""
    clear_screen()
    
    # The quote - written in Woody's voice
    quote = (
        "I don't want to achieve immortality through my work. "
        "I want to achieve it through not dying. "
        "But since that seems increasingly unlikely, "
        "I'll settle for being slightly less mortal than yesterday. "
        "Which, given my track record, is about as likely as "
        "a cockroach winning the Pulitzer for poetry."
    )
    
    # Build the "cosmic" frame
    width = min(80, len(quote) + 10)
    border = "·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇·̇\n"
    
    # Dramatic intro with shaking effect
    intro_lines = [
        f"{BOLD}{CYAN}⋆.ೃ࿔*:･ﾟ✧⋆.ೃ࿔*:･ﾟ✧⋆.ೃ࿔*:･ﾟ✧{RESET}",
        f"  {YELLOW}⊹  THE DEEP THOUGHTS OF A NEUROTIC COSMIC OBSERVER  ⊹{RESET}",
        f"{BOLD}{CYAN}⋆.ೃ࿔*:･ﾟ✧⋆.ೃ࿔*:･ﾟ✧⋆.ೃ࿔*:･ﾟ✧{RESET}",
        ""
    ]
    
    for line in intro_lines:
        neurotic_writer(line, delay=0.05, anxiety=False)
        time.sleep(0.3)
    
    time.sleep(1)
    
    # Build the quote box with alternating border colors
    print(f"{MAGENTA}╭{'─' * (width-2)}╮{RESET}")
    
    # Print the quote with auto-wrapping and dramatic pauses at punctuation
    words = quote.split()
    line = ""
    for word in words:
        if len(line + word) + 1 > width - 4:
            # Center the line with punctuation sensitivity
            padding = (width - len(line) - 4) // 2
            line_content = " " * padding + line.strip()
            
            # Add anxiety punctuation pauses
            if line_content[-1] in ".!?;":
                neurotic_writer(f"│ {line_content.ljust(width-4)} │{RESET}", 
                              color=GREEN if random.random() > 0.5 else YELLOW, 
                              delay=0.02)
                time.sleep(0.15)
            else:
                neurotic_writer(f"│ {line_content.ljust(width-4)} │{RESET}", 
                              color=WHITE, 
                              delay=0.015)
            line = word + " "
        else:
            line += word + " "
    
    # Last line
    if line:
        padding = (width - len(line) - 4) // 2
        line_content = " " * padding + line.strip()
        neurotic_writer(f"│ {line_content.ljust(width-4)} │{RESET}", 
                      color=WHITE, 
                      delay=0.015)
    
    time.sleep(0.5)
    
    # Dramatic bottom border with twinkling effect
    for _ in range(3):
        for color in [RED, YELLOW, GREEN, CYAN, MAGENTA, BLUE]:
            print(f"{color}╰{'─' * (width-2)}╯{RESET}", end="\r")
            time.sleep(0.1)
    print(f"{BOLD}{WHITE}╰{'─' * (width-2)}╯{RESET}")
    
    time.sleep(0.8)
    
    # The signature with existential shrug
    neurotic_writer(f"\n{BOLD}{BLUE}[typed in a moment of existential clarity, probably]{RESET}", 
                    delay=0.04)
    
    # Final dramatic pause
    time.sleep(1)
    neurotic_writer(f"\n{RED}•̮̮̖̗̖̗̖̗̖̗̖̗̖̗̖̗̖̗̖̗̖̗̖̗̖̗̃̊̃̑᷄{RESET}\n", 
                    delay=0.001)

if __name__ == "__main__":
    try:
        philosophical_fortune_cookie()
    except KeyboardInterrupt:
        print(f"\n{RED}[interrupted - the universe remains indifferent]{RESET}")
    finally:
        print(RESET, end="")