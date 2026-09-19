"""
Campbell's Soup Can #4992
Produced: 2026-09-19 23:06:45
Worker: inclusionAI: Ling 3.0 Flash Sante (free) (inclusionai/ling-3.0-flash-sante:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import math
import os

# ANSI escape codes
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BG_BLACK = "\033[40m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, color=C.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def color_cycle(text, colors, delay=0.05):
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char + C.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_brain():
    brain = f"""
{C.MAGENTA}    .-.    .-.    .-.
   (   )  (   )  (   )
    '-'    '-'    '-'     {C.CYAN}[neurotic cortex]{C.MAGENTA}
   /___\  /___\  /___\    {C.CYAN}[anxiety module]{C.MAGENTA}
  (o o o)(o o o)(o o o)   {C.CYAN}[existential dread]{C.MAGENTA}
   \_|_|_/\_|_|_/\_|_|_/   {C.YELLOW}[overthinking]{C.MAGENTA}
    | | |  | | |  | | |
    | | |  | | |  | | |{C.RESET}
    """
    return brain

def draw_frame(width, height, color=C.CYAN):
    corner = "+"
    h_edge = "-"
    v_edge = "|"
    top = color + corner + h_edge * (width - 2) + corner + C.RESET
    mid = color + v_edge + " " * (width - 2) + v_edge + C.RESET
    bot = color + corner + h_edge * (width - 2) + corner + C.RESET
    lines = [top]
    for _ in range(height - 2):
        lines.append(mid)
    lines.append(bot)
    return "\n".join(lines)

def main():
    clear()
    
    # ASCII art header
    header = f"""
{C.RED}{'='*60}
  {C.YELLOW}W  O  O  D  Y     A  L  L  E  N     S  T  Y  L  E
{C.RED}{'='*60}{C.RESET}
"""
    print(header)
    
    # Animated brain intro
    print(draw_brain())
    time.sleep(0.5)
    
    # The quote - original Woody Allen style
    quote = (
        '"I spent forty years in therapy trying to accept that '
        'the universe doesn\'t care about me. '
        'Then I realized: I don\'t care about the universe either. '
        'We\'re even. Now I just worry about whether my therapist '
        'is judging my choice of snacks."'
    )
    
    # Fancy box
    box_w = max(len(quote) + 4, 50)
    box_h = 7
    
    colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    
    print(draw_frame(box_w, box_h, C.MAGENTA))
    
    # Quote with color cycling
    padded = f"  {quote}  "
    color_cycle(padded, colors * (len(padded) // len(colors) + 1), delay=0.008)
    
    print(draw_frame(box_w, box_h, C.MAGENTA))
    
    # Woody Allen's stage directions
    time.sleep(0.5)
    slow_print(f"\n{C.DIM}  -- from \"Neuroses and Bagels: A Memoir\" (unpublished){C.RESET}", C.DIM, 0.01)
    
    time.sleep(0.3)
    slow_print(f"\n{C.YELLOW}  \"I'm not afraid of death, I just don't want to be there{C.RESET}\"", C.YELLOW, 0.02)
    slow_print(f"{C.YELLOW}   when it happens. Preferably somewhere with Wi-Fi.{C.RESET}\"", C.YELLOW, 0.02)
    
    print(f"\n{C.CYAN}{'~'*60}{C.RESET}")
    slow_print(f"{C.GREEN}  Existential crisis delivered fresh daily.{C.RESET}", C.GREEN, 0.01)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}Abort! Abort! Too much meaning detected!{C.RESET}")