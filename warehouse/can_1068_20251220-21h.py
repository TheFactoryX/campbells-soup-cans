"""
Campbell's Soup Can #1068
Produced: 2025-12-20 21:28:46
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time

def main():
    quote = (
        "Time is nature's way of keeping everything from happening at once. "
        "Which is clearly not working, because my laundry, existential dread, "
        "and that weird noise from the refrigerator all seem perfectly synchronized."
    )
    author = "- Woody Allen probably"

    # ANSI escape codes
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
    BLINK = "\033[5m"
    RESET = "\033[0m"
    
    # Box drawing characters
    top_left = "╔"
    top_right = "╗"
    bottom_left = "╚"
    bottom_right = "╝"
    vertical = "║"
    horizontal = "═"
    corner_bl = "╠"
    corner_br = "╣"
    horizontal_top = "╦"
    horizontal_bottom = "╩"

    # Split quote into lines that fit in 60 character width
    max_width = 60
    words = quote.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= max_width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(" ".join(current_line))
    
    # Calculate box dimensions
    box_width = max(len(line) for line in lines) + 4
    
    # Top border
    sys.stdout.write(CYAN + top_left + horizontal*(box_width-2) + top_right + RESET + "\n")
    
    # Quote lines with typing animation
    for i, line in enumerate(lines):
        padding = " " * ((box_width - len(line) - 4) // 2)
        centered_line = f"{vertical}{padding}{line}{padding}"
        if len(centered_line) < box_width - 1:
            centered_line += " " * (box_width - len(centered_line) - 1)
        centered_line += vertical
        
        sys.stdout.write(CYAN + vertical + RESET + " "*(box_width-2) + CYAN + vertical + RESET + "\r")
        
        sys.stdout.write(CYAN + vertical + RESET + "  ")
        for idx, char in enumerate(centered_line[4:-4]):
            sys.stdout.write(f"{BOLD}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.04 if char != " " else 0.01)
            # Add random fluctuation to typing speed
            if idx % 7 == 0: time.sleep(0.01)
            if idx % 13 == 0: time.sleep(0.02)
        
        # Cursor effect while waiting between lines
        if i < len(lines) - 1:
            sys.stdout.write(BLINK + " " + RESET)
            sys.stdout.flush()
            time.sleep(0.5)
        
        sys.stdout.write("\n")

    # Author attribution line
    sys.stdout.write(CYAN + corner_bl + horizontal*(box_width-2) + corner_br + RESET + "\n")
    sys.stdout.write(CYAN + vertical + RESET + " "*(box_width - len(author) - 3) + YELLOW + author + " " + CYAN + vertical + RESET + "\n")
    
    # Bottom border
    sys.stdout.write(CYAN + bottom_left + horizontal*(box_width-2) + bottom_right + RESET + "\n")
    
    # Post-display effects
    time.sleep(0.5)
    for _ in range(3):
        for i, line in enumerate(lines):
            sys.stdout.write(f"\033[{i+2}A")  # Move up i+2 lines
        sys.stdout.write("\033[32m")  # Briefly flash green
        time.sleep(0.08)
        sys.stdout.write("\033[0m")
        sys.stdout.flush()
        for i, line in enumerate(lines):
            sys.stdout.write(f"\033[{i+2}B")  # Move back down
        time.sleep(0.15)
    
    time.sleep(1)

if __name__ == "__main__":
    main()