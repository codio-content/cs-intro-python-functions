----------

## Helper Functions

Well written functions are those with a single, specific task. Complex problems will require more than one function for the solution. Helper functions are functions that are called from within other functions. Take, for example, the formula for calculating the area of a circle:
$$A = \pi r^2$$

It would be quite easy to write a Python function to calculate the area of a circle. However, instead of knowing the radius of the circle, you have the X/Y coordinates for a point at the center of the circle and another point on the circle. The distance formula (which is based on the Pythagorean Theorem) can calculate the radius of the circle.
$$\sqrt{(x2 - x1)^2 + (y2 - y1)^2}$$

![Radius](.guides/images/radius.png)

The area function is dependent upon the distance formula. This is where helper functions come into play. Start by defining a function `radius`. The square root function is included in the `math` module. Be sure to import `math` in your program. Then define a function `area` which calls `radius`. Since `area` requires `radius`, `area` also requires all of the parameters needed for the `radius` function. Finally, print the result of the area of a circle with the points (0, 0) and (4, 4).

```python
import math

def radius(x1, y1, x2, y2):
    """Distance formula to determine the radius of a circle"""
    return(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
  
def area(x1, y1, x2, y2):
    """Area of a circle function"""
    return(math.pi * radius(x1, y1, x2, y2)**2)

print(area(0, 0, 4, 4))
```

{try it}(python3 code/functions/helper-functions.py 1)

|||challenge
## Another way to do powers
Another way to do powers is to use `math.pow`. This function has two arguments, the base and the exponent. So `3 ** 2` becomes `math.pow(3, 2)`. Rewrite the `return` statements for the two functions above using `math.pow`.

<details>
  <summary><strong>Solution</strong></summary>
  The new return statements are:
  
  ```python
  return(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)))
  ```
  
  and 
  
  ```python
  return(math.pi * math.pow(radius(x1, y1, x2, y2), 2))
  ```
  
</details>

|||

{try it}(python3 code/functions/helper-functions.py 2)

## Inner Functions

Python allows you to declare a function inside another function. Doing this hides the inner function from the main program. In the code below, only the `area` function can call the `radius` function. 

```python
import math
  
def area(x1, y1, x2, y2):
    """Area of a circle function"""
    def radius(x1, y1, x2, y2):
        """Distance formula to determine the radius of a circle"""
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    
    return(math.pi * math.pow(radius(x1, y1, x2, y2), 2))
  
print(area(0, 0, 4, 4))
```

{try it}(python3 code/functions/helper-functions.py 3)

|||challenge
## What happens if you:
Try to call the `radius` function from your program?

```python
print(radius(0, 0, 4, 4))
```

<details>
  <summary><strong>Why does this cause an error?</strong></summary>
  Just as variables have scope, so do functions. The Python program cannot "see" inside the <code>area</code> function, so it cannot call the <code>radius</code> function. That is why your code produces the error <code>NameError: name 'radius' is not defined</code>.
</details>

|||

{try it}(python3 code/functions/helper-functions.py 4)

{Check It!|assessment}(multiple-choice-1330281496)
