"""
Campbell's Soup Can #5052
Produced: 2026-10-01 23:52:55
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

if __name__ == '__main__':
    # ANSI color codes
    Cyan = '\033[36m'
    Yellow = '\033[33m'
    Reset = '\033[0m'
    
    # The Woody Allen‑style philosophical quote
    quote = "I’m not afraid of death; I’m just afraid I’ll be the only one who shows up to my own funeral."
    
    # Box dimensions
    width = 100               # total width of the box
    inner_width = width - 2   # space between the side characters
    
    # Top and bottom borders
    top    = f"{Cyan}╔{'─'*inner_width}{Reset}{Cyan}╗"
    bottom = f"{Cyan}╚{'─'*inner_width}{Reset}{Cyan}╝"
    
    # Pad the quote so it fits inside the box
    spaces_needed = inner_width - len(quote)   # 5 spaces for this quote
    middle = f"{Cyan}║{Yellow}{quote}{Cyan}{' '*spaces_needed}{Reset}║"
    
    # Print the colorful, visually interesting box
    print(top)
    print(middle)
    print(bottom)