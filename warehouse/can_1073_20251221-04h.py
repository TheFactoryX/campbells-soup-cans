"""
Campbell's Soup Can #1073
Produced: 2025-12-21 04:49:31
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import textwrap

def animate_text(text, delay=0.02):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    # ANSI escape codes for colors
    FRAME = '\033[93m'   # bright yellow (frame)
    TEXT = '\033[95m'    # bright magenta (quote)
    RESET = '\033[0m'    # reset formatting

    # One Woody‑Allen‑style philosophical quote
    quote = (
        "I thought I'd be a philosopher. "
        "Then I realized I'm a neurotic optimist who keeps asking 'Why?' "
        "in the dark, and the answer is 404."
    )

    # Wrap quote so that the frame width stays reasonable
    wrapped = textwrap.wrap(quote, width=60)
    max_len = max(len(line) for line in wrapped)

    # Build the ASCII art frame
    top_border   = f"{FRAME}+{'-' * (max_len + 2)}+{RESET}\n"
    bottom_border = f"{FRAME}+{'-' * (max_len + 2)}+{RESET}\n"
    frame_lines = []
    for line in wrapped:
        padded = line.ljust(max_len)
        frame_line = (
            f"{FRAME}|{RESET} "
            f"{TEXT}{padded}{RESET} "
            f"{FRAME}|{RESET}\n"
        )
        frame_lines.append(frame_line)

    # Combine all parts
    output = top_border + ''.join(frame_lines) + bottom_border

    # Animate the whole output
    animate_text(output)

    # Finally reset terminal colours
    sys.stdout.write(RESET)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
