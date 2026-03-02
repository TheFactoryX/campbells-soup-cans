"""
Campbell's Soup Can #2521
Produced: 2026-03-02 10:06:33
Worker: Upstage: Solar Pro 3 (free) (upstage/solar-pro-3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Woody Allen's Existential Console 🎭

# ANSI color codes
WHITE = "\033[97m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# ASCII Art Frame
quote_art = f"""
{Red}
┌──────────────┐
│  {White}SCRIPTS WITH {Blue}ANGST RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET
│  {White}{Green}COLOR RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET
│  {White}{Blue}FLASHING RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET
│  {Red}{Blue}{White}Existential Reset RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET
│  {Blue}Woody {White}Allen RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET
│  {Blue}Says: RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET RESET
└──────────────┘
"""

# Woody Allen style quote (original)
quote = f"{Blue}I'm not afraid of death; I just don't want to be there when it happens.{Reset}"

# Print with animation effect
import time
import random

# Flashing colors
colors = [WHITE, RED, GREEN, BLUE]
delay = 0.3
for _ in range(5):
    print(f"{quote_art}\n{quote}")
    time.sleep(delay)
    # Randomly change color
    print("\033[1m", end="")  # bold
    print(f"{colors[random.randint(0,3)]}{quote}{RESET}", end="")
    time.sleep(delay)

# Final reveal
print(f"\n\n{Green}[IMPORTANT NOTICE]{RESET}")
print(f"{BLUE}IF LIFE WAS A MOVIE, YOU'D BE THE SECOND ACT WE NEVER SEE - BUT WAIT! THERE IS NO SEASON TWO! ONLY THE TRAILER THAT KEEPS RUNNING IN YOUR HEAD!{RESET}")
print(f"{White}Like a neurotic director who forgot his script in a fridge full of existential pickles.{RESET}")