"""
Campbell's Soup Can #3225
Produced: 2026-04-10 19:11:58
Worker: Z.ai: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI color codes
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    END = '\033[0m'

def clear_screen():
    print("\033[H\033[J", end="")

def type_text(text, delay=0.03, color=None):
    if color:
        color_code = getattr(colors, color.upper(), colors.END)
        text = f"{color_code}{text}{colors.END}"
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def woody_allen_quote():
    clear_screen()
    
    # ASCII art Woody Allen
    woody_art = [
        "      .--.",
        "     |o_o |",
        "     |:_/ |",
        "    //   \\ \\",
        "   (|     | )",
        "  /'\\_   _/`\\",
        "  \\___)=(___/",
        "",
        "     Woody Allen",
        "     (in thought)"
    ]
    
    # Print Woody Allen character
    for line in woody_art:
        print(colors.WHITE + line.center(80) + colors.END)
        time.sleep(0.1)
    
    # Animated frame
    frame_width = 76
    frame_top = "╔" + "═" * frame_width + "╗"
    frame_side = "║" + " " * frame_width + "║"
    frame_bottom = "╚" + "═" * frame_width + "╝"
    
    # Print frame with animation
    print("\n")
    print(colors.BLUE + frame_top + colors.END)
    print(colors.BLUE + frame_side + colors.END)
    print(colors.BLUE + frame_side + colors.END)
    print(colors.BLUE + frame_bottom + colors.END)
    
    # Quote with typewriter effect
    time.sleep(0.5)
    print("\n")
    quote = [
        f"{colors.YELLOW}{colors.UNDERLINE}I don't want to be immortal through my work; I want to be immortal through not dying.{colors.END}",
        f"{colors.WHITE}And if that doesn't work, I'll settle for being remembered as the guy who really loved pastrami.{colors.END}",
        f"{colors.CYAN}Because in the end, we're all just dust with anxieties and a fondness for cured meats.{colors.END}"
    ]
    
    # Center and print quote
    max_len = max(len(line) for line in quote)
    for line in quote:
        centered_line = line.center(max_len + 4)
        print(colors.BLUE + "║" + colors.END + " " + centered_line + " " + colors.BLUE + "║" + colors.END)
        time.sleep(0.5)
    
    # Complete frame
    print(colors.BLUE + "║" + " " * (frame_width + 2) + colors.BLUE + "║" + colors.END)
    print(colors.BLUE + frame_bottom + colors.END)
    
    # Signature
    time.sleep(1)
    print("\n" + colors.GREEN + "    -- Woody Allen" + colors.END)
    
    # Animated thinking bubble
    time.sleep(1)
    print("\n" + colors.BOLD + colors.RED + "THINKING..." + colors.END)
    time.sleep(0.5)
    
    # Animated thought bubble
    for i in range(3):
        bubble_chars = ["•", "o", "O", "°"]
        for char in bubble_chars:
            print(f"\r{colors.BOLD}{colors.RED}{char}{colors.END}", end="")
            time.sleep(0.1)
    
    print("\n" + colors.BOLD + colors.RED + "Maybe I should write another book..." + colors.END)
    
    # Final neurotic thoughts
    time.sleep(1)
    print("\n" + colors.BOLD + colors.MAGENTA + "Or maybe just worry about my legacy while eating a sandwich..." + colors.END)
    time.sleep(0.5)
    print(colors.BOLD + colors.MAGENTA + "Yes, that sounds more productive." + colors.END)
    
    # Philosophical flourish
    time.sleep(1.5)
    print("\n" + colors.BOLD + colors.CYAN + "Life is 10% what happens to you and 90% whether you have enough rye bread for your sandwich." + colors.END)

if __name__ == "__main__":
    woody_allen_quote()