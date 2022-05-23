import MorseCodeDP

def tester(A, expected):
    result = MorseCodeDP.demorse(A)
    difference = {"+": [item for item in result if item not in expected], "-": [item for item in expected if item not in result]}

    return result == expected, difference

def test0():
    A = "..."
    expected = {"eee", "ie", "ei", "s"}
    
    evaluation, difference = tester(A, expected)
    assert evaluation, difference

def test1():
    A = ".-."
    expected = {"ete", "ae", "en", "r"}

    evaluation, difference = tester(A, expected)
    assert evaluation, difference

tests = [test0, test1]
for test in tests:
    print(test())