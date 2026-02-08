"""
Campbell's Soup Can #2124
Produced: 2026-02-08 19:37:33
Worker: Google: Gemini 2.5 Pro Preview 06-05 (google/gemini-2.5-pro-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

def play_neurotic_thought():
    """
    Displays a funny, philosophical, Woody Allen-style quote with
    some light terminal animation and ASCII art.
    """

    class Colors:
        """A class for storing ANSI escape codes for terminal colors."""
        RESET = '\033[0m'
        BOLD = '\033[1m'
        DIM = '\033[2m'
        YELLOW = '\033[93m'
        CYAN = '\033[96m'
        GRAY = '\033[90m'
        ITALIC = '\033[3m'
        RED = '\033[91m'

    def clear_screen():
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def type_effect(text, color=Colors.CYAN, delay=0.04):
        """Prints text with a typewriter effect."""
        for char in text:
            sys.stdout.write(color + char + Colors.RESET)
            sys.stdout.flush()
            time.sleep(delay)
        print() # Newline after the effect

    # --- ASCII Art & Quote ---

    woody_glasses = [
        f"""
{Colors.GRAY}            .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
{Colors.GRAY}         ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
{Colors.GRAY}      ,,,,,,,,,,,,,,,,,....,,,,,,,,,,,,,,,,,,,,,,,,,
{Colors.GRAY}    ,,,,,,,,,,,,.    ({Colors.BOLD}o{Colors.RESET}{Colors.GRAY})  ({Colors.BOLD}o{Colors.RESET}{Colors.GRAY})   .        ,,,,,,,,,,,,
{Colors.GRAY}  ,,,,,,,,,,,,,      .,,      ,,.      .     .,,,,,,,,,,,,
{Colors.GRAY},,,,,,,,,,,,,,,        ''    ''              ,,,,,,,,,,,,,,,
{Colors.GRAY},,,,,,,,,,,,,,,,                           ,,,,,,,,,,,,,,,,,
{Colors.GRAY},,,,,,,,             {Colors.BOLD}/-----\\{Colors.RESET}{Colors.GRAY}               ,,,,,,,,
{Colors.GRAY},,,,,,,,        '    {Colors.BOLD}\\-----/{Colors.RESET}{Colors.GRAY}    '            ,,,,,,,,
{Colors.GRAY}  ,,,,,,,'              '                  ',,,,,,,,,
{Colors.GRAY}    ,,,,,,,'                               ,,,,,,,,,
{Colors.GRAY}      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
{Colors.GRAY}         .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.
        """
    ]

    drain_animation_frames = [
        f"""
{Colors.DIM}
                 ,-----.
             ,--'    '- -,
           ,'           ,.',
          /     ,-----'   '
         /    ,'_.,-''.    \\
        |   ,.'`   .'  '.   |
        |  |     '  (o)  |  |
        |   '.    '.__,'    /
         \\     '-.____,.' ,'
          '.         ,.,-'
           '.     ,-' ,'
             '-,,'---'
{Colors.RESET}""",
        f"""
{Colors.DIM}
                 ,-----.
             ,--'    '- -,
           ,'           ,.',
          /     ,-----'   '
         /    ,'_.,-''.    \\
        |   ,.'`   .'  '.   |
        |  |     ' .(O). |  |
        |   '.    '.__,'    /
         \\     '-.____,.' ,'
          '.         ,.,-'
           '.     ,-' ,'
             '-,,'---'
{Colors.RESET}""",
        f"""
{Colors.DIM}
                 ,-----.
             ,--'    '- -,
           ,'           ,.',
          /     ,-----'   '
         /    ,'_.,-''.    \\
        |   ,.'`   .'  '.   |
        |  |     ' ..*.. |  |
        |   '.    '.__,'    /
         \\     '-.____,.' ,'
          '.         ,.,-'
           '.     ,-' ,'
             '-,,'---'
{Colors.RESET}"""
    ]

    quote_part_1 = "I've been contemplating my place in the grand cosmic scheme..."
    quote_part_2 = "...I suspect I'm the part that gets stuck in the drain."

    # --- The Performance ---

    try:
        clear_screen()
        print(woody_glasses[0])
        time.sleep(1.5)

        print("\n\n")
        type_effect(quote_part_1, color=Colors.CYAN + Colors.ITALIC)
        time.sleep(2)

        clear_screen()

        # Drain animation
        print("\n" * 10) # Center the animation vertically
        for _ in range(4):
            for frame in drain_animation_frames:
                sys.stdout.write("\r" + frame)
                sys.stdout.flush()
                time.sleep(0.15)
        
        clear_screen()
        print(drain_animation_frames[-1])
        print("\n\n")
        
        type_effect(quote_part_2, color=Colors.YELLOW + Colors.ITALIC, delay=0.06)
        time.sleep(1)

        print("\n\n")
        type_effect(f"{Colors.DIM}*ba-dum tss*", color=Colors.GRAY, delay=0.03)
        time.sleep(2)
        
        print("\n" * 4)

    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Oh, an interruption. Of course. Just when I was getting to the point.{Colors.RESET}")
    finally:
        print(Colors.RESET) # Ensure terminal color is reset on exit

if __name__ == "__main__":
    play_neurotic_thought()