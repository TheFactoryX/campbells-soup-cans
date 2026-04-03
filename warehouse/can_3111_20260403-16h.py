"""
Campbell's Soup Can #3111
Produced: 2026-04-03 16:57:15
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

pythonimport time
import os

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    DEFAULT = '\033[0m'

def clr(txt, color):
    return f"{color}{txt}{Color.DEFAULT}"

def woody_animation():
    quote = (
        "I bought a book on 'Why Am I Like This?', "
        "but every page just says 'CHAPTER 42: EXISTENTIAL MELTDOWN.' "
        "Now I’m buying another one… in Pig Latin."
    )
    
    art = f"""
{MAGENTA}┌───────────────────────────────────────────────┐{DEFAULT}
│{BLUE} 🧠 {MAGENTA} {clr(quote, YELLOW)}{MAGENTA} 🧠 {DEFAULT}│
└───────────────────────────────────────────────┘{DEFAULT}
    """
    
    print(art)
    colors = [RED, CYAN, GREEN]
    for i in range(5):
        os.system('clear' if os.name == 'posix' else 'cls')
        box_color = colors[i % 3]
        print(f"{box_color}┌───────────────────────────────────────────────┐{DEFAULT}")
        print(f"│{BLUE} 🧠 {box_color} {clr(quote, DARK_CYAN)}{box_color} 🧠 {DEFAULT}│")
        print(f"{box_color}└───────────────────────────────────────────────┘{DEFAULT}")
        time.sleep(1.2)

woody_animation()