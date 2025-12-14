"""
Campbell's Soup Can #927
Produced: 2025-12-14 12:57:57
Worker: Nex AGI: DeepSeek V3.1 Nex N1 (free) (nex-agi/deepseek-v3.1-nex-n1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# Get terminal width for nice formatting
try:
	columns = os.get_terminal_size().columns
except:
	columns = 80

# ANSI color codes
class Colors:
	# Wood Allen-esque colors: muted, neurotic, vintage
	neurotic_blue = '\033[95m'      # Light magenta/neurotic purple
	worry_green = '\033[92m'        # Anxious green
	existential_gray = '\033[97m'   # Existential white
	italic_yellow = '\033[93m'      # Self-deprecating yellow
	reset = '\033[0m'
	bold = '\033[1m'
	ital = '\033[3m'

def draw_thinking_man():
	# ASCII art of Woody Allen worrying
	art = r"""
	      .-""-.
	     /      \
	    |  o   o |
	    |   ∆    |    I should really be worrying more about this...
	     \  ~   /
	      '.___.'
	       
	"""
	return art

def typewriter(text, delay=0.03):
	"""Typewriter effect for existential dread"""
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(delay)
	print()

def print_quote():
	# Create a neurotically formatted quote
	quote = ("I don't want to be reincarnated as a butterfly... "
			 "because frankly, I can't handle the pressure of being beautiful "
			 "AND having such a tragically short lifespan. Plus, what if I'm "
			 "reincarnated during the winter? Butterflies don't live through "
			 "winter! I'll just freeze my wings off and be dead AGAIN, which "
			 "ironically would make me kind of depressed about the whole "
			 "eternal cycle of death and rebirth thing... Oh God, I'm getting "
			 "anxiety about my next life before I've even finished this one?!")
	
	# Make the quote look neurotic with colors and formatting
	print("\n" + "="*columns)
	print(f"{Colors.neurotic_blue}{'EXISTENTIAL IRONY'.center(columns)}{Colors.reset}")
	print("="*columns)
	
	# Show the panicking thinker
	man_lines = draw_thinking_man().split('\n')
	for line in man_lines:
		print(f"{Colors.worry_green}{line.center(columns)}{Colors.reset}")
	
	# Slowly reveal the quote for dramatic neurotic effect
	print(f"\n{Colors.bold}")
	typewriter("MY LATEST NEUROTIC OBSESSION:".center(columns), 0.01)
	print(f"\n{Colors.reset}{Colors.italic_yellow}{Colors.ital}")
	
	# Split long quote into parts for typing effect
	words = quote.split()
	line = ""
	for word in words:
		new_line = line + word + " "
		if len(new_line) > columns - 20:  # Account for margins
			typewriter(line.center(columns))
			line = word + " "
		else:
			line = new_line
	typewriter(line.center(columns))
	
	print(f"{Colors.reset}\n")
	
	# Add final existential flourish
	finish_lines = [
		"So now I'm not just afraid of death,",
		"but I'm also developing a phobia of butterflies.",
		"And caterpillars.",
		"And anything with more than 4 legs, actually.",
		"God, I need to lie down..."
	]
	
	for flourish in finish_lines:
		print(f"{Colors.existential_gray}{Colors.ital}{flourish.center(columns)}{Colors.reset}")
		time.sleep(0.5)
	
	print("="*columns + "\n")

if __name__ == "__main__":
	# Show our masterpiece
	print_quote()
	
	# Add a dramatic pause
	time.sleep(2)
	
	# Exit with neurotic uncertainty
	print(f"{Colors.worry_green}{Colors.bold}")
	print("PROGRAM ENDS WITH EXISTENTIAL ANGST".center(columns))
	print(f"{Colors.reset}")
	sys.exit(0)