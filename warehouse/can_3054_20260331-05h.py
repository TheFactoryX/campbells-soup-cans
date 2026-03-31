"""
Campbell's Soup Can #3054
Produced: 2026-03-31 05:54:37
Worker: Qwen: Qwen3.6 Plus Preview (free) (qwen/qwen3.6-plus-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def main():
    # ANSI Escape Codes
    R  = "\033[0m"      # Reset
    B  = "\033[1m"      # Bold
    H  = "\033[38;5;74m"  # Header Cyan
    X  = "\033[38;5;245m" # Frame Grey
    Q  = "\033[38;5;223m" # Quote Warm White
    S  = "\033[38;5;185m" # Signature Gold

    # Hide terminal cursor for cleaner animation
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    time.sleep(0.1)

    sys.stdout.write("\n\n\n")
    
    # Animated ASCII Header
    header_art = [
        f"  {H}{B}.   *       .       *   .{R}",
        f"   {H}{B}    .  EXISTENTIAL  .    {R}",
        f"  {H}{B}.   *       .       *   .{R}"
    ]
    for line in header_art:
        sys.stdout.write(line + "\n")
        sys.stdout.flush()
        time.sleep(0.25)

    time.sleep(0.4)

    # The Woody Allen-esque Philosophical Quote
    quote_text = (
        "The universe expands relentlessly, fleeing from whatever "
        "cosmic neurosis birthed it... and frankly, so am I, "
        "if I could just find someone to split the cab fare "
        "to a place with fewer expectations."
    )

    # Word wrapping logic
    words = quote_text.split()
    lines = []
    current = ""
    max_w = 64
    for word in words:
        if not current:
            current = word
        elif len(current) + len(word) + 1 <= max_w:
            current += " " + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)

    # Box dimensions & drawing
    inner_w = 68
    top    = f"{X}╔{'═' * inner_w}╗{R}"
    bot    = f"{X}╚{'═' * inner_w}╝{R}"
    empty  = f"{X}║{' ' * inner_w}║{R}"

    sys.stdout.write(top + "\n")
    sys.stdout.write(empty + "\n")
    sys.stdout.flush()
    time.sleep(0.3)

    # Typewriter animation for the quote
    for line in lines:
        # Center the text within the inner box width
        padded = line.center(inner_w)
        # Build the colored frame line
        frame_line = f"{X}║{R} {Q}{B}{padded}{R} {X}║{R}"
        
        sys.stdout.write(f"{X}║{R} ")
        sys.stdout.flush()
        for char in f"{Q}{B}{padded}{R}":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.032)
        sys.stdout.write(f" {X}║{R}\n")
        sys.stdout.flush()
        time.sleep(0.35)

    sys.stdout.write(empty + "\n")
    
    # Signature
    sig = "— A Reluctant Cosmic Observer"
    sig_padded = sig.rjust(inner_w)
    sys.stdout.write(f"{X}║{R} {S}{B}{sig_padded}{R} {X}║{R}\n")
    
    sys.stdout.write(empty + "\n")
    sys.stdout.write(bot + "\n")

    sys.stdout.write("\n")
    
    # Restore cursor
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()

if __name__ == "__main__":
    main()