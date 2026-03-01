"""
Campbell's Soup Can #2514
Produced: 2026-03-01 23:37:20
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# Woody Allen's Existential Anxiety with ANSI Art

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def blink(text, color):
    """Blinking text effect with ANSI codes"""
    blink_on = f"{color}{text}{RESET}"
    return blink_on + f"{color}{text}{RESET}"

def woody_quote():
    return f"{YELLOW}The only thing that's constant is change... and my alarm clock buzzing at 4 AM{RESET}"

def woody_joke():
    return f"{BLUE}My psychiatrist says I'm neurotic... I've asked her how long that takes{RESET}"

def artistic_center(text, color):
    """Center text with padding and color"""
    pad = " " * 30
    centered = pad + text.center(80)
    return f"{color}{centered}{RESET}"

def main():
    # ANSI art borders
    top_border = artistic_center(" Woody Allen's Existential Angst ", MAGENTA)
    
    # Let's start with a blank screen
    artistic_center("Loading Woody Allen's mental health...", GREEN)
    
    import time
    import random
    
    quotes = [
        artistic_center("I'm not afraid of death. I just don't want to be there when it happens", RED),
        artistic_center("Life is a series of confirming that death is the only certainty", YELLOW),
        artistic_center("The trouble with having no philosophy is that you have nothing to complain about", BLUE),
        artistic_center("I don't want to achieve immortality through my work... I want it through a really good will", CYAN),
        artistic_center("I'm afraid of dying. It could be a mistake", WHITE)
    ]
    
    # Animation loop
    for _ in range(3):
        artistic_center(" * ... * ", GREEN)
        time.sleep(0.8)
        
        # Random quote
        art_quote = random.choice(quotes)
        
        # Blink effect
        print(blink(art_quote, RED))
        time.sleep(1.2)
        
        # Woody's witty self
        print(artistic_center("Woody Allen", BLUE) + 
              artistic_center(" is" if random.random() < 0.5 else " ain't", WHITE) +
              artistic_center("your favorite existential comedian" if random.random() < 0.7 else " serious philosopher", MAGENTA))
        time.sleep(1.5)
    
    # Final thought
    print(artistic_center("Remember:", RED))
    print(artistic_center(f"  {blink('Everything is meaningless... except this line', MAGENTA)}", BLUE))
    print(top_border)

if __name__ == "__main__":
    main()