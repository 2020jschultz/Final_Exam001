""" Pallendrome Checker 
    For this first problem fix the function
    so that if the input text is a pallendrome, it returns True.
    And if not, it returns false.

    Try running it on some samples to make sure it works
"""


def checkisPallendrome(text):
    result = False
    return result


def tester(text, expected_result):
    actual_result = checkisPallendrome(text)

    print_text = "The text was: " + str(text0) + " | "
    if expected_result == actual_result:
        print_text += "Correct: " + str(expected_result) + " == " + str(actual_result)
    else:
        print_text += "Incorrect: " + str(expected_result) + " != " + str(actual_result)
    return print_text


if __name__ == "__main__":
    # Try it on these to see if it works?
    text0 = "My foot is a hamburger"
    text1 = "Go hang a salami Im a lasagna hog"
    text2 = "She sells sea shells by the sea shore"
    text3 = "race car"

    # Test it like this
    print(tester(text0, False))
    print(tester(text1, True))
