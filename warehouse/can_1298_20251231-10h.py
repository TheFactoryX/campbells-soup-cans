"""
Campbell's Soup Can #1298
Produced: 2025-12-31 10:39:02
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def wally_animation():
    # Screen clear
    sys.stdout.write("\033[H\033[J")
    colors = {
        "dump": "\033[31m",
        "dairy": "\033[36m",
        "muffin": "\033[33m",
        "oh_darlin": "\033[35m",
        "reset": "\033[0m"
    }
    
    quote = (
        "\033[32m(\\     ........   () .-.            (\n"
        "    '|  .:   /(.\\||(  \\) (  .-. \n"
        "        (  ))\"\"  )'   |   ||( )\n"
        "       /  /(_)/  /RR/ (  )(\\ ( \\\\\n"
        "       |/[ ] /[ ] /RR/     | )   \\code-bashing/grape!                \n"
        "       \\   \\_   \\  \n"
        "     _.-%  {SHOULD   WE}\n"
        "    /`-'"   'THINK   (    \n"
        "   /_   **   ._____\\ \\'   \n"
    )
    
    print(f"{colors['oh_darlin']}{'bOOM-boo-boo'}{colors['reset']}")
    print("\n")
    print(f"{colors['dump']}WALLACE'S\n{BIG PIECES}{colors['reset']}             \n{quote}\n")
    
    print(f"{colors['muffin']}   ---   ")
    print(f"{colors['dairy']}\\           /")
    print(f"{colors['dump']}   \\         //   ")
    print(f"{colors['muffin']}     \\     //       ")
    print(f"{colors['dairy']}      \\  //         ")
    print(f"{colors['dump']}      \\_//__________")
    
    # Cream filling animation
    chaos_chars = "\\/|(\\"
    for _ in range(3):
        for c in chaos_chars:
            sys.stdout.write(f"\033[37;1m{c}\033[0m")
            time.sleep(0.03)
        print("\r", end='')
    

if __name__ == "__main__":
    fancy_quote()