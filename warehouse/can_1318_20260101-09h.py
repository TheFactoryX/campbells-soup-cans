"""
Campbell's Soup Can #1318
Produced: 2026-01-01 09:38:05
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import random

# Woody Allen style philosophical quote
QUOTE = (
    "I'm not afraid of death. "
    "I'm afraid of the parts where I'm still alive but I'm checking my emails."
)

# ANSI Colors
class T:
    """ANSI color constants"""
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    REVERSE = "\033[7m"
    ITALIC = "\033[3m"

# Cursor control
def hide_cursor():
    sys.stdout.write("\033[?25l")

def show_cursor():
    sys.stdout.write("\033[?25h")

def clear_screen():
    sys.stdout.write("\033[2J\033[H")

def move_to(x, y):
    sys.stdout.write(f"\033[{y};{x}H")

def print_centered(text, y, width=80):
    x = (width - len(text)) // 2 + 1
    move_to(x, y)
    sys.stdout.write(text)

def scroll_text(lines, speed=0.04):
    """Simulates old terminal scrolling"""
    height = 24
    for i, line in enumerate(lines):
        if i < height:
            move_to(1, i + 1)
        else:
            # Scroll up by printing newlines
            sys.stdout.write("\n")
        sys.stdout.write(line)
        sys.stdout.flush()
        time.sleep(speed)

def draw_progress_bar(width=40, steps=20, label="Life Progress"):
    """Draws a neurotic life progress bar"""
    bar = ""
    for i in range(steps):
        progress = (i + 1) / steps
        filled = int(width * progress)
        # The bar gets more anxious as it progresses
        if progress < 0.3:
            char = "."
            color = T.YELLOW
        elif progress < 0.6:
            char = "o"
            color = T.BLUE
        else:
            char = "!"
            color = T.RED
        
        bar = f"{color}{'█' * filled}{T.RESET}{'.' * (width - filled)}{T.RESET}"
        move_to(1, 12)
        sys.stdout.write(f"  {T.CYAN}{label}:{T.RESET} [{bar}] {int(progress*100)}%")
        sys.stdout.flush()
        time.sleep(0.15 + random.random() * 0.1)

def draw_ascii_art():
    """Draws a neurotic stick figure (Woody Allen style)"""
    art = [
        f"{T.BOLD}{T.YELLOW}    _                   _   _            _       {T.RESET}",
        f"{T.YELLOW}   / \\   _ __ _ __ ___ | |_| |__   ___  | | __   {T.RESET}",
        f"{T.YELLOW}  / _ \\ | '__| '_ ` _ \\| __| '_ \\ / _ \\ | |/ /   {T.RESET}",
        f"{T.YELLOW} / ___ \\| |  | | | | | | |_| | | |  __/ |   <    {T.RESET}",
        f"{T.YELLOW}/_/   \\_\\_|  |_| |_| |_|\\__|_| |_|\\___| |_|\\_\\   {T.RESET}",
        f"                                                 ",
        f"       {T.MAGENTA}\\\\         {T.RED}o          {T.MAGENTA}///{T.RESET}          ",
        f"        {T.MAGENTA}\\\\       /|\\         {T.MAGENTA}///{T.RESET}          ",
        f"         {T.MAGENTA}\\\\      / \\         {T.MAGENTA}///{T.RESET}          ",
        f"          {T.MAGENTA}\\\\     {T.CYAN}ANXIETY{T.MAGENTA}     {T.MAGENTA}///{T.RESET}          ",
    ]
    for i, line in enumerate(art):
        move_to(10, 4 + i)
        sys.stdout.write(line)

def glitch_effect(text, times=3):
    """Creates a glitching effect for the quote"""
    chars = list(text)
    for _ in range(times):
        # Randomly scramble some characters
        glitched = chars[:]
        indices = random.sample(range(len(chars)), min(5, len(chars)))
        for idx in indices:
            glitched[idx] = random.choice("!@#$%^&*<>?/")
        
        move_to(1, 18)
        sys.stdout.write(" " * 80)
        move_to(1, 18)
        sys.stdout.write(f"{T.REVERSE}{''.join(glitched)}{T.RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Restore
    move_to(1, 18)
    sys.stdout.write(" " * 80)
    move_to(1, 18)
    sys.stdout.write(f"{T.BOLD}{T.CYAN}{text}{T.RESET}")

def nervous_tick():
    """Visual representation of nervous ticks"""
    tick_marks = ["|", "/", "-", "\\", "|", "/", "-", "\\"]
    return random.choice(tick_marks)

def main():
    try:
        hide_cursor()
        clear_screen()
        
        # Title header
        print_centered(f"{T.REVERSE}{T.YELLOW}NEUROTIC PHILOSOPHY v1.0{T.RESET}", 1, 80)
        time.sleep(0.5)
        
        # Draw the ASCII art
        draw_ascii_art()
        time.sleep(1)
        
        # The Overthinker's Progress
        move_to(1, 15)
        sys.stdout.write(f"{T.MAGENTA}Loading existential dread...{T.RESET}")
        sys.stdout.flush()
        
        # Animate dots
        for _ in range(3):
            time.sleep(0.3)
            sys.stdout.write(".")
            sys.stdout.flush()
        
        # Neural activity bar
        draw_progress_bar(label="Neural Anxiety")
        
        # Visual "brain" scanning effect
        move_to(1, 16)
        sys.stdout.write(f"{T.CYAN}Scanning subconscious for meaning.{T.RESET}")
        time.sleep(0.5)
        
        # Typewriter effect for the quote
        move_to(1, 18)
        quote_prefix = f"{T.RED}WOODY:{T.RESET} "
        sys.stdout.write(quote_prefix)
        sys.stdout.flush()
        
        typed_text = ""
        for char in QUOTE:
            typed_text += char
            sys.stdout.write(f"{T.BOLD}{T.CYAN}{char}{T.RESET}")
            sys.stdout.flush()
            
            # Random nervous ticks
            if random.random() < 0.15:
                old_pos = sys.stdout.tell()
                move_to(75, 18)
                sys.stdout.write(nervous_tick())
                move_to(1, 19)
                sys.stdout.flush()
            
            time.sleep(0.03 + random.random() * 0.02)
        
        # Glitch effect (digital anxiety)
        time.sleep(0.5)
        glitch_effect(QUOTE)
        
        # Signature
        time.sleep(1)
        move_to(1, 21)
        sys.stdout.write(f"{T.YELLOW}{'─' * 60}{T.RESET}")
        move_to(1, 22)
        sys.stdout.write(f"{T.ITALIC}  'Time is nature's way of keeping everything from happening at once.'{T.RESET}")
        move_to(1, 23)
        sys.stdout.write(f"  {T.MAGENTA}- (Or something like that){T.RESET}")
        
        # Exit animation
        time.sleep(1.5)
        for i in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.5)
        
        move_to(1, 25)
        
    except KeyboardInterrupt:
        # Graceful interruption
        show_cursor()
        clear_screen()
        print("Left the conversation early. That's very Woody Allen of you.")
        sys.exit(0)
    finally:
        show_cursor()

if __name__ == "__main__":
    # Run it
    main()