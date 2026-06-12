"""
Campbell's Soup Can #3915
Produced: 2026-06-12 05:03:38
Worker: Owl Alpha (openrouter/owl-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import random
import sys

COLOR = {
    "orange":  "\033[38;5;208m",
    "pink":    "\033[38;5;213m",
    "cyan":    "\033[96m",
    "yellow":  "\033[93m",
    "white":   "\033[97m",
    "dim":     "\033[90m",
    "red":     "\033[91m",
    "green":   "\033[92m",
    "blue":    "\033[94m",
    "reset":   "\033[0m",
    "bold":    "\033[1m",
}

def slow_print(text, delay=0.022):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

def center(text, width=68):
    lines = text.split("\n")
    out = []
    for line in lines:
        pad = max(0, (width - len(line.rstrip())) // 2)
        out.append(" " * pad + line.rstrip())
    return "\n".join(out)

def big_banner():
    art = r"""
╔══════════════════════════════════════════════════════════════════════╗
║   _    _                            _     _                        ║
║  | |  | |                          | |   | |                       ║
║  | |__| | _____  _____   _____  ___| |   | |      _____________    ║
║  |  __  |/ _ \ \/ / _ \ / __ \/ __| |   | |     / / ___/  _  \  \  ║
║  | |  | |  __/>  < (_) | (__ \ (__  |   | |    / /\__ \/ /_\ / /   ║
║  |_|  |_|\___/_/\_\___/ \___/\___|__|  _|   /_//____//_____/     ║
║  / ____|                          | |  | |                        ║
║ | |     _____   _____ _ __ ___  __| |  | |    ░░░░░░               ║
║ | |    / _ \ \ / / _ \ '__/ _ \/ _` |  | |   ░▒▒░▒▒░               ║
║ | |___| (_) \ V /  __/ | |  __/ (_| |  |_|   ░▒▒░▒▒░               ║
║  \_____\___/ \_/ \___|_|  \___|\__,_|         ░░░                  ║
╚══════════════════════════════════════════════════════════════════════╝"""
    return art

def typewriter_effect(quote_lines):
    colors = [COLOR["yellow"], COLOR["cyan"], COLOR["pink"]]
    for i, line in enumerate(quote_lines):
        col = colors[i % len(colors)]
        slow_print(f"  {col}{COLOR['bold']}{line}{COLOR['reset']}\n", delay=0.018)
        time.sleep(0.08)

def shake_line(line, color_name="white", times=3, amplitude=3):
    results = []
    col = COLOR[color_name]
    for t in range(times + 1):
        shift = random.randint(-amplitude, amplitude) if t < times else 0
        pad = " " * max(0, shift + amplitude)
        results.append(f"{pad}{col}{line}{COLOR['reset']}")
    return results

def animate_neon_box():
    symbols = ["█","▓","░","▒","▄","▀","░","▒"]
    top_c = COLOR["cyan"]
    bot_c = COLOR["pink"]
    for i in range(len(symbols)):
        y = symbols[i:] + symbols[:i]
        s = "".join(y[:34])
        sys.stdout.write(f"\033[2K\r  {top_c}┌{s}┐{COLOR['reset']}")
        sys.stdout.flush()
        time.sleep(0.12)
    sys.stdout.write("\n")

def flicker(text_in, color_name, times_ms=600):
    col = COLOR[color_name]
    dim = COLOR["dim"]
    for i in range(4):
        sys.stdout.write(f"\r  {'' if i%2 else dim}{text_in}{col}{text_in}{COLOR['reset']}")
        sys.stdout.flush()
        time.sleep(0.35)
    sys.stdout.write(f"\r  {col}{COLOR['bold']}{text_in}{COLOR['reset']}\n")

main_quote = (
    '"My therapist says I have trouble with\n'
    'abandonment issues. I told him that\'s\n'
    'rich coming from someone I\'m paying.\n'
    'Besides, he\'s also Jewish."'
)

quote_speaker = "— Abandonment"

dimensions = [
    "PERSONAL_GROW",
    "INTERPERSONAL",
    "PHILOSOPHICAL_BUT_FUNNY",
    "NEUROTIC_CHARM",
    "SELF_DEPRECATING",
]
dimensions = [
    "Self-Worth          ██████████████████░░  88%",
    "Existential Angst   ████████████████████ 100%",
    "Jewish Humor        █████████████████░░░  87%",
    "Therapy Adherence   ████████████░░░░░░░░  60%",
    "Hope                ██░░░░░░░░░░░░░░░░░░  12%",
]


def main():
    sys.stdout.write("\033[2J\033[H")
    print(f"\n{COLOR['dim']}{'~'}{COLOR['reset']}\n")

    print(f"{COLOR['cyan']}{COLOR['bold']}{big_banner()}{COLOR['reset']}")
    time.sleep(0.6)

# Header Bar
    bar = "█" * 60
    print(f"\n  {COLOR['yellow']}╔═{'═' * 62}═╗{COLOR['reset']}")
    title = " ★ AN EVENING OF NEUROTIC SHORT STORIES BY ★ "
    spac = "=" * ((62 + 6 - len(title)) // 2)
    print(f"  {COLOR['yellow']}║{COLOR['reset']} {COLOR['orange']}{spac}{title}{spac}{COLOR['yellow']:  }  ║{COLOR['reset']}")
    print(f"  {COLOR['yellow']}╚═{'═' * 62}═╝{COLOR['reset']}")
    time.sleep(0.4)

    print(f"\n  {COLOR['dim']}Thinking deeply about the quote...{COLOR['reset']}")
    dots = ["  .     ","  ..    ","  ...     ","  ....    "]
    for d in range(8):
        sys.stdout.write(f"\r  {COLOR['yellow']}{dots[d % 4]}{COLOR['reset']}")
        sys.stdout.flush()
        time.sleep(0.18)
    print(f"\n")

    animate_neon_box()

    print(f"\n  {COLOR['pink']}{COLOR['bold']}{'─' * 38}{COLOR['reset']}")
    print(f"  {COLOR['pink']}{COLOR['bold']}  His profound opening words:{COLOR['reset']}")
    print(f"  {COLOR['pink']}{COLOR['bold']}{'─' * 38}{COLOR['reset']}\n")

    time.sleep(0.2)

    for line in main_quote.split("\n"):
        shake_lines = shake_line(line, color_name="yellow", times=2, amplitude=3)
        for sl in shake_lines:
            sys.stdout.write(f"\r  {sl}")
            sys.stdout.flush()
            time.sleep(0.05)
        print()


    time.sleep(0.3)

    name_color = "white"
    attributions = [
        "— Abandonment",
        "— His Therapist (after switching)",
        "— The Quote itself (self-aware)",
        "— Woody Allen (hypothetically)",
        "— Neurotic Oracle 3000",
    ]
    chosen = 2
    attr = attributions[chosen]

    spac = " " * (48)
    for attr in [attr]:
        sys.stdout.write(f"\r  {spac}{COLOR['dim']}{COLOR['bold']}{attr}{COLOR['reset']}")
        sys.stdout.flush()
        #time.sleep(0.08)
    print()
    time.sleep(0.3)

    # === RADAR CHART MOCKUP ===
    print(f"\n  {COLOR['cyan']}{COLOR['bold']}{'─' * 38}{COLOR['reset']}")
    print(f"  {COLOR['cyan']}{COLOR['bold']}  APPROXIMATE PERSONALITY METRICS{COLOR['reset']}")
    print(f"  {COLOR['cyan']}{COLOR['bold']}{'─' * 38}{COLOR['reset']}\n")


    labels = [
        "Self-Worth          ",
        "Existential Angst   ",
        "Jewish Humor        ",
        "Therapy Adherence   ",
        "Hope                ",
    ]

    metric_lines = [
        "Self-Worth          ██████████░░░░░░░░░░  50%",
        "Existential Angst   ████████████████████ 100%",
        "Jewish Humor        ███████████████░░░░░  78%",
        "Therapy Adherence   ██████░░░░░░░░░░░░░░  32%",
        "Hope                ██░░░░░░░░░░░░░░░░░░  10%",
    ]

    personality_palette = ["pink","red","yellow","cyan","green"]
    for i, line in enumerate(metric_lines):
        # Strip ASCII art, show with moving arrow color
        col = COLOR[personality_palette[i]]
        sys.stdout.write(f"  {col}{line}{COLOR['reset']}")
        time.sleep(0.3)
        print()


    print()

    # === MOOD METER ===
    print(f"\n  {COLOR['red']}♥{COLOR['white']}  CURRENT MOOD ON NARRATIVE DROP:         ", end="")
    mood_bar = "█" * 40
    # Single typewriter for mood
    for ch in mood_bar[:16]:
        {sys.stdout.write(ch), sys.stdout.flush(), time.sleep(0.02)}
    print(f"  {COLOR['dim']} ... still processing therapy bills ...{COLOR['reset']}")

    # ========= END CARD =========
    end_card = f"""{COLOR['dim']}{COLOR['reset']}
  {COLOR['orange']}~ {COLOR['pink']}✦ {COLOR['cyan']}~ {COLOR['yellow']}✦{COLOR['reset']} {COLOR['dim']}End of Transmission{COLOR['reset']} {COLOR['yellow']}✦{COLOR['reset']} {COLOR['cyan']}~ {COLOR['pink']}
                            
"""

    print(end_card)

    slow_print("\n  " + COLOR["dim"] + "“I can’t listen to that much Wagner.\n     I start getting the urge to conquer Poland.”\n                                           – Woody Allen" + COLOR["reset"] + "\n", delay=0.022)

if __name__ == "__main__":
    main()