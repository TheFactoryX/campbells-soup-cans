"""
Campbell's Soup Can #4058
Produced: 2026-06-30 22:39:51
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

python-
import time
import sys
import random

# --- CONFIGURATION & CONSTANTS ---
COLORS = {
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "white": "\033[97m",
    "reset": "\033[0m",
    "bold": "\033[1m",
    "italic": "\033[3m",
}

QUOTES = [
    "I'm not afraid of the void; I'm just worried the void will find me unattractive and judge my neuroticism.",
    "My therapist says I have a tendency to overthink, which is a ridiculous thing to say to someone whose only hobby is existential dread.",
    "The meaning of life is elusive, much like a decent bagel in Manhattan or my sense of self-worth.",
    "I have a profound fear of the unknown, but even more profound fear of a universe that actually knows who I am.",
    "Is there a God? I don't know, but if there is, I'm fairly certain He's a critic and He's going to find my performance quite disappointing."
]

def clear_screen():
    print("\033[H\033[J", end="")

def typewriter_print(text, speed=0.05, color=COLORS["white"]):
    """Prints text with a typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def draw_frame(width, height, color=COLORS["cyan"]):
    """Draws a decorative box around the text."""
    top = f"{color}╔{'═' * (width - 2)}╗{COLORS['reset']}"
    bottom = f"{color}╚{'═' * (width - 2)}╝{COLORS['reset']}"
    return top, bottom

def animate_pulse(duration=2):
    """Simulates a nervous, flickering light effect."""
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f"\r{COLORS['magenta']}... pondering the abyss...{COLORS['reset']}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write("\r" + " " * 30 + "\r")
        time.sleep(0.2)

def render_masterpiece():
    """The main performance."""
    COLORS = COLORS # Local reference
    clear_screen()
    
    # 1. Intro sequence
    print(f"\n{COLORS['magenta']}--- THE NEUROTIC THEATER PRESENTS ---{COLORS['reset']}\n")
    time.sleep(0.5)
    
    # 2. Loading 'Anxiety'
    print(f"{COLORS['yellow']}Loading existential dread...{COLORS['reset']}")
    for i in range(0, 101, 10):
        sys.stdout.write(f"\r[{'#' * (i // 5)}{'.' * (20 - i // 5)}] {i}%")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\n")
    
    # 3. Dramatic pause
    animate_pulse(1.5)
    print("\n")

    # 4. The Quote
    quote = random.choice(QUOTES)
    # Split quote for formatting
    words = quote.split()
    line_length = 50
    
    # Wrap text manually for the box
    lines = []
    current_line = []
    current_length = 0
    for word in words:
        if current_length + len(word) + 1 > line_length:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word) + 1
    lines.append(" ".join(current_line))

    # Draw the Box
    width = line_length + 4
    top, bottom = draw_frame(width, 0, COLORS["cyan"])
    
    print(top)
    for line in lines:
        padding = (width - len(line) - 2) // 2
        # Handle odd lengths
        left_pad = " " * (padding + 1)
        right_pad = " " * (width - len(line) - padding - 3)
        print(f"{COLORS['cyan']}║{COLORS['reset']}{left_pad}{COLORS['italic']}{line}{COLORS['reset']}{left_pad}{COLORS['cyan']}║{COLORS['reset']}")
    
    # Fill the bottom if the quote is short
    remaining_lines = 3 # Vertical padding
    for _ in range(remaining_lines):
        print(f"{COLORS['cyan']}║{''* (width - 2)}║{COLORS['reset']}")
        
    print(bottom)

    # 5. The 'Director's Note'
    print(f"\n{COLORS['yellow']}— A mid-life crisis, perhaps?{COLORS['reset']}")
    print(f"{COLORS['magenta']}[Press Ctrl+C to end the neurosis]{COLORS['reset']}\n")

if __    not __name__ == "__main__":
    try:
        render_masterpiece()
        # Keep window open for a moment
        time.sleep(3)
    except KeyboardInterrupt:
        print(f"\n\n{COLORS['red']}Even the audience is leaving. Typical.{COLORS['reset']}")