"""
Campbell's Soup Can #5018
Produced: 2026-09-24 19:10:45
Worker: inclusionAI: Ling 3.0 Flash Fin (free) (inclusionai/ling-3.0-flash-fin:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import threading

# ANSI Color Codes
class C:
    R = "\033[91m"
    G = "\033[92m"
    Y = "\033[93m"
    B = "\033[94m"
    M = "\033[95m"
    CY = "\033[96m"
    W = "\033[97m"
    RST = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITAL = "\033[3m"
    UNDER = "\033[4m"
    BLINK = "\033[5m"

# ASCII Art Decorations
def art():
    lines = [
        f"{C.M}{C.BOLD}╔══════════════════════════════════════════════╗{C.RST}",
        f"{C.M}{C.BOLD}║                                              ║{C.RST}",
        f"{C.CY}║    {C.RST}{C.R}{C.BOLD}╔═╗ {C.Y}╔═╗{C.RST}{C.M}{C.BOLD}║   {C.G}{C.BOLD}╔═╗   ╔═╗{C.RST}{C.M}{C.BOLD}  ║{C.RST}",
        f"{C.CY}║    {C.RST}{C.R}{C.BOLD}║ ║{C.Y}║ ║{C.RST}{C.M}{C.BOLD}║   {C.G}{C.BOLD}╠═╣   ║   {C.RST}{C.M}{C.BOLD}║{C.RST}",
        f"{C.CY}║    {C.RST}{C.R}{C.BOLD}╚═╝{C.Y}╚═╝{C.RST}{C.M}{C.BOLD}║   {C.G}{C.BOLD}╚═╝   ╚═╝{C.RST}{C.M}{C.BOLD}  ║{C.RST}",
        f"{C.CY}║    {C.RST}{C.R}{C.BOLD}╔═╗{C.Y}╔═╗{C.RST}{C.M}{C.BOLD}║   {C.G}{C.BOLD}╔═╗   ╔═╗{C.RST}{C.M}{C.BOLD}  ║{C.RST}",
        f"{C.CY}║    {C.RST}{C.R}{C.BOLD}║ ║{C.Y}║ ║{C.RST}{C.M}{C.BOLD}║   {C.G}{C.BOLD}╠═╣   ║   {C.RST}{C.M}{C.BOLD}║{C.RST}",
        f"{C.CY}║    {C.RST}{C.R}{C.BOLD}╚═╝{C.Y}╚═╝{C.RST}{C.M}{C.BOLD}║   {C.G}{C.BOLD}╚═╝   ╚═╝{C.RST}{C.M}{C.BOLD}  ║{C.RST}",
        f"{C.M}{C.BOLD}║                                              ║{C.RST}",
        f"{C.M}{C.BOLD}╚══════════════════════════════════════════════╝{C.RST}",
    ]
    for line in lines:
        print(line)
    time.sleep(0.3)

def spinner_running(stop_event):
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{C.Y}{C.BOLD}  {frames[i % len(frames)]} Contemplating the void... {frames[i % len(frames)]}{C.RST}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()

def typewrite(text, delay=0.03, color=C.W, bold=False):
    prefix = C.BOLD if bold else ""
    for char in text:
        if char == '\n':
            print()
        else:
            sys.stdout.write(f"{prefix}{color}{char}{C.RST}")
            sys.stdout.flush()
            time.sleep(delay)

def main():
    print("\n")
    art()
    print()

    # Spinner animation
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner_running, args=(stop_event,))
    spinner_thread.start()
    time.sleep(1.8)
    stop_event.set()
    spinner_thread.join()

    # Separator
    print(f"\n{C.CY}{'─' * 50}{C.RST}")
    time.sleep(0.2)

    # Quote attribution
    print(f"\n  {C.M}{C.BOLD}{C.ITAL}  — Woody Allen (probably){C.RST}")
    print()
    time.sleep(0.2)

    # The Quote with dramatic typing
    quote_lines = [
        (f"{C.R}{C.BOLD}I{RESET}", C.R),
        (f"{C.Y}{C.BOLD} don't{RESET}", C.Y),
        (f"{C.G}{C.BOLD} have{RESET}", C.G),
        (f"{C.CY}{C.BOLD} a{RESET}", C.CY),
        (f"{C.B}{C.BOLD} problem{RESET}", C.B),
        (f"{C.M}{C.BOLD} with{RESET}", C.M),
        (f"{C.Y}{C.BOLD} oblivion{RESET}", C.Y),
    ]

    print()
    print(f"  {C.W}{C.BOLD}{'═' * 40}{C.RST}")

    full_quote = "I don't have a problem with oblivion; oblivion has a problem with ME."
    # Print with rainbow effect
    colors = [C.R, C.Y, C.G, C.CY, C.B, C.M, C.R, C.Y, C.G, C.CY, C.B, C.M, C.R, C.Y, C.G]
    print("  ", end="")
    for i, ch in enumerate(full_quote):
        if ch == '\n':
            print()
            print("  ", end="")
        else:
            c = colors[i % len(colors)]
            sys.stdout.write(f"{c}{C.BOLD}{ch}{C.RST}")
            sys.stdout.flush()
            time.sleep(0.025)
    print()

    print(f"  {C.W}{C.BOLD}{'═' * 40}{C.RST}")
    print()

    time.sleep(0.3)

    # Punchline
    punchline = "It's not the dying that concerns me — it's the awkward small talk at the reception."
    print(f"  {C.CY}{C.DIM}{C.ITAL}{punchline}{C.RST}")
    print()
    time.sleep(0.3)

    # Bottom border
    print(f"  {C.RST}{C.DIM}{'░' * 50}{C.RST}")
    print()
    time.sleep(0.2)

    # Final flourish
    print(f"  {C.M}{C.BOLD}{C.BLINK}• The universe is indifferent, and so am I •{C.RST}")
    time.sleep(0.5)
    print(f"  {C.Y}{C.DIM}  (press Enter to accept your mortality){C.RST}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.R}Good. At least something's reliable.{C.RST}")
        sys.exit(0)