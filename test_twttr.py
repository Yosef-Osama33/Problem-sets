from twttr import shorten

def main():
    test_upper_lower_case()
    test_number()
    test_puncitotation()


def test_upper_lower_case():
    assert shorten ("twitter") == "twttr"
    assert shorten ("TWITTER") == "TWTTR"
    assert shorten ("TwiTTr") == "twTTr"

def test_number():
    assert shorten ("1234") == "1234"

def test_puncitotation():
    assert shorten (".?!,") == ".?!,"






if __name__ == "__main__":
    main()