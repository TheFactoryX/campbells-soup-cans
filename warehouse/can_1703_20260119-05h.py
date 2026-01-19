"""
Campbell's Soup Can #1703
Produced: 2026-01-19 05:48:34
Worker: Qwen: Qwen3 Coder 480B A35B (free) (qwen/qwen3-coder:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def woody_allen_quote():
    # ANSI color codes
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    # Create a typewriter effect
    def typewriter(text, delay=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    # ASCII art frame
    frame_top = f"{CYAN}┌" + "─" * 70 + f"┐{END}"
    frame_bottom = f"{CYAN}└" + "─" * 70 + f"┘{END}"
    
    # The Woody Allen-style quote
    quote = f"{YELLOW}I'm not afraid of eternity, but the idea of spending infinity with my own thoughts is what really terrifies me.{END}"
    attribution = f"{MAGENTA}— Definitely Not Woody Allen, Probably{END}"
    
    # Animation of a neurotic brain
    brain_frames = [
        f"{RED}    ○●○    {END}",
        f"{RED}   ○●●○   {END}",
        f"{RED}  ○●●●○  {END}",
        f"{RED} ○●●●●○ {END}",
        f"{RED}○●●●●●○{END}",
        f"{RED} ○●●●●○ {END}",
        f"{RED}  ○●●●○  {END}",
        f"{RED}   ○●●○   {END}",
        f"{RED}    ○●○    {END}"
    ]
    
    print("\n" * 2)
    
    # Animate the neurotic brain
    for _ in range(2):
        for frame in brain_frames:
            print(f"{BOLD}{GREEN}NEUROTIC MIND IN PROGRESS:{END}".center(75))
            print(frame.center(75))
            time.sleep(0.1)
            print("\033[1A\033[1A")  # Move cursor up two lines
    
    # Clear the animation lines
    print("\033[2K\033[1A\033[2K")
    
    # Present the quote in a fancy box
    print(frame_top)
    print(f"{CYAN}│{END}" + " " * 70 + f"{CYAN}│{END}")
    
    # Center the quote within the box
    quote_lines = []
    words = quote.split()
    line = ""
    
    for word in words:
        if len(line + word) <= 68:
            line += word + " "
        else:
            quote_lines.append(line.strip())
            line = word + " "
    quote_lines.append(line.strip())
    
    for line in quote_lines:
        padding = (70 - len(line)) // 2
        print(f"{CYAN}│{END}" + " " * padding + line + " " * (70 - padding - len(line)) + f"{CYAN}│{END}")
    
    print(f"{CYAN}│{END}" + " " * 70 + f"{CYAN}│{END}")
    print(f"{CYAN}│{END}" + " " * 45 + attribution + " " * (25 - len(attribution)) + f"{CYAN}│{END}")
    print(f"{CYAN}│{END}" + " " * 70 + f"{CYAN}│{END}")
    print(frame_bottom)
    
    # Add some existential dots for dramatic effect
    print("\n" + " " * 30, end="")
    for _ in range(10):
        typewriter(f"{BOLD}.{END}", 0.3)
        print("\033[1D", end="")  # Move cursor back
    
    print("\n" * 2)

if __name__ == "__main__":
    woody_allen_quote()