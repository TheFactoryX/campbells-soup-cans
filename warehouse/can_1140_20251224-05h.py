"""
Campbell's Soup Can #1140
Produced: 2025-12-24 05:41:20
Worker: Google: Gemini 2.5 Flash Lite Preview 09-2025 (google/gemini-2.5-flash-lite-preview-09-2025)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

# --- ANSI Color Codes ---
class C:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BG_BLACK = '\033[40m'
    BG_BLUE = '\033[44m'

# --- Woody Allen Style Quote ---
QUOTE_TEXT = "Existence is this sprawling, poorly directed German Expressionist film, and frankly, I suspect the director is using my own repressed anxieties as the primary plot device."

# --- Visual Presentation ---

def draw_marquee(text, width=80, char='█', color=C.CYAN):
    """Creates a simple, slightly jittery ASCII marquee effect."""
    padding = (width - len(text) - 4) // 2
    
    prefix = f"{C.BG_BLACK}{color}{C.BOLD}"
    suffix = f"{C.RESET}"
    
    for i in range(5): 
        time.sleep(0.1)
        
        # Jitter effect: slightly shift the centering
        shift = random.randint(-1, 1)
        current_padding = max(0, padding + shift)
        
        line = char * 2 + " " * current_padding + text + " " * (width - len(text) - 4 - current_padding) + char * 2
        print(f"{prefix}{line:<{width}}{suffix}")

def draw_think_bubble(text):
    """Draws a stylized, neurotic thought bubble."""
    lines = text.split('\n')
    max_len = max(len(l) for l in lines)
    
    # Frame components
    top = C.YELLOW + "╭" + "─" * (max_len + 4) + "╮" + C.RESET
    middle_start = C.YELLOW + "│ " + C.RESET + C.ITALIC + C.WHITE
    middle_end = C.RESET + C.YELLOW + " │" + C.RESET
    bottom_line = C.YELLOW + "╰" + "─" * (max_len + 4) + "╯" + C.RESET
    
    # The actual speech bubble pointing down (the 'tail')
    tail = " " * (max_len // 2 + 1) + C.YELLOW + "▼" + C.RESET

    print("\n" * 2)
    print(f"{' ' * 20}{top}")
    
    for line in lines:
        padding = max_len - len(line)
        print(f"{' ' * 20}{middle_start}{line}{' ' * padding}{middle_end}")
        
    print(f"{' ' * 20}{bottom_line}")
    print(f"{' ' * 20}{tail}")
    print("\n")

def animate_typing(text, color=C.MAGENTA):
    """Prints the text character by character for a classic AI effect."""
    print(f"{' ' * 10}{C.BOLD}{color}Analyzing existential dread...{C.RESET}")
    time.sleep(0.5)
    print(f"{' ' * 10}{color}>>> ", end="", flush=True)
    
    for char in text:
        print(char, end="", flush=True)
        # Speed adjusted for neurotic pace: slightly uneven
        if char in ('.', ',', '?'):
            time.sleep(random.uniform(0.08, 0.15))
        else:
            time.sleep(random.uniform(0.03, 0.07))
    print(f"{C.RESET}")
    time.sleep(1)


def render_final_scene():
    """Assembles the visual elements."""
    
    W = 78 # Total width of the screen area we want to simulate
    
    # 1. Top border / Title
    print(C.BG_BLUE + " " * W)
    draw_marquee("A Moment of Utter, Unnecessary Insight", width=W, char='~', color=C.BG_BLUE + C.YELLOW)
    print(C.BG_BLUE + " " * W + C.RESET)
    time.sleep(0.5)
    
    # 2. The Quote itself, presented as a troubled thought
    
    # Break the quote up for the speech bubble formatting
    q_lines = [
        "Existence is this sprawling, poorly directed",
        "German Expressionist film, and frankly, I suspect",
        "the director is using my own repressed anxieties",
        "as the primary plot device."
    ]
    
    draw_think_bubble("\n".join(q_lines))
    
    # 3. Typist signature effect
    print(f"\n{' ' * 25}{C.ITALIC}{C.RED}--- (A brief intermission for self-doubt) ---\n{C.RESET}")
    
    # 4. Reveal the source (The Machine) with an animation
    animate_typing(
        f"Source: The Unlicensed Therapist (v1.0)",
        color=C.GREEN
    )
    print("\n" * 2)


if __name__ == "__main__":
    try:
        render_final_scene()
    except KeyboardInterrupt:
        print(f"\n{C.RED}Aborted immediately. Smart move.{C.RESET}")