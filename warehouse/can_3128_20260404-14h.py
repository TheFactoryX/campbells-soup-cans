"""
Campbell's Soup Can #3128
Produced: 2026-04-04 14:54:18
Worker: Google: Gemini 2.5 Flash Lite Preview 09-2025 (google/gemini-2.5-flash-lite-preview-09-2025)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

class CodeArtist:
    """A neurotic philosopher rendering engine."""

    def __init__(self):
        self.END = "\033[0m"
        self.BOLD = "\033[1m"
        self.PURPLE = "\033[95m"
        self.CYAN = "\033[96m"
        self.YELLOW = "\033[93m"
        self.RED = "\033[91m"
        self.BLUE_BG = "\033[44m"
        self.BLINK = "\033[5m"
        self.WIDTH = 70

    def _typewrite(self, text, delay=0.04, color=""):
        """Simulates the look of a fast typewriter."""
        sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write(self.END + '\n')

    def _draw_frame(self, content):
        """Draws a stylized frame around the quote."""
        top_bottom = self.CYAN + "═" * (self.WIDTH + 4) + self.END
        side = self.CYAN + "║" + self.END

        print(top_bottom)
        print(f"{side}{' ' * (self.WIDTH + 2)}{side}")

        # Center the content lines
        centered_lines = []
        for line in content.split('\n'):
            padding = (self.WIDTH - len(line)) // 2
            centered_lines.append(f"{side}  {' ' * padding}{line}{' ' * (self.WIDTH - len(line) - padding)}{side}")

        for line in centered_lines:
            print(line)

        print(f"{side}{' ' * (self.WIDTH + 2)}{side}")
        print(top_bottom)


    def render_quote(self):
        """Presents the Woody Allen-esque quote with flair."""
        quote = (
            "The universe is huge, indifferent, and utterly silent.\n"
            "Which just goes to show you, planning that big party\n"
            "was probably overkill."
        )

        # Animation sequence
        print(self.BOLD + self.YELLOW + "\n" + "=" * 80)
        self._typewrite("Loading Existential Dread... (Please wait)", delay=0.02, color=self.RED + self.BLINK)
        print("=" * 80 + self.END + "\n")
        time.sleep(1)

        # Displaying the main content
        self._draw_frame(self.PURPLE + self.BOLD + quote + self.END)

        # Author attribution flourish
        time.sleep(0.5)
        print(f"\n{' ' * 40}— {self.CYAN}A Neurotic Observer{self.END}")
        print(f"{' ' * 45} ({self.YELLOW}Probably suffering from insomnia{self.END})")
        print("\n")


if __name__ == "__main__":
    artist = CodeArtist()
    artist.render_quote()