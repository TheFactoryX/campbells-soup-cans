"""
Campbell's Soup Can #2192
Produced: 2026-02-13 03:22:29
Worker: Free Models Router (openrouter/free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys, time, random

def colored(text: str, fg: str) -> str:
    """Wrap text with the given ANSI foreground color."""
    return f"\033[{fg}m{text}\033[0m"

def typewriter(message: str, delay: float = 0.07, colors=("94", "92", "95")):
    """Print each character of `message` one‑by‑one with a random pastel colour."""
    for ch in message:
        sys.stdout.write(colored(ch, random.choice(colors)))
        sys.stdout.flush()
        time.sleep(delay)

def ascii_banner():
    border = "+-------------------------------+"
    line1 = "|   Woody Allen's Philosophical   |"
    line2 = "|   Quote (Neurotic & Funny)       |"
    print(colored(border, "38;5;16"))
    print(colored(line1,  "38;5;16"))
    print(colored(line2,  "38;5;16"))
    print(colored(border, "38;5;16"))

def spinner():
    """A tiny spinner that pretends the program is “thinking”."""
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    i = 0
    print(colored("Thinking …", "38;5;203"), end="", flush=True)
    for _ in range(15):
        print(colored(f"Thinking … {chars[i]}", "38;5;203"), end="", flush=True)
        time.sleep(0.2)
        i = (i + 1) % len(chars)
    print("\n", flush=True)

if __name__ == "__main__":
    ascii_banner()
    spinner()
    quote = "I'm not afraid of death; I just don't want to be there when it happens."
    
    # Give the cursor a little pause before the quote appears
    print("\n", flush=True)
    print(colored("    ", "38;5;209"))   # tiny coloured padding
    typewriter(quote, delay=0.05)
    
    print("\n", flush=True)
    # Wait for any key before exiting
    sys.stdout.write(colored("\033[38;5;208mPress any key to exit…\033[0m"))
    sys.stdout.flush()
    sys.stdin.read(1)