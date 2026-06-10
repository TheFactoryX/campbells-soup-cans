"""
Campbell's Soup Can #3906
Produced: 2026-06-10 20:44:51
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, time, itertools

# ANSI escape codes for colors and styles
RESET  = "\033[0m"
BRIGHT = "\033[1m"
DIM    = "\033[2m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"
MAGENTA= "\033[35m"
BOLD   = "\033[1m"
REVERSE= "\033[7m"

# Quote in Woody Allen style
QUOTE = ("I’m not sure if I’m awake, or just dreaming my own nervous breakdown, "
         "but if consciousness is just a probability cloud, "
         "why does it feel so lonely inside the echo chamber of my own mind?")

# Frame ASCII art
FRAME_HORIZONTAL = "-" * 80
FRAME = f"""
{YELLOW}{BRIGHT}+{FRAME_HORIZONTAL}+{RESET}
"""

def animate_print(text, delay=0.04):
    """Print text one character at a time with a typewriter effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def spinning_cursor(stop_event):
    """Animated spinning cursor around the quote."""
    for frame in itertools.cycle(["|", "/", "-", "\\"]):
        sys.stdout.write(f"\r{CYAN}{BRIGHT}Thinking {frame}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
        if stop_event.is_set():
            break
    sys.stdout.write("\r" + " " * 30 + "\r")  # clear the line

import threading
stop_event = threading.Event()

def main():
    print(FRAME)
    # Start spinner in a background thread
    spinner = threading.Thread(target=spinning_cursor, args=(stop_event,))
    spinner.start()

    # Animate the quote
    animate_print(f"{MAGENTA}{BOLD}>>> {RESET}" + QUOTE)

    # Stop spinner after printing
    stop_event.set()
    spinner.join()

    print(FRAME)
    # Final fade-out effect
    for i in range(3, 0, -1):
        sys.stdout.write(f"\r{GREEN}See you in {i} seconds...   ")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\n")

if __name__ == "__main__":
    main()