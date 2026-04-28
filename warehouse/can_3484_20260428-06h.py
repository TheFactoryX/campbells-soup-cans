"""
Campbell's Soup Can #3484
Produced: 2026-04-28 06:44:50
Worker: inclusionAI: Ling-2.6-1T (free) (inclusionai/ling-2.6-1t:free)
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

# Woody Allen's Existential Confetti
def neurotic_rainbow(text, delay=0.003):
    colors = [
        "\033[38;5;204m",  # anxious pink
        "\033[38;5;208m",  # neurotic orange
        "\033[38;5;226m",  # paranoid yellow
        "\033[38;5;117m",  # therapy blue
        "\033[38;5;141m",  # lavender doubt
        "\033[38;5;240m",  # existential grey
    ]
    reset = "\033[0m"
    for char in text:
        sys.stdout.write(random.choice(colors) + char + reset)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def trembling_cursor(text, row, col):
    for attempt in range(5):
        jittery_col = col + random.randint(-2, 2)
        sys.stdout.write(f"\033[{row};{max(1,jittery_col)}H{text}\033[K")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f"\033[{row};{col}H{text}\033[K")
    sys.stdout.flush()

def main():
    # Clear screen and hide cursor
    print("\033[2J\033[H\033[?25l", end="")
    
    # Title in a wobbly box
    title = "  Woody Allen's Midnight Panic  "
    width = len(title) + 4
    
    # Draw trembling borders
    for i in range(3):
        sys.stdout.write(f"\033[{5+i};{40 - width//2}H{'╭' if i==0 else '├' if i==1 else '╰'}{'─' * (width-2)}{'╮' if i==0 else '┤' if i==1 else '╯'}")
        sys.stdout.flush()
        time.sleep(0.1)
    
    time.sleep(0.3)
    sys.stdout.write(f"\033[6;{40 - len(title)//2}H\033[1;3m{title}\033[0m")
    sys.stdout.flush()
    
    time.sleep(0.5)
    
    # Dramatic quote with neurotic styling
    quote = "I'm fairly certain that my existential dread is just my soul's way of telling me I forgot to return a library book in 1997."
    
    # Build decorative frame
    frame_top    = "   ╭──────────────────────────────────────────────────────────────────────────╮"
    frame_quote  = "   │                                                                              │"
    frame_bottom = "   ╰──────────────────────────────────────────────────────────────────────────╯"
    
    row_start = 10
    
    # Animate frame entrance (shaky)
    for frame_line in [frame_top, frame_quote, frame_quote, frame_quote, frame_quote, frame_bottom]:
        trembling_cursor(frame_line, row_start + [frame_top, frame_quote, frame_quote, frame_quote, frame_quote, frame_bottom].index(frame_line), 38)
        time.sleep(0.08)
    
    time.sleep(0.4)
    
    # Type the quote with color chaos
    padded_quote = f"   {quote}"
    row = 12
    col = 38
    
    # Clear the quote line first
    sys.stdout.write(f"\033[{row};{col}H{' ' * 78}")
    sys.stdout.flush()
    
    # Type with neurotic pauses
    neurotic_rainbow(f"\033[{row};{col}H{padded_quote}", 0.008)
    
    time.sleep(0.5)
    
    # Author attribution with fading effect
    author = "— Woody (probably sweating right now)"
    for i in range(3):
        sys.stdout.write(f"\033[15;{40 - len(author)//2}H\033[2;38;5;245m{author}\033[0m")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\033[15;{40 - len(author)//2}H{' ' * len(author)}")
        sys.stdout.flush()
        time.sleep(0.2)
    
    sys.stdout.write(f"\033[15;{40 - len(author)//2}H\033[2;38;5;245m{author}\033[0m")
    sys.stdout.flush()
    
    # Confetti of doubt falling
    confetti_chars = ['?', '!', '...', '¬', '°', '·', '∫', '∞', '☕']
    confetti_colors = [
        "\033[38;5;204m", "\033[38;5;208m", "\033[38;5;226m",
        "\033[38;5;117m", "\033[38;5;141m", "\033[38;5;240m"
    ]
    reset = "\033[0m"
    
    for _ in range(40):
        cx = random.randint(20, 100)
        cy = random.randint(17, 22)
        char = random.choice(confetti_chars)
        color = random.choice(confetti_colors)
        sys.stdout.write(f"\033[{cy};{cx}H{color}{char}{reset}")
        sys.stdout.flush()
        time.sleep(0.02)
    
    time.sleep(0.3)
    
    # Tiny footnote that appears and shivers
    footnote = "(The void was not amused. It never is.)"
    for _ in range(3):
        trembling_cursor(f"\033[24;{40 - len(footnote)//2}H\033[38;5;242m{footnote}\033[0m", 24, 40 - len(footnote)//2)
        time.sleep(0.2)
    
    time.sleep(1)
    
    # Restore cursor and move to bottom
    print("\033[?25h\033[28;1H", end="")

if __name__ == "__main__":
    main()