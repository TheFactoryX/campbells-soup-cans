"""
Campbell's Soup Can #2886
Produced: 2026-03-21 13:12:03
Worker: Xiaomi: MiMo-V2-Omni (xiaomi/mimo-v2-omni)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def woody_quote():
    quote = """I'm not afraid of death; I just don't want to be there when it happens.
    Also, I'm not crazy about the commuting and the paperwork involved."""
    
    # Create a colorful border
    border_top = "╔" + "═" * 70 + "╗"
    border_bottom = "╚" + "═" * 70 + "╝"
    side_border = "║"
    
    # ANSI color codes
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLINK = "\033[5m"
    
    # Clear screen for dramatic effect
    clear_screen()
    
    # Title with blinking effect
    print(f"\n{BOLD}{RED}✧✧✧ WOODY ALLEN PHILOSOPHICAL WISDOM ✧✧✧{RESET}\n")
    
    # Animated border reveal
    for i in range(1, 3):
        print(f"{BORDER_COLOR}{border_top}{RESET}" if i == 1 else "", end="")
        time.sleep(0.1)
    
    print(f"{CYAN}{side_border}{RESET}{'':^70}{CYAN}{side_border}{RESET}")
    
    # Quote with word-by-word color animation
    words = quote.split()
    current_line = ""
    
    for word in words:
        # Randomly assign colors to words
        colors = [RED, YELLOW, GREEN, MAGENTA, CYAN]
        word_color = colors[len(word) % len(colors)]
        
        # Check line length
        if len(current_line) + len(word) + 1 <= 68:
            current_line += f"{word_color}{word}{RESET} "
        else:
            print(f"{CYAN}{side_border}{RESET} {current_line:^68} {CYAN}{side_border}{RESET}")
            current_line = f"{word_color}{word}{RESET} "
            time.sleep(0.05)  # Typewriter effect
    
    # Print last line
    if current_line:
        print(f"{CYAN}{side_border}{RESET} {current_line:^68} {CYAN}{side_border}{RESET}")
    
    # Empty lines
    print(f"{CYAN}{side_border}{RESET}{'':^70}{CYAN}{side_border}{RESET}")
    
    # Signature with animation
    signature = "— Woody Allen (probably)"
    for char in signature:
        print(f"{MAGENTA}{char}{RESET}", end="", flush=True)
        time.sleep(0.05)
    print(f"{CYAN}{side_border}{RESET}{'':^(70-len(signature))}{CYAN}{side_border}{RESET}")
    
    # Bottom border
    print(f"{BORDER_COLOR}{border_bottom}{RESET}")
    
    # Final dramatic pause
    print(f"\n{YELLOW}{BLINK}[Existential crisis loading...]{RESET}")
    time.sleep(2)
    clear_screen()
    
    # ASCII art version
    print(f"""
{GREEN}              .---.
             /     \\
            ( {RED}WOODY{GREEN} )
             `-----'
    {YELLOW}  "I don't fear death,
    {YELLOW}   I just don't want
    {YELLOW}   to be there when
    {YELLOW}   it happens."
    {MAGENTA}   (The paperwork
    {MAGENTA}    alone is 
    {MAGENTA}    overwhelming)
    {RESET}""")

if __name__ == "__main__":
    try:
        woody_quote()
    except KeyboardInterrupt:
        print(f"\n{RED}Even escaping this program is fraught with existential dread.{RESET}")