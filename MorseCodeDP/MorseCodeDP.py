# idea: take any morse code and turn it into possible translations
import json
import sys

def demorse(A):
    """
    Returns a list of all the possible demorsifications of a string.

    DP analysis gives a runtime of about O(n), where n is the length of A.
    Note that this assumes updating is O(1).

    Input A (str): String of dots (.) and dashes (-)
    Output (list): List of possible alphanumerical translations 
    """

    T = dict() # T(i) = set of possible demorsifications from A[:i]
    T[0] = set(("",))
    morse_dict = json.load(open("morse_code.json", 'r'))

    n = len(A)
    for i in range(1, n+1):
        T_i = set()

        for key, code in morse_dict.items():
            if i-len(code)<0: continue
            if code != A[i-len(code):i]: continue
            T_i.update(prior+key for prior in T[i-len(code)])

        T[i] = T_i

    return T[n]


def format_morse(string):
    """
    Will attempt to convert string to proper format of morse code (dots (.) and dashes (-) with no spaces)

    Input string (str): Morse code of varying formats
    Output (str): Morse code of correct format 
    """
    string.replace(" ", "")
    unique_chars = set(string)
    assert isinstance(string, str), "String should be a Python str instance"
    assert len(unique_chars) <= 2, "String should only have up to two unique characters"
   
    if unique_chars == {"0", "1"}:
        string = string.replace("0", ".")
        string = string.replace("1", "-")
    elif unique_chars == {".", "/"}:
        string = string.replace("/", "-")
    elif unique_chars == {".", "\\"}:
        string = string.replace("\\", "-")
    elif unique_chars == {".", "-"}:
        pass
    else:
        unique_chars = list(unique_chars)
        if unique_chars[0:1] != []: string = string.replace(unique_chars[0], ".")
        if unique_chars[1:2] != []: string = string.replace(unique_chars[1], "-")
    
    return string

if __name__ == "__main__":
    assert sys.argv[1:2], 'Must pass in morse code as first argument inclosed in quotation marks (")'
    morse_code = sys.argv[1]
    print(demorse(format_morse(morse_code)))
