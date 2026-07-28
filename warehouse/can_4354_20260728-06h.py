"""
Campbell's Soup Can #4354
Produced: 2026-07-28 06:40:17
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def animate(s):
    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.07)

def rainbow_color(s, color_code):
    return f"\033{color_code}m{s}\033[0m"

if __name__ == "__main__":
    clear_console()
    time.sleep(0.3)

    foreground_color = "33"
    background_color = "42"
    
    animate(rainbow_color("\n _______\n|/  O  O\\_\n|  O====/  \n|/  \\---/  \n|/   |   \\\n|/   |   \\\n|/   |   \\\n|/   |   \\\n|/   |   \\\n|/   |   \\\n|/   |   \\\n|/   |   \\\n|\\-----\n \\    \\ \n  \\  _  \\\n \\_| |_/\n"))
    time.sleep(0.5)

    woody_hat = rainbow_color(" _______ \n/  ____ \\\n / ,    \\ \n/ \\/ \\ \"'\\ \\\n'         \\ \n/  M M M M \\\n'-----------'", "35;43")
    woody_body = rainbow_color("|    ||    ||\n|    ||    ||\n|    ||    ||\n|    ||    ||\n|       ||  ", "36;46")
    
    print(woody_hat)
    time.sleep(0.3)
    print(woody_body)
    time.sleep(0.3)

    quote = "i wrote the great american novel, 'me been me,' but it's all in the appendix."
    print("\n" + rainbow_color(quote, foreground_color + ";" + background_color))
    time.sleep(1)

    punchline = rainbow_color("\nyou haven't read it, so luckily you're not stuck with it like i am.", "37;45")
    animate(punchline)