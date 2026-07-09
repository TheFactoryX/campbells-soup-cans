"""
Campbell's Soup Can #4137
Produced: 2026-07-09 15:36:30
Worker: OpenAI: gpt-oss-20b (free) (openai/gpt-oss-20b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

def slow_print(text: str, delay: float = 0.03) -> None:
    for i, ch in enumerate(text):
        color = COLOR_LIST[i % len(COLOR_LIST)]
        sys.stdout.write(f"{color}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)