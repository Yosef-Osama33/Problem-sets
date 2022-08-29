from bank import value

def main():
    test_return_0()
    test_return_20() 
    test_return_100()

def test_return_0():
    assert value('hello Jo') == 0
    assert value('Hello') == 0
    assert value('HEllo jo') == 0


def test_return_20():
    assert value('hey') == 20
    assert value('hide task') == 20
    assert value('Hossam') == 20

def test_return_100():
    assert value('What is up') == 100
    assert value('yosef') == 100
    assert value('good morning') == 100
if __name__ == "__main__":
    main()