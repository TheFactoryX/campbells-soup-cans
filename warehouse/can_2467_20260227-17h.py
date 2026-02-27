"""
Campbell's Soup Can #2467
Produced: 2026-02-27 17:53:50
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def animate_text(text, color=Colors.WHITE, delay=0.03, glitch_chance=0.05):
    """Print text with typewriter effect and occasional glitches."""
    for char in text:
        if random.random() < glitch_chance:
            # Glitch effect: print random character then correct
            sys.stdout.write(color + random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?") + Colors.RESET)
            sys.stdout.flush()
            time.sleep(delay/2)
            sys.stdout.write("\b" + color + char + Colors.RESET)
        else:
            sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_woody_face():
    """Draw a simple Woody Allen face with glasses."""
    face = [
        f"{Colors.BG_WHITE}{Colors.BLACK}  {Colors.RESET}",
        f"{Colors.BG_WHITE}{Colors.BLACK}◔─┼─◕  {Colors.RESET}",
        f"{Colors.BG_WHITE}{Colors.BLACK}  ║    {Colors.RESET}",
        f"{Colors.BG_WHITE}{Colors.BLACK} ─┼─   {Colors.RESET}",
        f"{Colors.BG_WHITE}{Colors.BLACK}  ║    {Colors.RESET}",
        f"{Colors.BG_WHITE}{Colors.BLACK}  ║    {Colors.RESET}",
    ]
    for line in face:
        print(line)

def main():
    clear_screen()
    
    # Woody Allen's neurotic philosophical quote (original creation)
    quote = (
        "I don't want to achieve immortality through my work; "
        "I want to achieve it through not dying. "
        "But then I think: what if the afterlife is just one long therapy session "
        "with my mother? So I've decided to live forever, "
        "or at least until the coffee shop closes."
    )
    
    # Draw Woody's face
    print("\n" * 2)
    draw_woody_face()
    time.sleep(1)
    
    # Animate quote with colorful decorations
    print("\n" + "═" * 60 + Colors.YELLOW)
    print(f"{Colors.BOLD}{Colors.CYAN}»" + " " * 58 + f"{Colors.CYAN}«{Colors.RESET}")
    
    # Split quote into parts for dramatic effect
    parts = [
        "I don't want to achieve immortality through my work;",
        "I want to achieve it through not dying.",
        "",
        "But then I think:",
        "what if the afterlife is just one long therapy session with my mother?",
        "",
        "So I've decided to live forever,",
        "or at least until the coffee shop closes."
    ]
    
    # Print each part with different colors and slight delays
    for i, part in enumerate(parts):
        if not part:
            time.sleep(0.5)
            continue
            
        # Alternate colors for dramatic effect
        colors = [Colors.WHITE, Colors.YELLOW, Colors.GREEN, Colors.MAGENTA, Colors.CYAN]
        color = colors[i % len(colors)]
        
        # Indent nicely
        indent = " " * 4 if i > 0 else ""
        sys.stdout.write(indent)
        animate_text(part, color=color, delay=0.02 if len(part) < 30 else 0.015)
        time.sleep(0.3)
    
    # Bottom decoration
    print("\n" + " " * 4 + "═" * 52 + Colors.YELLOW)
    print(f"{Colors.BOLD}{Colors.RED}— Woody Allen (probably){Colors.RESET}")
    print(" " * 4 + "═" * 52 + Colors.RESET)
    
    # Final neurotic footnote
    time.sleep(1)
    footnote = f"\n{Colors.BLUE}[Note: This quote may cause existential dread. " \
               f"Side effects include overthinking, ordering too much coffee, " \
               f"and avoiding mirrors. Consult your therapist, or at least " \
               f"someone who pretends to listen.]{Colors.RESET}"
    animate_text(footnote, color=Colors.BLUE, delay=0.01, glitch_chance=0.02)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}⟨Interrupted by existential panic⟩{Colors.RESET}")
        sys.exit(0)