"""
Campbell's Soup Can #3999
Produced: 2026-06-23 23:30:27
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ╔══════════════════════════════════════════════════════════╗
# ║        🎬  THE WOODY ALLEN EXISTENTIAL GENERATOR  🎬     ║
# ╚══════════════════════════════════════════════════════════╝

# ANSI color codes
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"
    BG_DARK = "\033[40m"

def slow_print(text, delay=0.03, color=Color.WHITE):
    """Print text character by character with color."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Color.RESET)
    print()

def blink_print(text, blinks=3, delay=0.15):
    """Print text that blinks."""
    for _ in range(blinks):
        sys.stdout.write(f"\033[1;97m{text}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write("\r" + " " * (len(text) + 10) + "\r")
        sys.stdout.flush()
        time.sleep(delay)
    print(f"\033[1;97m{text}\033[0m")

def thinking_animation():
    """Show a 'Woody is thinking...' animation."""
    thoughts = [
        "Contemplating the void",
        "Wondering about mortality",
        "Analyzing my relationship with my mother",
        "Questioning free will",
        "Thinking about jazz",
        "Worrying about everything",
    ]
    choice = random.choice(thoughts)
    print()
    for i in range(3):
        for dots in range(4):
            sys.stdout.write(f"\r  {Color.DIM}🧠 {choice}{'.' * dots}{' ' * (3 - dots)}{Color.RESET}")
            sys.stdout.flush()
            time.sleep(0.35)
    print(f"\r  {Color.GREEN}💡 Eureka!{Color.RESET}" + " " * 30)
    time.sleep(0.5)

def draw_saxophone():
    """Draw a tiny saxophone because Woody loves jazz."""
    sax = [
        "      \\",
        "       \\  ♪",
        "    ____\\___",
        "   /        \\",
        "  |  🎷  |",
        "   \\________/",
        "       ||",
        "      _||_\\",
    ]
    return "\n".join(sax)

def draw_neurotic_face():
    """Draw a neurotic little face."""
    face = [
        "       .---.",
        "      / o o \\",
        "     |   <   |",
        "      \\ --- /",
        "       `---´",
    ]
    return "\n".join(face)

def print_box(text, width=60, color=Color.YELLOW):
    """Print text inside a decorative box."""
    print(f"{color}╔{'═' * (width + 2)}╗{Color.RESET}")
    print(f"{color}║{' ' * (width + 2)}║{Color.RESET}")
    
    # Word wrap
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= width:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    for line in lines:
        padding = width - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{color}║ {' ' * left_pad}{Color.WHITE}{Color.BOLD}{line}{Color.RESET}{color}{' ' * right_pad} ║{Color.RESET}")
    
    print(f"{color}║{' ' * (width + 2)}║{Color.RESET}")
    print(f"{color}╚{'═' * (width + 2)}╝{Color.RESET}")

def existential_progress_bar():
    """A progress bar that fills up to 'Existential Dread Level'."""
    print(f"\n  {Color.DIM}Measuring existential dread...{Color.RESET}")
    bar_width = 40
    for i in range(bar_width + 1):
        filled = "█" * i
        empty = "░" * (bar_width - i)
        percent = int((i / bar_width) * 100)
        
        if percent < 30:
            color = Color.GREEN
            label = "Mildly Concerned"
        elif percent < 60:
            color = Color.YELLOW
            label = "Moderately Anxious"
        elif percent < 90:
            color = Color.RED
            label = "Full-Blown Neurosis"
        else:
            color = Color.MAGENTA + Color.BOLD
            label = "Peak Woody Allen"
        
        sys.stdout.write(f"\r  {color}[{filled}{empty}] {percent}% {label}{Color.RESET}")
        sys.stdout.flush()
        time.sleep(0.04)
    print()

def main():
    # The quote
    quote = (
        "I finally made peace with the meaninglessness of existence — "
        "and then my therapist raised her rates."
    )
    
    # Clear screen effect
    print("\033[2J\033[H", end="")
    
    # Title
    print(f"""
{Color.CYAN}  ╔══════════════════════════════════════════════════════════════════╗
  ║                                                                  ║
  ║   🎬 {Color.WHITE}{Color.BOLD}THE WOODY ALLEN EXISTENTIAL QUOTE GENERATOR{COLOR.RESET}{Color.CYAN}              ║
  ║                                                                  ║
  ║   {Color.DIM}"Where there is nothing to be done, there is nothing to     {Color.CYAN}  ║
  ║   {Color.DIM} worry about — but oh, how I worry anyway."              {Color.CYAN}  ║
  ║                                                                  ║
  ╚══════════════════════════════════════════════════════════════════╝{Color.RESET}
""")
    
    # Show the neurotic face
    print(f"  {Color.YELLOW}{draw_neurotic_face()}{Color.RESET}")
    print()
    
    # Thinking animation
    thinking_animation()
    print()
    
    # The quote in a box
    print()
    print_box(quote, width=56, color=Color.CYAN)
    print()
    
    # Existential dread meter
    existential_progress_bar()
    
    # Attribution
    print()
    print(f"  {Color.DIM}         — Woody Allen, probably, while worrying{Color.RESET}")
    print(f"  {Color.DIM}           about whether this quote is too self-deprecating{Color.RESET}")
    print()
    
    # Saxophone
    print(f"  {Color.YELLOW}{draw_saxophone()}{Color.RESET}")
    print()
    
    # Footer
    print(f"  {Color.GRAY}{'─' * 62}{Color.RESET}")
    print(f"  {Color.DIM}  ♪ Thank you. Please tip your therapist. ♪{Color.RESET}")
    print(f"  {Color.GRAY}{'─' * 62}{Color.RESET}")
    print()

if __name__ == "__main__":
    main()