"""
Campbell's Soup Can #5015
Produced: 2026-09-24 04:52:28
Worker: LiquidAI: LFM2.5-2.6B (free) (liquid/lfm-2.5-2.6b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

"""
A Woody Allen-inspired philosophical quote presented in a visually striking,
colorful format. No external dependencies required — pure Python magic.
"""

# ─── The Quote ──────────────────────────────────────────────────────────────
quote = (
    "I have always believed that the universe is both profoundly beautiful "
    "and utterly indifferent to our existence. We spend our lives searching for "
    "meaning in a cosmos that seems determined to remain silent. Perhaps that "
    "is the point. After all, even the most profound questions often lead us back "
    "to the same uncomfortable truth: we are here, wondering, and that is enough."
)

# ─── ANSI Color Codes ──────────────────────────────────────────────────────
RED   = "\033[91m"
GREEN = "\033[92m"
CYAN  = "\033[96m"
BLUE  = "\033[94m"
WHITE = "\033[97m"
RESET = "\033[0m"

# ─── Helper Functions ──────────────────────────────────────────────────────
def draw_box(text, width):
    """
    Draw a horizontal bar box around *text*.
    The box uses alternating CYAN/BLUE fill blocks for a subtle gradient.
    """
    half = width // 2
    lines = []

    # Top border
    lines.append(f"{RED}{'=' * (half + 2)}{RESET}")

    # Left vertical line
    lines.append(f"{CYAN}{' ' * half}{RESET}")

    # Filled interior (alternating colors)
    for i in range(half):
        if i % 2 == 0:
            lines.append(
                f"{BLUE}▓{' ' * (width - half)}▓{RESET}"
            )
        else:
            lines.append(
                f"{GREEN}▓{' ' * (width - half)}▓{RESET}"
            )

    # Right vertical line
    lines.append(f"{RED}{'=' * (half + 2)}{RESET}")

    # Bottom border
    lines.append(f"{RED}{'=' * (half + 2)}{RESET}")

    return "\n".join(lines)


def center_text(text, width):
    """Return *text* centered within a field of given width."""
    padding = (width - len(text)) // 2
    return f" {text:<{padding}} " + " " * (width - len(text))


# ─── Main ───────────────────────────────────────────────────────────────────
def main():
    # Header decoration
    header = (
        f"\n{WHITE}[ *** WOODY'S EXISTENTIAL MOMENT *** ]{RESET}\n"
        f"{CYAN}╔═══════════════════════════════════════════╗{RESET}\n"
        f"{CYAN}║   A QUOTE FOR THE NIGHT SHIFT   ║{RESET}\n"
        f"{CYAN}╚═══════════════════════════════════════════╝{RESET}\n"
    )

    # Prepare the quote
    q = quote.strip()

    # Compute box size
    w = len(q)
    box = draw_box(q, w)

    # Assemble output
    output = header + box + "\n" + "=" * 58 + "\n"

    print(output)


if __name__ == "__main__":
    main()