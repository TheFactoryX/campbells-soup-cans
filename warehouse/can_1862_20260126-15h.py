"""
Campbell's Soup Can #1862
Produced: 2026-01-26 15:45:14
Worker: Xiaomi: MiMo-V2-Flash (xiaomi/mimo-v2-flash)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
"Woody Allen's Guide to Existential Anxiety in Technicolor"
A single-file, no-dependencies, color-bursting, cursor-dancing tribute.
"""

import sys
import time
import random

# ─────────────────────────────────────────────────────────────────────────────
# ANSI Colors & Effects (Linux/macOS/Windows Terminal support)
# ─────────────────────────────────────────────────────────────────────────────
class ANSI:
    """Tiny ANSI color/escape code toolkit."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"

    # Foreground colors (256 is widely supported)
    class FG:
        @staticmethod
        def code(c: int) -> str:
            return f"\033[38;5;{c}m"

        # A fun pastel palette
        LAVENDER = code(183)
        ROSE = code(211)
        LEMON = code(227)
        MINT = code(121)
        SKY = code(117)
        PEACH = code(216)
        GRAY = code(245)
        NEON = code(190)

    @staticmethod
    def move_up(n: int) -> str:
        return f"\033[{n}A"

    @staticmethod
    def move_down(n: int) -> str:
        return f"\033[{n}B"

    @staticmethod
    def move_right(n: int) -> str:
        return f"\033[{n}C"

    @staticmethod
    def move_left(n: int) -> str:
        return f"\033[{n}D"

    @staticmethod
    def clear_line() -> str:
        return "\033[2K"

    @staticmethod
    def hide_cursor() -> str:
        return "\033[?25l"

    @staticmethod
    def show_cursor() -> str:
        return "\033[?25h"

    @staticmethod
    def pos(x: int, y: int) -> str:
        # x = column, y = row (1-based)
        return f"\033[{y};{x}H"


# ─────────────────────────────────────────────────────────────────────────────
# Quote Generation (Woody Allen flavor)
# ─────────────────────────────────────────────────────────────────────────────
def random_pick(options):
    return random.choice(options)

def make_quote():
    """Compose a new, original Woody Allen-style philosophical quote."""
    intros = [
        "I used to think I was neurotic",
        "My therapist says I'm an existential work in progress",
        "I've always feared the universe",
        "Death doesn't scare me",
        "Life's a cosmic joke",
        "I'm not afraid of the void",
        "My hobbies include worrying about the inevitable",
        "Immortality sounds exhausting",
    ]
    middles = [
        "but then I realized",
        "however",
        "so naturally",
        "which is why",
        "and yet",
        "so I thought",
        "and it turns out",
        "in the end",
    ]
    punchlines = [
        "I prefer my midlife crisis with a side of kale and panic.",
        "the void keeps leaving me on read.",
        "I just don't want to be there when it happens.",
        "I scheduled my existential crisis and it ran late.",
        "I'm pretty sure my aura has impostor syndrome.",
        "I'd like immortality delivered to-go, but without the bag.",
        "the universe keeps texting me 'we need to talk'.",
        "I asked for answers and got a therapist bill.",
    ]
    # Construct a Woody-esque two-parter: self-deprecating setup, existential twist.
    return f"{random_pick(intros)}, {random_pick(middles)} {random_pick(punchlines)}"


# ─────────────────────────────────────────────────────────────────────────────
# Visuals: ASCII Art, Colors, Motion & Animation
# ─────────────────────────────────────────────────────────────────────────────
def woody_ascii_art() -> str:
    """Minimalist Woody-esque figure with glasses and expressive eyebrows."""
    # A playful stylization; not a real portrait.
    return r"""
      .-""""-.
     /  _   _ \
    |  (o) (o) |
     \   _^_  /
      '-....-'
       |    |
       '----'
    """

def rainbow_text(text: str) -> str:
    """Colorize each character in a pastel rainbow."""
    colors = [
        ANSI.FG.LEMON,
        ANSI.FG.PEACH,
        ANSI.FG.ROSE,
        ANSI.FG.LAVENDER,
        ANSI.FG.SKY,
        ANSI.FG.MINT,
    ]
    out = []
    for i, ch in enumerate(text):
        c = colors[i % len(colors)]
        out.append(f"{c}{ch}{ANSI.RESET}")
    return "".join(out)

def typewriter_print(text: str, delay: float = 0.02, color: str = None) -> None:
    """Print text with a typewriter effect and optional color."""
    if color:
        sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if color:
        sys.stdout.write(ANSI.RESET)
    sys.stdout.write("\n")
    sys.stdout.flush()

def wavy_print(text: str) -> None:
    """Print text with an animated sine-wave bounce using ANSI."""
    chars = list(text)
    n = len(chars)
    if n == 0:
        return

    # Animate a wave (3 frames) moving left-to-right across the text
    for t in range(n + 6):
        # Clear line and move to start
        sys.stdout.write(ANSI.clear_line())
        sys.stdout.write(ANSI.pos(1, 0))  # Move to start of current line (fallback)
        # Compose frame
        line = []
        for i in range(n):
            # Sine amplitude: 2 rows visual up/down
            offset = int(2 * (0.5 + 0.5 * ((t - i) / 6)))
            ch = chars[i]
            # Pick color by phase
            phase = (t + i) % 6
            colors = [ANSI.FG.LEMON, ANSI.FG.PEACH, ANSI.FG.ROSE, ANSI.FG.LAVENDER, ANSI.FG.SKY, ANSI.FG.MINT]
            c = colors[phase]
            line.append(f"{c}{ch}{ANSI.RESET}")
        # Add a subtle underline wave
        wave = ("_" * n).replace("_", "▁", max(0, t - 3))
        sys.stdout.write("".join(line))
        sys.stdout.write("\n")
        sys.stdout.write(wave)
        sys.stdout.flush()
        time.sleep(0.06)
    sys.stdout.write("\n")

