"""
Campbell's Soup Can #4298
Produced: 2026-07-23 09:47:47
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

INTRO = ['heh', '(Y)_', '(Y|_', '(Y|_', ' )_/']
    
ASCII_QUOTE = r"""

  ___      _                             _        
 /	\    (_)_ __ ___   ___ ___  _ __ __| |___ 
/ _ \ | / / '_ \/ _ \ / __/ _ \| '__/ _` / __|
\ ___ / |_| | | | (_) | (_| (_) | | | (_| \__ \
\___/|_(_)_| |_|\___/ \___\___/|_|  \__,_|___/

                    Jase V. Dreamer

"""
COLORS = {
    "intro": "\u001b[95m",
    "header": "\u001b[96m",
    "quote": "\u001b[93m",
    "tagline": "\u001b[92m",
    "end": "\u001b[0m",
}

def clear_line(num):
    print("\r" + "\b" * num, end="")
    print("\033[K", end="")  # Clear remaining characters
    cursor = 0
    clear = cursor + 30
    print(' ' * clear)
    
def animate_intro():
    print("\033c", end="")  # clear the screen
    cursor = 0
    num_line = 0
    for i in range(len(INTRO)):
        print(INTRO[i], end="", flush=True)
        time.sleep(random.randint(1, 3) / 10)
        if i == 2:
            num_line = cursor
        cursor += len(INTRO[i])
    clear_line(num_line)

def print_centered(text, color):
    console_width = 78  # Assuming standard console width
    text_length = len(text)
    left_padding = (console_width - text_length) // 2
    right_padding = console_width - text_length - left_padding
    print(color + " " * left_padding + text + " " * right_padding + "\033[0m")

def print_colored_ascii_quote(quote, ascii_val="", tagline=""):
    customer_width = 80  # Assuming standard console width
    ascii_width = len(ascii_val)
    quote_width = len(quote)
    tagline_width = len(tagline)
    ascii_padding = (customer_width - ascii_width) // 2
    quote_padding = (customer_width - quote_width) // 2
    tagline_padding = (customer_width - tagline_width) // 2
    print(ASCII_QUOTE + color["intro"] + color["header"] + "\n" + color["quote"] + "\n" + color["end"] + '\003') 

    for a in ascii_val:
        print(f"{color['intro']}  {a} {color['end']}")
    print('\003') 
    color["header"] = color["quote"]
    print(color[quote])
    print(f"  {quote} ")
    time.sleep(1)
    clear_line(quote_width + 2)
    print('\003') 
    color["header"] = color["intro"]
    color["quote"] = color["tagline"]
    print(f"{color[tagline_padding]}  {tagline} {color['end']}")

def main():
    animate_intro()
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    print_colored_ascii_quote(quote, " ", "Don't let the bastards grind you down")

if __name__ == "__main__":
    main()