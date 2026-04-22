"""
Campbell's Soup Can #3399
Produced: 2026-04-22 11:31:37
Worker: OpenAI: GPT-4 (openai/gpt-4)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.border_char = "*"

    def __add_border(self, line, padding=2):
        border = " " + padding * " " + self.border_char + line + self.border_char
        return border

    def print_quote(self, padding=2):
        quoted_text = f" \"{self.text}\" - {self.author} " 
        max_len = len(max(quoted_text.split("\n"), key=len))
        horizontal_line = self.__add_border(self.border_char * max_len)

        print("\033[1;34;40m")  # Set color to blue 

        # Print top border
        print(horizontal_line)

        # Print text 
        for line in quoted_text.split("\n"):
            print(self.__add_border(line.ljust(max_len)))

        # Print bottom border
        print(horizontal_line)

        print("\033[0;37;40m")  # Reset color to default


def main():
    funny_philosophical_quote = Quote("I'm not afraid of dying, I just don't want to be there when it happens.", "Woody Allen")
    funny_philosophical_quote.print_quote()


if __name__ == "__main__":
    main()