'''
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below,
wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''
from twttr import shorten

def main():
    test_upper_lower_case()
    test_number()

def test_upper_lower_case():
    assert shorten("twitter") == "twttr"
    assert shorten ("TWITTER") == "TWTTR"
def test_number():
    assert shorten ("1234") == "1234"


if __name__ == "__main__":
    main()
