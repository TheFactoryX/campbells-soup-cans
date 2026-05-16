"""
Campbell's Soup Can #3702
Produced: 2026-05-16 22:05:07
Worker: Poolside: Laguna XS.2 (free) (poolside/laguna-xs.2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Philosophy Box
"""

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_thoughtful_quote():
    # Create a thinking brain ASCII art
    brain = f"""
{Colors.CYAN}    🤔  .-''~''-.{Colors.RESET}
{Colors.CYAN}      .' _   _ '.{Colors.RESET}
{Colors.CYAN}     /   | |   \   {Colors.RESET}
{Colors.CYAN}    |    | |    |  {Colors.RESET}
{Colors.CYAN}   /     |_|     \ {Colors.RESET}
{Colors.CYAN}   |               |{Colors.RESET}
{Colors.CYAN}    \             / {Colors.RESET}
{Colors.CYAN}     '.         .'  {Colors.RESET}
{Colors.CYAN}       '~-------~'   {Colors.RESET}
    """
    
    # The quote in Woody Allen's style
    quote = "I'm having a philosophical crisis — someone please pass the existential dread and a stiff drink."
    
    # Visual presentation
    border = f"{Colors.YELLOW}{'·' * 58}{Colors.RESET}"
    
    print(f"\n{brain}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}        ╔════════════════════════════╗{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}        ║   WOODY ALLEN'S THOUGHTS   ║{Colors.RESET}")
    print(f"{Colors.MAGENTA}{Colors.BOLD}        ╚════════════════════════════╝{Colors.RESET}")
    print(f"\n{border}")
    print(f"{Colors.RED}{Colors.BOLD}  {quote}{Colors.RESET}")
    print(f"{border}")
    print(f"{Colors.GREEN}  (He said while questioning if his therapist had better jokes.){Colors.RESET}")
    print(f"{Colors.YELLOW}{'·' * 58}{Colors.RESET}")
    print(f"{Colors.CYAN}    ~  Where genius meets neurosis, one martini at a time  ~{Colors.RESET}\n")

if __name__ == "__main__":
    print_thoughtful_quote()