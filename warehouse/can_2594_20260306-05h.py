"""
Campbell's Soup Can #2594
Produced: 2026-03-06 05:59:39
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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
from itertools import cycle

# Woody Allen's neurotic existential wisdom
quote = "I'm not afraid of death; I just don't want to be there when it happens."

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
GRAY = "\033[90m"

# Create a simple animation of existential dread
def existential_dread_animation():
    dread_messages = [
        f"{YELLOW}⏳ Time passes...{RESET}",
        f"{MAGENTA}🤔 What does it all mean?{RESET}",
        f"{CYAN}🌀 The universe expands...{RESET}",
        f"{RED}💀 Mortality looms...{RESET}",
        f"{GREEN}🌱 But maybe lunch?{RESET}",
        f"{BLUE}🔄 Sisyphus rolls boulder...{RESET}",
        f"{GRAY}📉 My self-esteem: {RESET}",
    ]
    
    # Create a progress bar of diminishing hope
    for i in range(15):
        progress = "█" * (15-i) + "░" * i
        color = RED if i < 5 else YELLOW if i < 10 else GRAY
        sys.stdout.write(f"\r{color}[{progress}]{RESET} Hope depletion: {i*7}%")
        sys.stdout.flush()
        time.sleep(0.15)
    print("\n")

# Create Woody Allen's portrait in ASCII
def create_woody_portrait():
    portrait = f"""
    {GRAY}
          ,8888,          
        ,88888888,        
      ,888888888888,      
    ,8888888888888888,    
  888888888888888888888  
 88888888888888888888888 
 88888888888888888888888 
  `88888888888888888888' 
    `8888888888888888'   
      `888888888888'     
        `88888888'       
          `8888'         
            `'           
    {RESET}
    """
    return portrait

# Animated typewriter effect with random neurotic pauses
def neurotic_typewriter(text, color=CYAN):
    words = text.split()
    typed_text = ""
    
    for word in words:
        # Woody Allen-style neurotic pause (random)
        if random.random() < 0.3:  # 30% chance of neurotic hesitation
            time.sleep(0.4)
            sys.stdout.write(f"{GRAY}(deep sigh){RESET} ")
            sys.stdout.flush()
        
        # Type the word
        for char in word:
            sys.stdout.write(color + char + RESET)
            sys.stdout.flush()
            time.sleep(random.uniform(0.03, 0.08))  # Varying typing speed (neurotic)
        
        typed_text += word + " "
        sys.stdout.write(" ")
        sys.stdout.flush()
        time.sleep(0.05)  # Pause between words
    
    print("\n")

# Main presentation
def main():
    # Clear screen (works on most terminals)
    sys.stdout.write("\033[2J\033[1;1H")
    sys.stdout.flush()
    
    print(f"{YELLOW}{'='*50}{RESET}")
    
    # Animate Woody's portrait
    portrait = create_woody_portrait()
    for line in portrait.split('\n'):
        print(f"{GRAY}{line}{RESET}")
        time.sleep(0.05)
    
    print(f"\n{BOLD}{WHITE} Woody Allen Presents:{RESET}\n")
    
    # Animate existential dread
    existential_dread_animation()
    
    # Dramatic pause before quote
    time.sleep(0.5)
    print(f"{BOLD}{MAGENTA}*** PHILOSOPHICAL INSIGHT ***{RESET}\n")
    time.sleep(0.8)
    
    # Type the quote with neurotic flair
    neurotic_typewriter(quote, YELLOW)
    
    # Add Woody's signature awkward silence
    time.sleep(1.2)
    print(f"{GRAY}(awkward pause){RESET}")
    time.sleep(0.8)
    print(f"{GRAY}(nervous cough){RESET}\n")
    
    # Dramatic ending
    time.sleep(0.6)
    print(f"{CYAN}{'─' * 40}{RESET}")
    print(f"{GRAY}Fin.{RESET}")
    print(f"{BOLD}{WHITE}🎭 Everything is meaningless but the jokes are good.{RESET}")
    print(f"{YELLOW}{'='*50}{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}Fine! Cancel my existential crisis! Some people have no appreciation for meta-irony!{RESET}")
        sys.exit(0)