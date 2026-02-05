"""
Campbell's Soup Can #2059
Produced: 2026-02-05 15:58:00
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken, missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ── WOODY ALLEN PHILOSOPHICAL QUOTE GENERATOR ────────────────────────────────────
# "I'm not afraid of death; I just don't want to be there when it happens."

class WoodyAllenWisdom:
    def __init__(self):
        self.quote = self._select_quote()
        self.colors = [
            '\033[38;5;208m',  # existential orange
            '\033[38;5;45m',   # neurotic cyan
            '\033[38;5;220m',  # anxious yellow
            '\033[38;5;129m',  # self-deprecating purple
            '\033[38;5;123m',  # overthinking blue
        ]
        self.reset = '\033[0m'
        self.bold = '\033[1m'
        
    def _select_quote(self):
        quotes = [
            "I'm not afraid of death; I just don't want to be there when it happens.",
            "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
            "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
            "What if everything is an illusion and nothing exists? In that case, I definitely overpaid for my carpet.",