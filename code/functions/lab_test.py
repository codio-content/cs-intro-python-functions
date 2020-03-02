# Import student function form the newly copied file
from lab_challenge import to_upper

# Import system module
import sys

# Homemade unit test, call student function w/ instructor input & output
def test_student_code():
    """Homemade unit test for student work
    Return True if all of the tests pass
    Return False if at least one test fails"""
    
    # Boolean variables for each test
    test1 = False
    
    # First test case
    if to_upper("hello") == "HELLO":
        test1 = True
        print(to_upper("hello"))
    else:
        print("Test did not pass.")
    
    # Return results of the unit tests
    if test1:
        return True
    else:
        return False

# Print final results of the unit test
if test_student_code():
    print("Well done!")
    sys.exit(0)
else:
    print("Looks like your code needs some work")
    sys.exit(1)