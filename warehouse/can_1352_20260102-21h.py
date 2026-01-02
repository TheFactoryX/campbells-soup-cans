"""
Campbell's Soup Can #1352
Produced: 2026-01-02 21:27:41
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def woody_allen_quote():
    # A collection of neurotic, existential, and self-deprecating quotes in the style of Woody Allen
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering – and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "My brain is my second favorite organ.",
        "I took a speed reading course and read War and Peace in twenty minutes. It involves Russia.",
        "Basically my wife was immature. I'd be at home in the bathtub and she'd come in and sink my boats.",
        "It's not that I'm afraid to die, I just don't want to be around when it happens.",
        "I have a very low threshold of death. My doctor told me I have the body of a twenty-year-old, but I keep it in the fridge."
    ]
    
    # ANSI color codes for a "theater" feel
    RED = "\033[91m"
    YELLOW = "\033[93m"
    WHITE = "\033[97m"
    DIM = "\033[2m"
    BRIGHT = "\033[1m"
    BLINK = "\033[5m"
    RESET = "\033[0m"
    INVERT = "\033[7m"
    
    # Select a random quote
    quote = random.choice(quotes)
    
    # Pre-calculated visual elements
    width = 78
    border = f"{YELLOW}+{RESET}"
    horizontal_line = f"{YELLOW}-{RESET}"
    v_bar = f"{RED}|{RESET}"
    
    # Clear screen (works on most terminals)
    print("\033[2J", end="") 
    
    # --- ASCII ART: The Neurotic Thinker ---
    art = [
        f"{RED}    o            o    {RESET}   {YELLOW}Philosophy Checkpoint{RESET}",
        f"{RED}    |            |    {RESET}   {DIM}Proceed with existential dread?{RESET}",
        f"{RED}   / \\          / \\   {RESET}",
        f"{RED}  | H |        | H |  {RESET}   {BLINK}[ WAITING FOR INPUT ]{RESET}",
        f"{RED}   \\_/          \\_/   {RESET}",
        f"{RED}    |            |    {RESET}",
        f"{RED}   / \\          / \\   {RESET}"
    ]
    
    # --- 1. The Setup (Typewriter Effect) ---
    def typewriter(text, speed=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(random.uniform(speed/2, speed*1.5))
        print()

    print("\n" * 2)
    
    # Draw the intro banner
    print(f"{INVERT}{' ' * 40}{' ' * 38}{RESET}")
    print(f"{INVERT}{YELLOW.center(40)}{RESET}{INVERT}{WHITE.center(38)}{RESET}")
    print(f"{INVERT}{BRIGHT}  W O O D Y   A L L E N   S I M U L A T O R   2024  {RESET}{INVERT}{' ' * 27}{RESET}")
    
    # Draw the ASCII Art with a little dramatic pause
    for line in art:
        print(line)
        time.sleep(0.2)
        
    print(f"{INVERT}{' ' * 78}{RESET}\n")

    # --- 2. The Quote Display (The "Card" Effect) ---
    
    # Calculate padding to center the quote
    total_width = width - 4  # Space for borders and margins
    
    # Word wrap logic manually to fit inside the box
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(" ".join(current_line + [word])) <= total_width:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
        
    # Determine the longest line to center the whole quote box
    max_line_len = max(len(l) for l in lines) if lines else 1
    box_width = max_line_len + 4
    
    # Draw the Top Border
    top_border = f"{YELLOW}┌{'─' * (box_width - 2)}┐{RESET}"
    bottom_border = f"{YELLOW}└{'─' * (box_width - 2)}┘{RESET}"
    
    print(" " * ((78 - box_width) // 2) + top_border)
    
    # Draw the Quote (with slow typing animation)
    for line in lines:
        left_pad = " " * ((78 - box_width) // 2)
        padding_spaces = " " * (box_width - 4 - len(line))
        
        # Typewriter effect for the line
        sys.stdout.write(f"{left_pad}{v_bar} {RESET}")
        sys.stdout.flush()
        
        # Randomize typing speed slightly for human feel
        for char in line:
            sys.stdout.write(f"{WHITE}{BRIGHT}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(random.uniform(0.02, 0.06))
            
        sys.stdout.write(f" {RED}|{RESET}\n")
        
    print(" " * ((78 - box_width) // 2) + bottom_border)
    
    # --- 3. The Outro (The "Fade Out") ---
    print()
    time.sleep(1)
    
    msg = f"{DIM}Press Ctrl+C to stop overthinking... or just sit here in silence.{RESET}"
    print(" " * ((78 - len(msg) + 20) // 2) + msg)
    
    # Animate blinking cursor at the end
    try:
        for _ in range(5):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.5)
        print("\n")
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    woody_allen_quote()