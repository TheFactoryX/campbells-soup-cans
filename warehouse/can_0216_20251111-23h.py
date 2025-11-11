"""
Campbell's Soup Can #216
Produced: 2025-11-11 23:29:22
Worker: Meituan: LongCat Flash Chat (free) (meituan/longcat-flash-chat:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import time
import sys
import itertools

# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RED = '\033[91m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'
INVERT = '\033[7m'
DIM = '\033[2m'

# Create a frame counter for animation
frames = 0
dots = itertools.cycle(['   ', '.  ', '.. ', '...'])

def clear_screen():
    # ANSI escape to clear screen and move cursor to home
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def print_ascii_eye():
    eye = rf"""
{GREEN}        _______{RESET}  
{GREEN}       /       \{RESET} 
{GREEN}      |  {YELLOW}o   o  {GREEN}|{RESET}
{GREEN}      |   {RED}vvv   {GREEN}|{RESET}
{GREEN}       \  {CYAN}X X  {GREEN}/{RESET} 
{GREEN}        \_____{RESET}  
{GREEN}         |   |{RESET}  
{GREEN}         U   U{RESET}  
    """
    print(eye)

def animate_quote():
    global frames
    dot_text = next(dots)
    frames += 1
    
    quote = (f"\"I used to think the whole universe {RED}depended{BLUE} on me...{RESET} \n"
            f"then I realized it was just my {PURPLE}dysfunction{RESET} creating {YELLOW}entropy{RESET} \n"
            f"for {INVERT}someone else{RESET}'s {DIM}convenience{RESET}.{dot_text}\"")
    
    # Create a fancy border
    border = f"{BOLD}{BLUE}" + "═" * 60 + f"{RESET}"
    
    # Clear and redraw
    clear_screen()
    
    # Print header
    print(f"{BOLD}{CYAN}┌{'─' * 58}┐{RESET}")
    print(f"{BOLD}{CYAN}│{RESET}{GREEN} <WOODY PHILOSOPHY MODE ENGAGED>{' ' * (50 - len(' <WOODY PHILOSOPHY MODE ENGAGED>'))}{CYAN} │{RESET}")
    print(f"{BOLD}{CYAN}├{'─' * 58}┤{RESET}")
    
    # ASCII eye art
    eye_lines = [
        rf"{CYAN}│{RESET} {GREEN}        _______{RESET}                                                               {CYAN}│{RESET}",
        rf"{CYAN}│{RESET} {GREEN}       /       \{RESET}                                                              {CYAN}│{RESET}",
        rf"{CYAN}│{RESET} {GREEN}      |  {YELLOW}o   o  {GREEN}|{RESET}                                                             {CYAN}│{RESET}",
        rf"{CYAN}│{RESET} {GREEN}      |   {RED}vvv   {GREEN}|{RESET}                                                             {CYAN}│{RESET}",
        rf"{CYAN}│{RESET} {GREEN}       \  {CYAN}X X  {GREEN}/{RESET}                                                             {CYAN}│{RESET}",
        rf"{CYAN}│{RESET} {GREEN}        \_____{RESET}                                                               {CYAN}│{RESET}",
        rf"{CYAN}│{RESET} {GREEN}         |   |{RESET}                  {BOLD}{YELLOW}WOODY ALLEN SAYS:{RESET}                              {CYAN}│{RESET}",
        rf"{CYAN}│{RESET} {GREEN}         U   U{RESET}                 {'_'*37:^37}        {CYAN}│{RESET}"
    ]
    
    for line in eye_lines:
        print(line)
    
    # Quote box
    print(f"{CYAN}│{RESET} {BOLD}{BLUE}{' '*36} {RED}'{RESET}{' '*20}{CYAN}│{RESET}")
    
    # Print quote line by line
    for i, line in enumerate(quote.split('\n')[:-1]):
        centered_line = line.center(58)
        print(f"{CYAN}│{RESET}{centered_line}{CYAN}│{RESET}")
    
    # The closing dots with emphasis
    final_dot = dot_text
    if frames % 4 == 0:
        final_dot = f"{PURPLE}{dot_text}{RESET}"
    
    closing = f"\"{final_dot}{RESET}"
    print(f"{CYAN}│{RESET}{closing:>58}{CYAN}│{RESET}")
    print(f"{CYAN}│{RESET} {' '*58}{CYAN}│{RESET}")
    
    # Attribution with a twist
    attribution = f"{RED}— Woody Allen (probably),{RESET} if he weren't {DIM}too neurotic{GREEN} to write it down{RESET}"
    print(f"{CYAN}│{RESET}{attribution:^58}{CYAN}│{RESET}")
    print(f"{BOLD}{CYAN}└{'─' * 58}┘{RESET}")
    
    # Philosophical disclaimer scrolling text at bottom
    disclaimers = [
        "WARNING: Existential dread may cause sudden urge to see a therapist",
        "Side effects: Temporary anxiety, mild paranoia, improved humor tolerance",
        "Philosophical content provided is 63% neurosis, 37% pasta byproducts",
        "Not intended to replace professional help. Or wine. Mostly wine."
    ]
    
    scroll_pos = frames % (len(disclaimers) * 10) // 10
    disclaimer = disclaimers[scroll_pos]
    colored_disclaimer = "".join([
        f"{CYAN}{c}" if i % 4 == 0 else
        f"{YELLOW}{c}" if i % 4 == 1 else
        f"{GREEN}{c}" if i % 4 == 2 else
        f"{PURPLE}{c}"
        for i, c in enumerate(disclaimer)
    ])
    print(f"{DIM}{colored_disclaimer}{RESET}")
    
    sys.stdout.flush()

def main():
    # Initial pause for dramatic effect
    print(f"{BOLD}{PURPLE}Initializing Woody Mode...{RESET}", end='', flush=True)
    time.sleep(1.5)
    for _ in range(3):
        print(f"{YELLOW}.{RESET}", end='', flush=True)
        time.sleep(0.8)
    print()
    time.sleep(1)
    
    # Animate the quote for a little while
    try:
        for _ in range(24):  # ~10 seconds at 0.4s intervals
            animate_quote()
            time.sleep(0.4)
        
        # Final static frame with a wink
        clear_screen()
        animate_quote()
        # Replace the eye with a winky version
        time.sleep(1)
        clear_screen()
        final_eye = rf"""
{GREEN}        _______{RESET}  
{GREEN}       /       \{RESET} 
{GREEN}      |  {YELLOW}o   ⌐   {GREEN}|{RESET}
{GREEN}      |   {RED}vvv   {GREEN}|{RESET}
{GREEN}       \  {CYAN}X X  {GREEN}/{RESET} 
{GREEN}        \_____{RESET}  
{GREEN}         |   |{RESET}  
{GREEN}         U   U{RESET}  
    """
        # Recreate the final frame but with winky eye
        border = f"{BOLD}{BLUE}" + "═" * 60 + f"{RESET}"
        print(f"{BOLD}{CYAN}┌{'─' * 58}┐{RESET}")
        print(f"{BOLD}{CYAN}│{RESET}{GREEN} <WOODY PHILOSOPHY MODE COMPLETE>{' ' * (49 - len(' <WOODY PHILOSOPHY MODE COMPLETE>'))}{CYAN} │{RESET}")
        print(f"{BOLD}{CYAN}├{'─' * 58}┤{RESET}")
        print(final_eye.split('\n')[1])
        print(final_eye.split('\n')[2])
        print(final_eye.split('\n')[3])
        print(final_eye.split('\n')[4])
        print(final_eye.split('\n')[5])
        print(final_eye.split('\n')[6])
        print(final_eye.split('\n')[7])
        print(f"{CYAN}│{RESET} {BOLD}{YELLOW}WOODY ALLEN SAYS:{RESET} {'_'*37:^37}        {CYAN}│{RESET}")
        print(f"{CYAN}│{RESET} {BOLD}{BLUE}{' '*36} {RED}'{RESET}{' '*20}{CYAN}│{RESET}")
        print(f"{CYAN}│{RESET} \"I used to think the whole universe {RED}depended{BLUE} on me...{RESET}                {CYAN}│{RESET}")
        print(f"{CYAN}│{RESET} then I realized it was just my {PURPLE}dysfunction{RESET} creating {YELLOW}entropy{RESET}  {CYAN}│{RESET}")
        print(f"{CYAN}│{RESET} for {INVERT}someone else{RESET}'s {DIM}convenience{RESET}...\"                               {CYAN}│{RESET}")
        print(f"{CYAN}│{RESET} {' '*58}{CYAN}│{RESET}")
        attribution = f"{RED}— Woody Allen (probably),{RESET} if he weren't {DIM}too neurotic{GREEN} to write it down{RESET}"
        print(f"{CYAN}│{RESET}{attribution:^58}{CYAN}│{RESET}")
        print(f"{BOLD}{CYAN}└{'─' * 58}┘{RESET}")
        print(f"{DIM}{colored_disclaimer}{RESET}")
        print(f"\n{BOLD}{GREEN}>> Reality not found. You are already dreaming. Have some wine. <<{RESET}")
        
        time.sleep(2.5)
        print(f"\n{DIM}Program exiting. Your therapy session is over. Pay up.{RESET}")
        
    except KeyboardInterrupt:
        print(f"\n\n{PURPLE}Exited mid-torpor. Typical.{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()