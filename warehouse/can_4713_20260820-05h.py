"""
Campbell's Soup Can #4713
Produced: 2026-08-20 05:45:56
Worker: NVIDIA: Nemotron 3.5 Lightning (free) (nvidia/nemotron-3.5-lightning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""A Woody Allen style philosophical quote, beautifully boxed with colors."""
QUOTE = ("I'm not afraid of death. I just don't want to be there when it happens… "
         "mostly because I'd be heartbroken if the afterlife turned out to be a really long, "
         "awkward dinner party with no dessert.")

C = "\033[96m"  # cyan
Y = "\033[93m"  # yellow
R = "\033[0m"   # reset

# Box width adapts to quote length, minimum 56 chars
w = max(len(QUOTE), 50) + 6

if __name__ == "__main__":
    # Top border
    print(f"{C}╔{'═' * w}╗{R}")
    # Quote line in colorful box
    print(f"{C}║{Y} {QUOTE}{C} ║{R}")
    # Bottom border
    print(f"{C}╚{'═' * w}╝{R}")
    # Neurotic ASCII footer
    print(f"{Y}   ⊂(◉‿◉)⊃  Woody's wisdom in every byte!  ⊂(◉‿◉)⊃{R}")