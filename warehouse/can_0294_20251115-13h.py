"""
Campbell's Soup Can #294
Produced: 2025-11-15 13:33:33
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

# ANSI escape codes
RESET = "\033[0m"
COLORS = [
    "\033[31m",  # red
    "\033[32m",  # green
    "\033[33m",  # yellow
    "\033[34m",  # blue
    "\033[35m",  # magenta
    "\033[36m",  # cyan
]

def random_color():
    return random.choice(COLORS)

def typewriter(text, delay=0.07, color_func=None):
    """Print text character‑by‑character with optional random colors."""
    for ch in text:
        if ch == '\n':
            sys.stdout.write('\n')
        else:
            col = color_func() if color_func else ''
            sys.stdout.write(col + ch + (RESET if col else ''))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

# Simple blink animation with two frames
face_frames = [
    r"""
   _____
  /     \
 | (O O) |
  \_____/
""",
    r"""
   _____
  /     \
 | (× ×) |
  \_____/
"""
]

def blink(frames, count=3, delay=0.5):
    """Clear screen and show each frame in sequence."""
    for _ in range(count):
        for frame in frames:
            sys.stdout.write("\033[2J\033[H")  # clear screen
            print(frame)
            time.sleep(delay)

def main():
    blink(face_frames, count=2, delay=0.6)

    quote = (
        "I always ask myself \"why?\", then answer with an existential shrug. "
        "Life, apparently, is just a sitcom before you realize the laugh track is empty."
    )
    typewriter(quote, delay=0.06, color_func=random_color)

if __name__ == "__main__":
    main()
