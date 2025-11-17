"""
Campbell's Soup Can #330
Produced: 2025-11-17 05:34:54
Worker: Google: Gemini 2.5 Flash (google/gemini-2.5-flash)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() # Newline after typeout

def main():
    clear_screen()

    # ANSI escape codes for colors and reset
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BLUE = "\033[94m" # Added for variety
    MAGENTA = "\033[95m" # Added for variety
    BOLD = "\033[1m"
    RESET = "\033[0m"

    quote_body = (
        "I've finally found the meaning of life. "
        "Unfortunately, it came with terms and conditions, "
        "and I seem to have misplaced the fine print... again."
    )

    # Frame for the quote
    frame_width = max(len(line) for line in quote_body.split('\n')) + 8
    top_bottom_border = BOLD + BLUE + "─" * frame_width + RESET
    side_border = BOLD + BLUE + "│" + RESET

    # Animation steps
    animation_frames = [
        f"{YELLOW}* {RESET}",
        f"{YELLOW}  {RESET}",
    ]

    print("\n" * 3) # Add some padding from the top

    # Top border
    typewriter_print(top_bottom_border, delay=0.005)
    time.sleep(0.5)

    # Intro animation
    for _ in range(3):
        for frame in animation_frames:
            print(f"{side_border}{CYAN}{frame}{RESET} Searching for wisdom... {CYAN}{frame}{RESET}{side_border.replace('│', ' ' * (frame_width - len(' Searching for wisdom... ') - len(frame)*2)) + side_border}")
            time.sleep(0.1)
            # clear_screen() # Uncomment for a more aggressive blink effect, might be too much

    print(f"{side_border}{' ' * (frame_width - 2)}{side_border}")
    print(f"{side_border}{' ' * (frame_width - 2)}{side_border}")

    # Quote display
    words = quote_body.split(' ')
    current_line = []
    line_count = 0
    for word in words:
        if len(' '.join(current_line + [word])) < frame_width - 4: # -4 for side borders and padding
            current_line.append(word)
        else:
            line = ' '.join(current_line)
            padded_line = line.center(frame_width - 2) # Center text within the frame
            typewriter_print(f"{side_border}{BOLD}{RED}{padded_line}{RESET}{side_border}", delay=0.04)
            current_line = [word]
            line_count += 1
            time.sleep(0.1) # Pause between lines

    # Print the last line
    line = ' '.join(current_line)
    padded_line = line.center(frame_width - 2)
    typewriter_print(f"{side_border}{BOLD}{RED}{padded_line}{RESET}{side_border}", delay=0.04)
    line_count += 1

    print(f"{side_border}{' ' * (frame_width - 2)}{side_border}")
    print(f"{side_border}{' ' * (frame_width - 2)}{side_border}")

    # Outro animation with a 'confused' touch
    for _ in range(3):
        typewriter_print(f"{side_border}{' ' * 5}{YELLOW}🤔{RESET}{' ' * (frame_width - 10 - 2)}{YELLOW}❓{RESET}{' ' * 5}{side_border}", delay=0.05)
        time.sleep(0.2)
        typewriter_print(f"{side_border}{' ' * 5}{YELLOW}  {RESET}{' ' * (frame_width - 10 - 2)}{YELLOW}  {RESET}{' ' * 5}{side_border}", delay=0.005)
        time.sleep(0.2)


    # Bottom border
    typewriter_print(top_bottom_border, delay=0.005)
    print("\n" * 2) # More padding at the bottom

    typewriter_print(f"{MAGENTA}{BOLD}  -- A purely hypothetical, slightly neurotic individual.{RESET}", delay=0.02)
    time.sleep(1)

if __name__ == "__main__":
    main()