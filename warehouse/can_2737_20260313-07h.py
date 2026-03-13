"""
Campbell's Soup Can #2737
Produced: 2026-03-13 07:57:31
Worker: StepFun: Step 3.5 Flash (stepfun/step-3.5-flash)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# Woody Allen philosophical quote generator with visual flair!
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03, color='\033[37m'):
    """Print text with typewriter effect and color"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\033[0m')
    sys.stdout.flush()

def draw_waviness(width):
    """Draw wavy line with alternating colors"""
    colors = ['\033[36m', '\033[34m']  # Cyan and blue
    wave = ""
    for i in range(width):
        color = colors[i % len(colors)]
        wave += color + "~"
    return wave + '\033[0m'

def main():
    clear_screen()
    
    # Terminal dimensions
    try:
        term_width = os.get_terminal_size().columns
    except:
        term_width = 80
    
    # Center everything
    padding = " " * ((term_width - 60) // 2)
    
    # Top wavy border
    print(padding + draw_waviness(60))
    time.sleep(0.1)
    
    # Woody Allen quote (original creation!)
    quote = (
        "\033[33m“I'm not afraid of death; I just don't want to be there when it happens. "
        "I mean, what if it's boring? What if they serve bad coffee in the afterlife? "
        "And why must everything be 'eternal'? Can't I have just a really, really long weekend?\n"
        "\n"
        "I've decided my tombstone should read: 'He finally found something better to do.' "
        "Though knowing my luck, it'll just say: 'Out to lunch - probably at a terrible buffet.'”\033[0m"
    )
    
    # Create box with double lines
    box_top = padding + "\033[33m╔" + "═" * 58 + "╗\033[0m"
    box_bottom = padding + "\033[33m╚" + "═" * 58 + "╝\033[0m"
    empty_line = padding + "\033[33m║\033[0m" + " " * 58 + "\033[33m║\033[0m"
    
    print(box_top)
    time.sleep(0.2)
    print(empty_line)
    time.sleep(0.1)
    
    # Print quote line by line with typewriter effect
    quote_lines = quote.split('\n')
    for line in quote_lines:
        if line.strip():
            # Center each line within the box
            line_padding = " " * ((58 - len(line) + 9) // 2)  # +9 for ANSI codes
            print(padding + "\033[33m║\033[0m" + line_padding, end='')
            slow_print(line.strip(), 0.015, '\033[37m')
            remaining = 58 - (len(line) + len(line_padding) + 1)  # +1 for space before text
            print(" " * remaining + "\033[33m║\033[0m")
            time.sleep(0.05)
        else:
            print(empty_line)
            time.sleep(0.05)
    
    print(empty_line)
    time.sleep(0.2)
    print(box_bottom)
    time.sleep(0.3)
    
    # Bottom wavy border with different pattern
    bottom_wave = padding + draw_waviness(60).replace('~', '≈')
    print(bottom_wave)
    time.sleep(0.2)
    
    # Dramatic signature
    signature = "\033[2m\033[90m~ Woody Allen, probably while avoiding a party ~\033[0m"
    print(" " * ((term_width - len(signature) - 4) // 2) + signature)
    
    # Blinking cursor effect
    time.sleep(1)
    for _ in range(3):
        sys.stdout.write('\033[?25l')  # Hide cursor
        sys.stdout.write('\033[37m' + " " * term_width + '\033[0m\r')
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\033[?25h')  # Show cursor
        sys.stdout.flush()
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[90m⟨Even interruption feels existential⟩\033[0m")
        sys.exit(0)