"""
Campbell's Soup Can #1852
Produced: 2026-01-26 05:48:38
Worker: Noromaid 20B (neversleep/noromaid-20b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""


from typing import Union

def print_quote(quote: Union[str, list[str]]):
    quote = f"""
    {quote}
    """
    print(f'''
    {inspired_quote_layout(quote)}
    ''').center()

def inspired_quote_layout(quote):
    preface_str = f"""
    \n\n{preface()}\n\n
    """
    
    quote_lines = quote.splitlines()
    quote_str = "\n".join([format_line(l) for l in quote_lines])
    
    postscript_str = "\n\n" + postscript() + " \n\n"
    
    return f"{preface_str}{quote_str.center(80)}\n{postscript_str}"

def preface():
    return f"""
    **********************
    In the words of Woody Allen:
    **********************
    """

def postscript():
    return f"""
    Suffering refines the taste.
    **********************
    W.A.
    """

def format_line(line):
    split_line = line.strip().split()
    leading_spaces = ' ' * len(split_line[0])
    line_str = ''.join([leading_spaces] + split_line + [next_line()])
    return line_str.center(80)

def next_line():
    return ''

# Example usage

quote = [
    'Life is full of misery, loneliness, and suffering - and it\'s all over much too soon.',
    'I don\'t want to achieve immortality through my work; I want to achieve it through not dying.'
]
print_quote(quote)