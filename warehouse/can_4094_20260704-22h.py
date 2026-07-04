"""
Campbell's Soup Can #4094
Produced: 2026-07-04 22:12:58
Worker: NVIDIA: Nemotron 3 Nano Omni (free) (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

def main():
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"

    quote = "i'm not afraid of death; i just don't want to be there when it happens--especially if the afterlife has a waiting line."
    inner_width = 118
    border = f"{GREEN}+{'-' * inner_width}+{RESET}"
    padded_quote = "  " + quote + "  "  # total length = inner_width
    quote_line = f"{GREEN}|{YELLOW}{padded_quote}{RESET}{GREEN}|"

    print("\n".join([border, quote_line, border]))

if __name__ == "__main__":
    main()