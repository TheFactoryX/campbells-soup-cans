"""
Campbell's Soup Can #3576
Produced: 2026-05-05 20:17:25
Worker: OpenAI: GPT-5 Codex (openai/gpt-5-codex)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"

palette = [
    "\033[38;5;216m",
    "\033[38;5;219m",
    "\033[38;5;183m",
    "\033[38;5;147m",
    "\033[38;5;111m",
    "\033[38;5;75m",
    "\033[38;5;39m"
]

brain_art = [
    "           ___---___",
    "       .--         --.",
    "     /  .-.  .-.      \\",
    "    /  /   \\/   \\      \\",
    "   |   \\__/\\__/        |",
    "   |    (____)         |",
    "   |  .-`----`-.       |",
    "    \\_/  .--.   \\_____/ ",
    "      \\ (____) /",
    "       '.____.'"
]

thoughts = [
    " recalculating existence...",
    " debating with the furniture...",
    " misplacing certainty...",
    " negotiating with absurdity..."
]

def clear():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def color_cycle():
    while True:
        for color in palette:
            yield color

def animate_brain(duration=3.5):
    start = time.time()
    cycler = color_cycle()
    blink = [DIM, RESET]
    blink_idx = 0
    thought_idx = 0
    while time.time() - start < duration:
        clear()
        color = next(cycler)
        label_color = next(cycler)
        print(f"{color}{BOLD}   ~ Neurotic Thought Laboratory ~{RESET}\n")
        for line in brain_art:
            print(f"{color}{line}{RESET}")
        blink_state = blink[blink_idx % 2]
        print()
        print(f"{label_color}{blink_state} status: {thoughts[thought_idx % len(thoughts)]}{RESET}")
        blink_idx += 1
        thought_idx += 1
        time.sleep(0.35)

def print_quote():
    border_color = "\033[38;5;208m"
    glow_color = "\033[38;5;228m"
    quote_color = "\033[38;5;194m"
    accent = "\033[38;5;33m"
    quote = (
        "I asked the universe for life advice; "
        "it recommended therapy, invoiced me for cosmic insight, "
        "and now I'm dodging my therapist and infinity with the same awkward shuffle."
    )

    clear()
    print(f"{border_color}{BOLD}{'═' * 72}{RESET}")
    print(f"{border_color}{BOLD}║{RESET}{glow_color}{BOLD}   \"{RESET}{quote_color}{quote}{glow_color}{BOLD}\"{RESET}")
    print(f"{border_color}{BOLD}║{RESET}{accent}{ITALIC}        — a nervous aside in the key of existential kvetching{RESET}")
    print(f"{border_color}{BOLD}{'═' * 72}{RESET}")

if __name__ == "__main__":
    animate_brain()
    print_quote()