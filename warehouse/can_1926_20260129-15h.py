"""
Campbell's Soup Can #1926
Produced: 2026-01-29 15:53:35
Worker: Google: Gemini 2.0 Flash Experimental (free) (google/gemini-2.0-flash-exp:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def color_text(text, color_code):
  return f"\033[{color_code}m{text}\033[0m"

def loading_animation(duration=2):
  chars = ["|", "/", "-", "\\"]
  start_time = time.time()
  while time.time() - start_time < duration:
    char = chars[int((time.time() - start_time) * 10) % len(chars)]
    print(f"\r{color_text('Thinking...', 33)} {char}", end="") # 33 is yellow
    time.sleep(0.1)
  print("\r", end="") # Clear the animation line

def print_ascii_art():
  print(color_text("  _    _       _       ", 32))  # Green
  print(color_text(" | |  | |     | |      ", 32))
  print(color_text(" | |__| | __ _| |_ ___ ", 32))
  print(color_text(" |  __  |/ _` | __/ _ \\", 32))
  print(color_text(" | |  | | (_| | ||  __/", 32))
  print(color_text(" |_|  |_|\\__,_|\\__\\___|", 32))
  print()

def main():
  print_ascii_art()

  loading_animation(1.5)

  woody_quote = color_text("You know, I'm convinced that life is just a restaurant.  ", 36) # Cyan
  woody_quote += color_text("Unfortunately, I have a severe allergy to everything on the menu.", 31) #Red.
  woody_quote =  "┌" + "─" * (len(woody_quote) + 2) + "┐\n" + \
                    "│ " + woody_quote + " │\n" + \
                    "└" + "─" * (len(woody_quote) + 2) + "┘"

  print(woody_quote)

  print("\n" + color_text("...and the waiter seems perpetually confused.", 35))  #Magenta
  print()


if __name__ == "__main__":
  main()