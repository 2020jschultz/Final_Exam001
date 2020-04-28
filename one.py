""" Pallendrome Checker 
    For this first problem fix the function
    so that if the input text is a pallendrome, it returns True.
    And if not, it returns false.

    Try running it on some samples to make sure it works
"""



def checkisPallendrome(text):


  result = False
  return result


# Try it on these to see if it works?
text0 = "My foot is a hamburger"
text1 = "Go hang a salami Im a lasagna hog"
text2 = "She sells sea shells by the sea shore"
text3 = "race car"

# Test it like this
print(tester(text0,False))
print(tester(text1,True))


def tester(text,expected_result):
  actual_result = checkisPallendrom(text)

  print_text = "The text was: " + str(text0)
  if expected_result == actual_result:
    print_text += "and the function was correct"
  else:
    print_text += "and the function was not correct"
  return print_text 

