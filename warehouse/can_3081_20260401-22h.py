"""
Campbell's Soup Can #3081
Produced: 2026-04-01 22:57:38
Worker: Google: Nano Banana Pro (Gemini 3 Pro Image Preview) (google/gemini-3-pro-image-preview)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# --- Configuration for Visuals ---
# ANSI escape codes for colors
C_RESET = "\033[0m"
C_TEXT_PALE = "\033[38;5;223m"  # A sickly, pale beige
C_TEXT_EMPH = "\033[38;5;215m"  # A slightly more frantic, muted orange
C_BORDER    = "\033[38;5;239m"  # A dark, unobtrusive grey
C_SIGNATURE = "\033[38;5;245m"  # A dim grey for the attribution

# The Quote
quote_part1 = "I ordered a self-help book titled 'How to Cope with the Meaninglessness of Existence,' but it's on permanent backorder... "
quote_part2 = "which I believe is the universe's subtle way of making a point."

# Layout calculations
padding_h = 4
full_quote = quote_part1 + quote_part2
box_width = len(full_quote) + (padding_h * 2)

# --- Helper Functions ---
def nervous_type(text, color_code, base_delay=0.04):
    """Simulates typing with a nervous, jittery rhythm."""
    sys.stdout.write(color_code)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Randomize the sleep time to create a 'nervous' typing effect
        sleep_time = random.uniform(base_delay * 0.2, base_delay * 1.8)
        time.sleep(sleep_time)
    sys.stdout.write(C_RESET)

def create_chaotic_border_line(length):
    """Generates a 'wobbly' border line using chaotic characters."""
    chars = ['~', '-', '.', ',', '`']
    line = ""
    for _ in range(length):
        line += random.choice(chars)
    return line

# --- Main Execution ---
def main():
    # Clear the line and add some top spacing
    print("\r" + " " * (box_width + 10) + "\r", end="") # Clear noisy previous output if any
    print("\n\n")

    # 1. Print Top Border
    border_line_top = create_chaotic_border_line(box_width)
    print(f"{' ':>4}{C_BORDER}{border_line_top}{C_RESET}")

    # 2. Print Left Border and Padding
    sys.stdout.write(f"{' ':>4}{C_BORDER}|{C_RESET}{' ' * padding_h}")

    # 3. Print Plot Part 1 (nervously)
    nervous_type(quote_part1, C_TEXT_PALE, base_delay=0.035)

    # 4. Comedic Pause
    time.sleep(0.7)

    # 5. Print Plot Part 2 (punchline with slight emphasis and slower, more deliberate pacing)
    nervous_type(quote_part2, C_TEXT_EMPH, base_delay=0.05)

    # 6. Print Right Padding and Border
    sys.stdout.write(f"{' ' * padding_h}{C_BORDER}|{C_RESET}\n")

    # 7. Print Bottom Border
    border_line_bot = create_chaotic_border_line(box_width)
    print(f"{' ':>4}{C_BORDER}{border_line_bot}{C_RESET}")

    # 8. Final 'Signature'
    time.sleep(0.5)
    signature_padding = box_width - 20
    sys.stdout.write(f"\n{' ' * (signature_padding + 4)}")
    nervous_type("-- A Neurotic Philosopher", C_SIGNATURE, base_delay=0.02)
    print("\n\n")

if __name__ == "__main__":
    main()