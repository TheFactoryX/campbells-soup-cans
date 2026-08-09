"""
Campbell's Soup Can #4506
Produced: 2026-08-09 19:48:04
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic philosophical quote generator in Woody Allen's style.
 existential dread has never looked so colorful.
"""

import sys
import time
import random

# ─── ANSI Color Codes ──────────────────────────────────────────────
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    
    BG_BRIGHT_BLACK = "\033[100m"
    BG_BRIGHT_RED = "\033[101m"
    BG_BRIGHT_GREEN = "\033[102m"
    BG_BRIGHT_YELLOW = "\033[103m"
    BG_BRIGHT_BLUE = "\033[104m"
    BG_BRIGHT_MAGENTA = "\033[105m"
    BG_BRIGHT_CYAN = "\033[106m"
    BG_BRIGHT_WHITE = "\033[107m"


def slow_print(text, delay=0.03):
    """Print text character by character for dramatic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def paranoid_typewriter(text, delay=0.04):
    """
    A typewriter effect with occasional neurotic pauses
    and self-doubting backspaces.
    """
    typed = ""
    i = 0
    while i < len(text):
        char = text[i]
        
        # Occasionally hesitate like a neurotic writer
        if random.random() < 0.08 and len(typed) > 5:
            # Self-doubt pause
            sys.stdout.write(Colors.DIM + "…" + Colors.RESET)
            sys.stdout.flush()
            time.sleep(0.5)
            # Maybe backspace and redo?
            if random.random() < 0.4:
                # Backspace effect
                for _ in range(min(3, len(typed))):
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
                    time.sleep(0.02)
                    typed = typed[:-1]
                i = max(0, i - 3)
                i += 1
                continue
            else:
                # Clear the dots
                for _ in range(1):
                    sys.stdout.write("\b \b")
                    sys.stdout.flush()
        
        typed += char
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
        i += 1
    print()


def draw_thought_bubble(text):
    """Draw the quote inside a wavy, existential thought bubble."""
    
    # Top border with wave pattern
    wave = "╭" + "〰️  " * 20 + "╮"
    # Can't use emoji in some terminals, let's use ASCII
    wave = "  " + "".join([random.choice(["~", "～", "〰", "~ "]) for _ in range(40)])
    
    # Create a box with wavy top
    border_top = "  ╭" + "~" * 56 + "╮"
    border_bottom = "  ╰" + "~" * 56 + "╯"
    
    lines = text.split('\n')
    padded_lines = []
    max_len = max(len(line) for line in lines)
    
    for line in lines:
        padding = (max_len - len(line)) // 2
        padded_lines.append("  │ " + " " * padding + line + " " * (max_len - len(line) - padding) + " │")
    
    # Print top
    print(Colors.BRIGHT_YELLOW + border_top + Colors.RESET)
    
    # Wavy animation on top border
    for _ in range(2):
        wave_line = "  ╭"
        for _ in range(28):
            wave_line += random.choice(["~", "n", "z", "u", "v"])
        wave_line += "╮"
        sys.stdout.write(Colors.CYAN + "\r" + wave_line + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.3)
    
    print("\r" + " " * 60 + "\r", end="")
    print(Colors.BRIGHT_YELLOW + border_top + Colors.RESET)
    
    for line in padded_lines:
        print(Colors.BRIGHT_YELLOW + line + Colors.RESET)
        time.sleep(0.2)
    
    print(Colors.BRIGHT_YELLOW + border_bottom + Colors.RESET)
    
    # Draw little feet underneath
    feet = "     " + Colors.BRIGHT_BLACK + "╯  ╭╯" + Colors.RESET + "  " + \
           Colors.BRIGHT_BLACK + "╯  ╭╯" + Colors.RESET + "  " + \
           Colors.BRIGHT_BLACK + "╯" + Colors.RESET
    print(feet)


def draw_existential_border():
    """Draw a border filled with tiny existential symbols."""
    symbols = list("?!…‽¿¡∶∙·")
    line = "  "
    for _ in range(40):
        line += random.choice(symbols)
    return line


def clear_screen():
    """Clear the terminal screen."""
    # Don't actually clear, just add space
    print("\n" * 3)


def main():
    clear_screen()
    
    # Dramatic title
    title_lines = [
        ("    ╔═══════════════════════════════════════════════╗", Colors.BRIGHT_MAGENTA),
        ("    ║          WOODY ALLEN'S MIND                ║", Colors.BRIGHT_MAGENTA), 
        ("    ║         (SIMULATED PHILOSOPHER)            ║", Colors.BRIGHT_MAGENTA),
        ("    ║         ╔════════════════════╗             ║", Colors.BRIGHT_MAGENTA),
        ("    ║         ║  NEUROTIC MODE: ON  ║             ║", Colors.BRIGHT_RED + Colors.BOLD),
        ("    ║         ╚════════════════════╝             ║", Colors.BRIGHT_MAGENTA),
        ("    ╚═══════════════════════════════════════════════╝", Colors.BRIGHT_MAGENTA),
    ]
    
    print()
    for line, color in title_lines:
        print(color + line + Colors.RESET)
        time.sleep(0.3)
    
    print()
    
    # A wavy existential border
    print(Colors.DIM + "  " + "".join(random.choice("～~") for _ in range(52)) + Colors.RESET)
    print()
    
    # The actual quote - Woody Allen style
    quote = (
        "I used to think the most devastating thing was to\n"
        "be a dwarf with a Napoleon complex who also had\n"
        "a speech impediment that made him say 'herring'\n"
        "instead of 'interesting.' But then I realized...\n"
        "\n"
        "Actually, that's exactly me, so I guess\n"
        "I'm projecting again. But hey, at least\n"
        "my existential crisis comes with built-in humor!\n"
        "\n"
        "    — A man who definitely isn't Woody Allen\n"
        "       (because that would be weird, right?)"
    )
    
    # Print the quote in a thought-bubble-like format
    draw_thought_bubble("                    A THOUGHT")
    
    print()
    print(Colors.DIM + "  " + "".join(random.choice("～~") for _ in range(52)) + Colors.RESET)
    print()
    
    # Now print the actual quote with typewriter effect
    # Color each line differently
    quote_lines = quote.split('\n')
    colors = [
        Colors.BRIGHT_CYAN,
        Colors.BRIGHT_CYAN,
        Colors.BRIGHT_CYAN,
        Colors.BRIGHT_CYAN,
        Colors.BRIGHT_YELLOW,
        Colors.BRIGHT_YELLOW,
        Colors.BRIGHT_YELLOW,
        Colors.RESET,
        Colors.BRIGHT_MAGENTA,
        Colors.BRIGHT_MAGENTA,
    ]
    
    for i, line in enumerate(quote_lines):
        color = colors[i] if i < len(colors) else Colors.RESET
        # Center the line and add some decoration
        indent = 10
        decorated_line = " " * indent + line
        paranoid_typewriter(color + decorated_line + Colors.RESET, delay=0.02)
        time.sleep(0.3)
    
    # Bottom border
    print()
    print(Colors.DIM + "  " + "".join(random.choice("～~") for _ in range(52)) + Colors.RESET)
    print()
    
    # Little philosophical footer
    footer = (
        Colors.BRIGHT_BLACK +
        "    ╔════════════════════════════════════════════╗\n" +
        "    ║  Remember: You are just a random collection║\n" +
        "    ║  of stardust having an existential crisis. ║\n" +
        "    ║  Enjoy the show!                           ║\n" +
        "    ╚════════════════════════════════════════════╝" +
        Colors.RESET
    )
    slow_print(footer, delay=0.01)
    
    print()
    print(Colors.BRIGHT_BLUE + "    [Existential anxiety level: CRITICAL]" + Colors.RESET)
    print(Colors.BRIGHT_RED + "    [Neurosis intensity: ALLEN-LEVEL MAXIMUM]" + Colors.RESET)


def animated_main():
    """Wrapper that adds a bit of paranoid startup sequence."""
    
    startup_messages = [
        ("Initializing neurotic thought processes...", Colors.BRIGHT_YELLOW),
        ("Calibrating existential dread modules...", Colors.BRIGHT_RED),
        ("Loading philosophy engine v2.7...", Colors.BRIGHT_CYAN),
        ("WARNING: High levels of self-deprecation detected.", Colors.BRIGHT_MAGENTA),
        ("Engaging Woody Allen simulation protocol...", Colors.BOLD + Colors.BRIGHT_GREEN),
    ]
    
    print()
    for msg, color in startup_messages:
        sys.stdout.write(color + "  [" + Colors.BRIGHT_BLACK + "...processing..." + Colors.RESET + "] " + 
                         color + msg + Colors.RESET)
        sys.stdout.flush()
        
        # Animated dots
        for _ in range(3):
            sys.stdout.write(color + "." + Colors.RESET)
            sys.stdout.flush()
            time.sleep(0.4)
        
        # Random paranoid comment
        if random.random() < 0.6:
            comments = [
                " (is this enough?)",
                " (probably not)",
                " (should I restart?)",
                " (too slow?)",
                " (maybe I'm broken)",
            ]
            sys.stdout.write(Colors.DIM + random.choice(comments) + Colors.RESET)
        
        print()
        time.sleep(0.2)
    
    print()
    print(Colors.DIM + "  " + "".join(random.choice("～~") for _ in range(52)) + Colors.RESET)
    print()
    
    main()


if __name__ == "__main__":
    try:
        animated_main()
    except KeyboardInterrupt:
        print("\n\n" + Colors.BRIGHT_RED + 
              "  Even my interruption is existentially meaningless." + 
              Colors.RESET)
        sys.exit(0)
    except Exception as e:
        print("\n\n" + Colors.BRIGHT_RED + 
              "  ERROR: The universe doesn't care about your problems." + 
              Colors.RESET)
        print(Colors.DIM + f"  Technical details: {e}" + Colors.RESET)