def draw_box(lines: list[str]) -> None:
    """Wrap lines in a colorful, dashed box."""
    width = max(len(l) for l in lines)
    # Borders in neon
    border_color = ANSI.FG.NEON
    top = f"{border_color}┏{ANSI.FG.NEON}{'━' * (width + 2)}{ANSI.FG.NEON}┓{ANSI.RESET}"
    bottom = f"{border_color}┗{ANSI.FG.NEON}{'━' * (width + 2)}{ANSI.FG.NEON}┛{ANSI.RESET}"
    mid = f"{border_color}┃{ANSI.RESET}  {ANSI.FG.GRAY}{{content}}{ANSI.RESET}  {border_color}┃{ANSI.RESET}"

    sys.stdout.write(f"{top}\n")
    for line in lines:
        content = line.ljust(width)
        sys.stdout.write(mid.replace("{{content}}", content) + "\n")
    sys.stdout.write(f"{bottom}\n")
    sys.stdout.flush()

def animated_confetti() -> None:
    """Celebrate the punchline with a brief burst of falling confetti."""
    rows = 5
    cols = 40
    colors = [ANSI.FG.LEMON, ANSI.FG.PEACH, ANSI.FG.ROSE, ANSI.FG.LAVENDER, ANSI.FG.SKY, ANSI.FG.MINT]
    chars = ["*", ".", "+", "•", "✦", "✧"]

    # Build initial grid
    grid = [[None for _ in range(cols)] for _ in range(rows)]

    for step in range(18):
        # Spawn new particles at top
        for c in range(cols):
            if random.random() < 0.15 and grid[0][c] is None:
                grid[0][c] = (random.choice(chars), random.choice(colors))

        # Draw
        sys.stdout.write(ANSI.move_up(rows) if step > 0 else "")
        for r in range(rows):
            line = []
            for c in range(cols):
                if grid[r][c]:
                    ch, col = grid[r][c]
                    line.append(f"{col}{ch}{ANSI.RESET}")
                else:
                    line.append(" ")
            sys.stdout.write("".join(line) + "\n")

        # Move down
        new_grid = [[None for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    if r == rows - 1:
                        # Bottom fades out
                        continue
                    # Random drift left/right
                    drift = random.choice([-1, 0, 1])
                    nc = max(0, min(cols - 1, c + drift))
                    new_grid[r + 1][nc] = grid[r][c]
        grid = new_grid
        sys.stdout.flush()
        time.sleep(0.08)

    # Clear confetti area
    sys.stdout.write(ANSI.move_up(rows))
    for _ in range(rows):
        sys.stdout.write(ANSI.clear_line() + "\n")
    sys.stdout.flush()


# ─────────────────────────────────────────────────────────────────────────────
# Orchestration
# ─────────────────────────────────────────────────────────────────────────────
def main():
    # Try to ensure visual polish and safe cleanup.
    try:
        sys.stdout.write(ANSI.hide_cursor())
        sys.stdout.flush()

        # 1) Draw a minimalist ASCII "Woody" figure with colorized edges
        art = woody_ascii_art()
        for line in art.splitlines():
            if line.strip():
                # Colorize the glasses and mouth subtly
                colored = line.replace('o', f"{ANSI.FG.SKY}o{ANSI.RESET}").replace('"', f"{ANSI.FG.ROSE}\"{ANSI.RESET}")
                sys.stdout.write(f"{ANSI.FG.GRAY}{colored}{ANSI.RESET}\n")
        sys.stdout.write("\n")

        # 2) Typewriter the title
        title = "Woody Allen's Guide to Existential Anxiety in Technicolor"
        typewriter_print(f"{ANSI.BOLD}{ANSI.FG.LEMON}{title}{ANSI.RESET}", delay=0.03)

        # 3) Generate and reveal the quote with visual flair
        quote = make_quote()

        # Split into two parts for dramatic pacing (setup / punchline)
        # Find the comma that splits the self-deprecating intro from the punchline.
        parts = quote.split(",", 1)
        setup = parts[0] + ","
        punchline = parts[1].strip() if len(parts) > 1 else ""

        # Display setup via typewriter, then punchline via wavy animation
        typewriter_print(f"{ANSI.FG.GRAY}{setup}{ANSI.RESET}", delay=0.04)
        time.sleep(0.25)

        # Center the punchline in a box, with a wavy reveal above it
        wavy_print(punchline)

        # 4) Boxed presentation
        draw_box([f"{ANSI.BOLD}{punchline}{ANSI.RESET}"])

        # 5) Confetti celebration for the punchline
        animated_confetti()

        # 6) Subtle footer
        sys.stdout.write(f"\n{ANSI.DIM}{ANSI.FG.GRAY}Generated entirely with pure Python & ANSI codes. No external libraries.{ANSI.RESET}\n")

    finally:
        # Always restore cursor visibility
        sys.stdout.write(ANSI.show_cursor())
        sys.stdout.flush()


if __name__ == "__main__":
    # Windows fallback for ANSI on older consoles (best-effort)
    if sys.platform.startswith("win"):
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass
    main()