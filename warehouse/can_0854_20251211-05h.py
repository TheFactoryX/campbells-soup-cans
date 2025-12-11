"""
Campbell's Soup Can #854
Produced: 2025-12-11 05:39:52
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

# --- Configuration ---
# A quote capturing cosmic insignificance mixed with mundane anxiety
QUOTE = (
    "I've finally accepted that the universe is vast, indifferent, "
    "and inherently meaningless. But what really keeps me up at "
    "night is wondering if I tipped enough on that sandwich in 1998."
)
ATTRIBUTION = "- The Neurotic Philosopher"
WIDTH = 50

# --- ANSI Escape Codes for Aesthetics ---
ESC = "\033["
RESET = f"{ESC}0m"
BOLD = f"{ESC}1m"

# Color Palette (Muted, anxious tones)
C_BORDER = f"{ESC}38;5;94m"   # Dull brown/orange
C_TEXT = f"{ESC}38;5;223m"    # Pale yellowish-white
C_ACCENT = f"{ESC}38;5;131m"  # Muted reddish-brown for emphasis
C_ATTR = f"{ESC}38;5;240m"    # Dark grey

# --- Animation Helpers ---
def typewriter_print(text, color=C_TEXT, min_delay=0.01, max_delay=0.08):
    """Simulates nervous typing."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Pauses for punctuation to simulate deep, worried breaths
        if char in ['.', ',', ';']:
             time.sleep(0.3)
        # Random jittery delays between keystrokes
        time.sleep(random.uniform(min_delay, max_delay))
    sys.stdout.write(RESET)

def nervous_loading():
    """Displays a chaotic, jittery loading bar simulating anxiety."""
    anxiety_chars = ["?", "¿", "!", ".", ":", ";", "~", "-", "_"]
    sys.stdout.write("\n\n")
    
    # Center the loading bar roughly
    indent = " " * ((WIDTH // 2) - 10)
    
    for _ in range(30):
        bar = ""
        for i in range(20):
            # Color changes randomly to reflect panic
            color = random.choice([C_BORDER, C_ACCENT, C_ATTR])
            char = random.choice(anxiety_chars)
            bar += color + char
        
        progress_msg = random.choice(["Calculating existence", "Hyperventilating", "Checking WebMD", "Panicking silently"])
        
        sys.stdout.write(f"\r{indent}[{bar}{RESET}] {C_ATTR}{progress_msg}...{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Clear the anxiety bar line
    sys.stdout.write(f"\r{indent}" + " " * 50 + "\r")
    time.sleep(0.5)

# --- Text Layout Helpers ---
def wrap_text(text, width):
    lines = []
    words = text.split()
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def center_pad(text, width):
    pad = width - len(text)
    left = pad // 2
    right = pad - left
    return " " * left + text + " " * right

# --- Main Presentation ---
def presentquote():
    sys.stdout.write(f"{ESC}2J{ESC}H") # Clear screen
    
    nervous_loading()
    
    sys.stdout.write("\n")

    # Top Border
    border_line = "═" * (WIDTH + 2)
    print(f"  {C_BORDER}╔{border_line}╗{RESET}")

    # Content
    wrapped_lines = wrap_text(QUOTE, WIDTH)
    for i, line in enumerate(wrapped_lines):
        sys.stdout.write(f"  {C_BORDER}║ {RESET}")
        
        # Highlight the "sandwich in 1998" part as the source of true anxiety
        if "1998" in line:
             parts = line.split("sandwich in 1998")
             sys.stdout.write(center_pad(parts[0], WIDTH - len("sandwich in 1998.") - 1))
             typewriter_print("sandwich in 1998.", color=C_ACCENT + BOLD, min_delay=0.08, max_delay=0.15)
        else:
             centered_line = center_pad(line, WIDTH)
             typewriter_print(centered_line)

        sys.stdout.write(f"{C_BORDER} ║{RESET}\n")

    # Bottom Border
    print(f"  {C_BORDER}╚{border_line}╝{RESET}")

    # Attribution
    time.sleep(0.5)
    attr_padded = center_pad(ATTRIBUTION, WIDTH + 4)
    sys.stdout.write(f"\n  {C_ATTR}{attr_padded}{RESET}\n\n")

if __name__ == "__main__":
    try:
        presentquote()
    except KeyboardInterrupt:
        # Even interrupting the program causes anxiety
        print(f"\n{C_ACCENT}Oh god, you stopped it. Did I say something wrong??{RESET}\n")