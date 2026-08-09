"""
Campbell's Soup Can #4502
Produced: 2026-08-09 15:46:26
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
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

def clear_screen():
    """Clears the terminal screen."""
    print("\033[H\033[J", end="")

def color_text(text, color_code):
    """Wraps text in ANSI color codes."""
    return f"{color_code}{text}\033[0m"

def typewriter_effect(text, delay=0.05, color="\033[37m"):
    """Prints text with a typewriter animation effect."""
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(quote, width=70):
    """Draws a neurotic, messy ASCII frame around the quote."""
    border_char = random.choice(["+", "-", "*", "x", "#"])
    top = border_char * (width + 2)
    bottom = border_char * (width + 2)
    
    # Colors for the frame
    frame_color = "\033[90m"  # Grey
    quote_color = "\033[95m"  # Magenta
    anxiety_color = "\033[91m" # Red
    
    clear_screen()
    
    # 1. The Nervous Header
    print(color_text("   [ SYSTEM OVERLOAD: EXISTENTIAL DREAD DETECTED ]", anxiety_color))
    print(color_text("   [ Status: Thinking about death... again. ]", anxiety_color))
    print("\n")

    # 2. The Box and Quote
    print(color_text(top, frame_color))
    
    # Calculate padding for centering
    quote = quote.strip()
    if len(quote) > width - 4:
        # Simple wrap logic if quote is too long
        lines = [quote[i:i+width-6] for i in range(0, len(quote), width-6)]
    else:
        lines = [quote]

    for line in lines:
        padding = (width - len(line)) // 2
        left_pad = " " * padding
        right_pad = " " * (width - len(line) - padding)
        print(color_text(f"{border_char}{left_pad}{line}{right_pad}{border_char}", frame_color))

    print(color_text(bottom, frame_color))
    print("\n")

    # 3. The Neurotic Footer
    footer_lines = [
        "I'd ask for a second opinion, but I'm afraid I'd agree with it.",
        "Is it anxiety, or am I just living?",
        "Does this existential crisis make my glasses look too thick?"
    ]
    for line in footer_lines:
        time.sleep(0.5)
        print(color_text(f"  > {line}", "\033[90m"))
    print("\n")

def main():
    # The Woody Allen inspired quote
    woody_quote = (
        "I find the concept of meaninglessness deeply disturbing, "
        "primarily because I'm starting to think "
        "it's actually quite organized."
    )

    # Stage 1: The "Glitchy" Intro
    glitch_chars = ["?", "!", "#", "@", "%", "&"]
    for _ in range(15):
        sys.stdout.write(f"\r\033[91m{''.join(random.choice(glitch_chars) for _ in range(30))}\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)

    # Stage 2: The Reveal
    draw_frame(woody_quote)
    
    # Stage 3: The Dramatic Pause
    time.sleep(1)
    print(color_text("   ..and frankly, it's exhausting.", "\033[93m"))
    time.sleep(2)

if __name__ == "__main__":
    # Check if terminal supports ANSI
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[91m[ Exit aborted by user. Still feeling anxious. ]\033[0m")