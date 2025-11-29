"""
Campbell's Soup Can #594
Produced: 2025-11-29 06:44:01
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
class color:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"

# Center text in console
def center(text):
    width = 80
    return text.center(width)

# Animated text output
def print_animated(text, color_code, delay=0.01):
    for char in text:
        sys.stdout.write(color_code + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(color.RESET + "\n")
    sys.stdout.flush()

# ASCII art of Woody Allen
woody_face = [
    "   /\_/\   =", color.GREEN,                           # Tux hat
    "  ( o.o )  =", color.GREEN,
    "   > ^ <   =", color.GREEN,
    "",                                  # Empty line
    "    /\\      =", color.YELLOW,
    "   //\\\\     =", color.YELLOW,                      # Cape
    "  ///\\\\\\    =", color.YELLOW,
    " /////\\\\\\\\  =", color.YELLOW,
    "  //////////////////\\        ", color.YELLOW,       # Unrealistically long cape
    "  _____     _____", color.RED,                      # Thinking face
    " /     \\   /     \\",
    "(  / _ \\  ) (  / _ \\  ) =", color.RED,
    " \\_____\\ / \\_____\\ /[1]", color.RED
]

# Prepare Woody's thought bubble
thought_bubble = [
    "                     .-\"\"\"-.                    ",
    "                    /_______\\                   ",
    "                   //'  _   `'\\                  ",
    "                  //  ,'|'.,_  \\                 ",
    "                 // -'  |  `-.  \\                ",
    "                // o     |     `. \\              ",
    "               //|       |       \\ \\             ",
    "                \\\\       ｜       //             ",
    "                 `\\\\______|__.,-'                ",
    "          ''',    ,.    :| |    .,'''          The meaning of life"
]

# Philosophical quote
quote = [
    "I'm not afraid of death; I just don't want to be there",
    "when it happens... To be honest though, I'm afraid",
    "of elevators. If all the wires broke and I started",
    "falling, I'd probably be more afraid of what I might",
    "land on than the actual fall... Exists tend to trip",
    "me in grocery stores. Truly existential dread."
]

# Main animation
def main():
    # Clear screen for best effect (clear doesn't work on Windows terminals)
    sys.stdout.write("\033c")
    
    # Header
    print_animated(center("WOODY ALLEN'S EXISTENTIAL MADNESS"), color.YELLOW)
    
    # Print Woody's thought bubble
    print_animated(center("               "), color.GREEN)
    for line in thought_bubble:
        print_animated(center(line), color.RED)
    
    # Print Woody Stan
    print_animated(center("               "), color.GREEN)
    for line in woody_face:
        # Every 5 lines we change color for dramatic effect
        color_code = color.YELLOW if "cape" in line or any(x in line for x in ["\\", "/"]) else color.RED
        print_animated(center(line), color_code)
    
    # Print quote with dramatic pauses
    print_animated(center("               "), color.YELLOW)
    print_animated(center("        - ME / REFLECT / ABSURD / ", color.CYAN), color.CYAN)
    print_animated(center("                  QUOTES"), color.YELLOW)
    print_animated(center("               "), color.YELLOW)
    
    # Print the quote line by line with pauses
    for i, line in enumerate(quote):
        if i > 0 and i % 2 == 0:
            time.sleep(0.5)  # Pause between sections
        print_animated(center(line), color.RED)
    
    print_animated(center("              -- A PERFECTLY LOGICAL CONCLUSION", color.CYAN), color.CYAN)
    print_animated(center("                     ...or is it?"), color.YELLOW)

if __name__ == "__main__":
    main()