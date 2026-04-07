"""
Campbell's Soup Can #3181
Produced: 2026-04-07 18:11:26
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys, time, os

def main():
    # ANSI color codes
    RED   = "\033[31m"
    GREEN = "\033[32m"
    YELLOW= "\033[33m"
    BLUE  = "\033[34m"
    MAGENTA="\033[35m"
    CYAN  = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[0m"
    BOLD  = "\033[1m"

    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Woody Allen‑style quote
    quote = "I keep wondering if the universe is just a bad sitcom and I forgot the laugh track."
    # Simple neurotic ASCII face
    face = r"""
      (\_/)
      ( . .)
      C(")(")
    """

    # Determine box width
    quote_len = len(quote)
    face_lines = face.splitlines()
    face_width = max((len(line) for line in face_lines if line.strip()), default=0)
    width = max(quote_len, face_width) + 4   # padding inside box

    top    = f"{CYAN}{BOLD}╔{'═'*width}╗{RESET}"
    bottom = f"{CYAN}{BOLD}╚{'═'*width}╝{RESET}"
    print(top)

    # Print face centered
    for line in face_lines:
        if line.strip() == "":
            continue
        print(f"{CYAN}{BOLD}║{RESET} {line.center(width)} {CYAN}{BOLD}║{RESET}")

    # Print quote with typing effect
    print(f"{CYAN}{BOLD}║{RESET} ", end="", flush=True)
    for ch in quote:
        sys.stdout.write(f"{YELLOW}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f" {CYAN}{BOLD}║{RESET}")

    print(bottom)

if __name__ == "__main__":
    main()