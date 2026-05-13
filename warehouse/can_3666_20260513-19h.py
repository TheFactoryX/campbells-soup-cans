"""
Campbell's Soup Can #3666
Produced: 2026-05-13 19:06:07
Worker: inclusionAI: Ring-2.6-1T (free) (inclusionai/ring-2.6-1t:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
🎬 A Woody Allen-Inspired Philosophical Quote Generator
Presented with love, neurosis, and ANSI color codes.
"""

import sys
import time
import os

# ─── ANSI Color Codes ───────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    ITALIC  = "\033[3m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"

# ─── ASCII Art Elements ─────────────────────────────────────────────
MARQUEE_TOP = f"""
{RED}{C.BOLD}  ███╗   ██╗ ██████╗ ██╗   ██╗███████╗██████╗ ████████╗    {YELLOW}╦ ╦╔═╗╔╗ ╔═╗╔═╗{C.RESET}
  ████╗  ██║██╔═══██╗██║   ██║██╔════╝██╔══██╗╚══██╔══╝    {YELLOW}║║║║╣ ╠╩╗║╣ ╚═╗{C.RESET}
  ██╔██╗ ██║██║   ██║██║   ██║█████╗  ██║  ██║   ██║       {YELLOW}╚╝║╠═╣╚═╝╚═╝╚═╝{C.RESET}
  ██║╚██╗██║██║   ██║██║   ██║██╔══╝  ██║  ██║   ██║       {YELLOW}╔═╗║║╚═╗╔═╗╔═╗{C.RESET}
  ██║ ╚████║╚██████╔╝╚██████╔╝██║     ██████╔╝   ██║       {YELLOW}╚═╝╚╝╚═╝╚═╝╚═╝{C.RESET}
  ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═════╝    ╚═╝{C.RESET}
"""

MARQUEE_BOTTOM = f"""
  {MAGENTA}▀▀█▀▀ █▀▀█ █▀▀▄ █▀▀▄ █▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀▀ █▀▀█ █▀▀█ █▀▀▄ {C.RESET}
  {YELLOW}░░▀█░ █▄▄█ █░░█ █░░█ █▄▄▀ █░░█ █▄▄▀ █░░█ █▀▀▀ █▀▀▀ █▄▄▀ █░░█ █░░█ {C.RESET}
  {GREEN}░▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀░ ▀░▀▀ ▀▀▀▀ ▀░▀▀ ▀▀▀░ ▀▀▀░ ▀▀▀░ ▀░░▀ ▀▀▀▀ ▀▀▀▀ {C.RESET}
"""

QUOTE = (
    f"{C.ITALIC}{C.CYAN}Einstein proved that time is relative.{C.RESET}\n"
    f"{C.ITALIC}{C.CYAN}I've been in therapy for 30 years, and it still feels like an eternity.{C.RESET}\n"
    f"{C.ITALIC}{C.CYAN}So either Einstein was wrong,{C.RESET}\n"
    f"{C.ITALIC}{C.MAGENTA} or my therapist is using a very, very slow clock.{C.RESET}\n"
    f"\n"
    f"  {C.DIM}— {C.YELLOW}Woody Allen{C.DIM} (probably){C.RESET}"
)

STAGE_WIDTH = 58


def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if sys.platform == "windows" else "clear")


def draw_curtain():
    """Draw decorative theater curtain."""
    curtain_color = [C.RED, C.DIM + C.RED, C.MAGENTA, C.DIM + C.MAGENTA]
    lines = []
    for row in range(6):
        left = "▓" * (STAGE_WIDTH // 2 - 2)
        right = "▓" * (STAGE_WIDTH // 2 - 2)
        col = curtain_color[row % len(curtain_color)]
        lines.append(f"{col}║{left}  ★  {right}║{C.RESET}")
    return "\n".join(lines)


def draw_box(content_lines):
    """Draw a fancy box around the quote."""
    max_len = max(len(l) for l in content_lines)
    border = f"{C.BLUE}{C.BOLD}{'═' * (max_len + 4)}{C.RESET}"
    top_left = f"{C.BLUE}{C.BOLD}╔{C.RESET}"
    top_right = f"{C.BLUE}{C.BOLD}╗{C.RESET}"
    bot_left = f"{C.BLUE}{C.BOLD}╚{C.RESET}"
    bot_right = f"{C.BLUE}{C.BOLD}╝{C.RESET}"
    side = f"{C.BLUE}{C.BOLD}║{C.RESET}"

    print(f"{top_left}{border}{top_right}")
    for line in content_lines:
        padding = max_len - len(line)
        print(f"{side} {line}{' ' * padding} {side}")
    print(f"{bot_left}{border}{bot_right}")


def typewriter(text, delay=0.015):
    """Print text with a typewriter animation effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def spotlight_effect(quote_lines):
    """Fade-in each line with a dramatic pause."""
    print()
    delays = [0.04, 0.04, 0.04, 0.06, 0.03, 0.03]
    for i, line in enumerate(quote_lines):
        if i < len(delays):
            typewriter(line, delay=delays[i])
        else:
            print(line)
        time.sleep(0.15)


def draw_stars(count=20):
    """Draw scattered twinkling stars."""
    import random
    stars = [C.YELLOW + "✦" + C.RESET, C.WHITE + "✧" + C.RESET,
             C.CYAN + "·" + C.RESET, C.YELLOW + "★" + C.RESET]
    return " ".join(random.choice(stars) for _ in range(count))


def main():
    clear_screen()

    # ── Opening Curtain ──────────────────────────────────────────
    print(f"\n  {C.DIM}🎭  Tonight's presentation at the Theatre of Existential Dread  🎭{C.RESET}\n")
    print(f"  {draw_stars(30)}\n")

    curtain = draw_curtain()
    print(curtain)

    # ── Marquee Title ────────────────────────────────────────────
    print()
    print(MARQUEE_TOP.rstrip())
    print(f"    {C.BOLD}{C.WHITE}O N E    E V E N I N G    O N E    Q U O T E{C.RESET}")
    print(MARQUEE_BOTTOM.strip())

    # ── Dramatic pause ───────────────────────────────────────────
    time.sleep(0.4)
    print(f"\n  {C.DIM}* spotlight narrows *{C.RESET}\n")
    time.sleep(0.3)

    # ── The Quote, in a box ──────────────────────────────────────
    quote_lines = QUOTE.split("\n")
    draw_box(quote_lines)

    # ── Post-quote musings ───────────────────────────────────────
    time.sleep(0.6)
    print(f"\n  {C.DIM}* crowd politely chuckles in the dark *{C.RESET}\n")

    musing = (
        f"  {C.ITALIC}{C.YELLOW}P.S. — {C.RESET}{C.YELLOW}{C.ITALIC}"
        f"If you enjoyed this quote, I have 12,000 more where that came from.{C.RESET}\n"
        f"  {C.ITALIC}{C.DIM}Most of them are about my mother.{C.RESET}"
    )
    typewriter(musing, delay=0.02)

    # ── Closing curtain ──────────────────────────────────────────
    time.sleep(0.5)
    print(f"\n  {draw_stars(25)}")

    curtain2 = draw_curtain()
    print(curtain2)

    print(f"\n  {C.DIM}{C.BOLD}  🎬  CURTAIN  🎬{C.RESET}\n")


if __name__ == "__main__":
    main()