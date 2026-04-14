"""
Campbell's Soup Can #3284
Produced: 2026-04-14 11:19:48
Worker: TheDrummer: Cydonia 24B V4.1 (thedrummer/cydonia-24b-v4.1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

def spin_animation():
    spinner = "|/-\\"
    for i in range(10):
        sys.stdout.write(f"\r{ITALIC}{MAGENTA}Thinking about existential dread...{spinner[i % 4]}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\r{' ' * 50}\r")
    sys.stdout.flush()

def display_frame(message, color, delay=0.05):
    lines = ["", "", "", "", ""]
    
    # Top border
    lines[0] = "┌" + "─" * (len(message) + 2) + "┐"
    
    # Side borders
    for i in range(1, 4):
        lines[i] = f"│{color} {message}{RESET} │"
    
    # Bottom border
    lines[4] = "└" + "─" * (len(message) + 2) + "┘"
    
    for line in lines:
        print(line)
        time.sleep(delay)
    print()

def display_woody_quote():
    # Think deeply about the meaninglessness of it all
    woody_quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "I don't deserve a prize for not strangling my neighbor, I didn't do it out of virtue, I just abhor sweat and too much physical exertion.",
        "The world is divided into victimizers and victims; I'm just waiting to be a victimizer the right way."
    ]
    
    quote = random.choice(woody_quotes)
    spin_animation()
    
    # Display with dramatic flair
    print(f"{BOLD}{YELLOW}{'=' * 70}{RESET}")
    print(f"{ITALIC}{UNDERLINE}WOODY ALLEN'S PROFOUND WISDOM:{RESET}")
    print(f"{BOLD}{YELLOW}{'=' * 70}{RESET}")
    
    # Colorful character-by-character display
    for char in quote:
        colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]
        print(f"{random.choice(colors)}{char}{RESET}", end='')
        time.sleep(0.03)
    
    print(f"\n\n{BOLD}{ITALIC}{UNDERLINE}...and now back to your regularly scheduled existential crisis.{RESET}")

def display_ascii_woody():
    woody = f"""
{RESET}
    {RED}@.{RESET}   {YELLOW}@                        {BLUE}@@.{RESET}
   {RED}@@.{RESET}  {YELLOW}@{RESET}                      {BLUE}@{RESET}
    {RED}@{RESET}  {YELLOW}@@{RESET}    {GREEN}@@.{RESET}   {BLUE}@{RESET}
            {YELLOW}@{RESET}        {GREEN}@{RESET}
           {RESET}{YELLOW}@{RESET}      {GREEN}@{RESET}
          {YELLOW}@{RESET}         {GREEN}@{RESET}    {CYAN}@@.{RESET}
         {BLUE}@{RESET}           {GREEN}@{RESET}  {CYAN}@{RESET}@{RESET}
        {BLUE}@{RESET}             {CYAN}@{RESET}@{RESET}@{RESET}
       {BLUE}@{RESET}                {CYAN}@{RESET}@{RESET}@{RESET}
      {BLUE}@{RESET}                       @{RESET}
{RESET}    {MAGENTA}@{RESET}                          {BLUE}@{RESET}
  {MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}                {MAGENTA}@{RESET}
{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}        {MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}
{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}        {MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}
  {MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}                    {MAGENTA}@{RESET}@{MAGENTA}@{RESET}@{MAGENTA}@{RESET}
    {MAGENTA}@{RESET}                          {MAGENTA}@{RESET}
{RESET}"""
    print(woody)

if __name__ == "__main__":
    display_frame("WOODY ALLEN WISDOM GENERATOR", CYAN)
    display_ascii_woody()
    
    display_woody_quote()
    
    print(f"{BOLD}{YELLOW}{'=' * 70}{RESET}")
    print(f"{BOLD}{ITALIC}{MAGENTA}Try again for a different existential crisis!{RESET}{RESET}")
    print(f"{YELLOW}{'=' * 70}{RESET}")