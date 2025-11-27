"""
Campbell's Soup Can #549
Produced: 2025-11-27 05:35:06
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

def print_ansi(text, ansi_code):
    sys.stdout.write(ansi_code + text + "\033[0m")
    sys.stdout.flush()

# ANSI color codes
BORDER_COLOR = "\033[94m"
HEADER_COLOR = "\033[1;95m"
QUOTE_COLOR = "\033[1;92m"
RESET = "\033[0m"

# ASCII art function
def animated_box():
    box_chars = ["┌", "─", "┐", "│", "┘", "└", "┼", "╷", "╸", "╺", "ibern"
    sizes = [45, 3, 3, 3, 3, 3, 7, 9, 9, 7, 9]
    shifts = [0, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0]
    
    for i in range(20):
        sys.stdout.write("\033[1;3H")  # Move to position (1,3) on terminal
        for idx, char in enumerate(box_chars):
            if idx == 0:  # Top horizontal
                print_ansi(char * 60, BORDER_COLOR)
            elif idx == 1:  # Top horizontal
                row = char * 60
                print_ansi(row, RESET)
            elif idx == 7:  # Quote lines
                quote = "The most important thing in life is extra vacation time. If that's our final destination, then let us all go immediately."
                print_ansi(quote.center(60), QUOTE_COLOR)
            elif idx == 8:  # Author line
                print_ansi("- Woody Allen".center(60), RESET)
            elif idx == 10:  # Leaving info
                print_ansi("Press any key to stop...", RESET)
        sys.stdout.flush()
        sys.stdin.flush()  # Ensure input is flushed
        # Move cursor up to draw next frame
        if i < 10:  # First half: animation
            y = 2 + i // 10 * 10
            status = f"woody = neurotic(200%)"
        else:  # Second half: freeze
            y = 1  # Freeze the animation on last frame
            status = "Neuroticism Level: 100%"
        sys.stdout.write(f"\033[{y};1H{status}")
        sys.stdout.write("\033[K")  # Clear line
        sys.stdout.flush()
        sys.stdin.flush()
        # Delay between frames
        import time
        time.sleep(0.1)

# Main execution
print("\033[2J\033[1;1H")  # Clear terminal and move to top-left

# Print animated ASCII box
animated_box()

# Keep the box visible until a key is pressed
print("\033[1;9HPress any key to exit...")
try:
    input()
except EOFError:
    pass  # Handle Ctrl+D properly
print("\033[2J\033[1;1H")

# Final quote display
print(f"{HEADER_COLOR}┌{'─'*61}┐{RESET}")
print(f"{BORDER_COLOR}│{HEADER_COLOR}             WOO-DY ALLEN'S SARCASM BOX              {BORDER_COLOR}│{RESET}")
print(f"{BORDER_COLOR}├{'─'*61}┤{RESET}")
quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
lines = [quote[:28], quote[28:]]

print(f"{BORDER_COLOR}│{RESET}{f'{QUOTE_COLOR}{lines[0]}{RESET}'.center(62)}{BORDER_COLOR}│{RESET}")
print(f"{BORDER_COLOR}│{RESET}{f'{QUOTE_COLOR}{lines[1]}{RESET}'.center(62)}{BORDER_COLOR}│{RESET}")
print(f"{BORDER_COLOR}├{'—'*61}┤{RESET}")
print(f"{BORDER_COLOR}│{HEADER_COLOR}           - Not afraid of dying just not present          {BORDER_COLOR}│{RESET}")
print(f"{BORDER_COLOR}└{'─'*61}┘{RESET}")