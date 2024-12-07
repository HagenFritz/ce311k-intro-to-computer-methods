# Basics of Functions
**Definition:** Functions are reusable blocks of code that perform a specific task — essentially "mini-programs" within your program. They are key to structuring code effectively in Python. Functions usually take **input parameters**, perform a task, and then **return outputs**.

### Why Use Functions
- Simplify code by breaking it into smaller, logical chunks.
- Promote reusability and efficiency.
- Improve readability and maintainability.
- Facilitate easier testing and debugging.

---

### Anatomy of a Function
A function in Python consists of several key components

```python
def function_name(parameters):
    # Code block (function body)
    return value
```

### Key Parts
1. **`def`:** The keyword that indicates the start of a function.
2. **Function Name:** The name of the function follows the same rules as variable names: descriptive, no spaces, no special characters other than underscores, and cannot start with a number.
3. **Parameters (Optional):** Inputs inside parentheses.
4. **Colon (`:`):** Denotes the start of the function body.
5. **Indented Code Block:** Contains the logic of the function.
6. **`return` Statement (Optional):** Outputs the result of the function.

**Example: Simple Function**
```python
def greet(name):
    greeting = "Hello" + str(name) + "!"
    return gredting

# Using the function
print(greet("Hagen"))  # Output: Hello, Hagen!
```

---

### Calling a Function
To use a function, you call it by its name and provide arguments if required.

**Example: Adding 10 to a Number**
```python
def add_ten(x):
    total = x + 10
    return total

result = add_ten(3)
print(result)  # Output: 13
```

#### Parameters vs. Arguments
- **Parameters:** Placeholders in the function definition (e.g., `x` in `def add_ten(x):`).
- **Arguments:** The actual values you pass when calling the function (e.g., `3` in `add_ten(3)`).

---

### Scope: Variables Inside Functions
Variables created inside a function are called **local variables**, and they are only accessible within that function. This concept is known as **scope**.

### Key Points about Scope
- Variables inside a function do not interfere with variables outside the function (and vice versa).
- Once the function has finished running, its local variables are discarded.

#**Example: Local Variables**
```python
def multiply(a, b):
    result = a * b  # 'result' is local to this function
    return result

print(multiply(3, 4))  # Output: 12

# Accessing 'result' outside the function would cause an error
# print(result)  # NameError: name 'result' is not defined
```

**Example: Global vs. Local Variables**
```python
x = 10  # Global variable

def add_to_global(y):
    x = y + 5  # Local variable (different from global 'x')
    return x

print(add_to_global(3))  # Output: 8
print(x)  # Output: 10 (global 'x' is unchanged)
```

#### Best Practices
- Minimize reliance on global variables to avoid confusion and bugs.
- Use return statements to pass data out of a function instead of modifying global variables directly.

---

### Functions with Multiple Inputs
You can create functions that take more than one input.

**Example: Area of a Triangle**
```python
def calc_area_triangle(base, height):
    area = 0.5 * base * height
    return area

area = calc_area_triangle(4, 6)
print(area)  # Output: 12
```

#### Using Keyword Arguments
Keyword arguments explicitly name the parameters, improving clarity and allowing out-of-order inputs.

```python
def calc_volume(length, width, height):
    return length * width * height

# Using keyword arguments
volume = calc_volume(width=2, height=4, length=1)
print(volume)  # Output: 8
```

---

### Functions with Multiple Outputs
A function can return multiple values using tuples.

**Example: Quadratic Formula**
```python
def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None, None  # No real solutions

    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return x1, x2

# Solving x^2 - 3x + 2 = 0
x1, x2 = quadratic_formula(1, -3, 2)
print(x1, x2)  # Output: 2.0, 1.0
```

#### Unpacking Outputs
Unpacking is the process of assigning multiple return values from a function to individual variables. This makes it easier to work with each result separately.

```python
roots = quadratic_formula(1, -7, 10)
print(roots)  # Output: (5.0, 2.0)

x1, x2 = quadratic_formula(1, -7, 10)
print(f"Root 1: {x1}, Root 2: {x2}")  # Output: Root 1: 5.0, Root 2: 2.0
```

This is especially useful when the function returns multiple values, as it allows you to directly assign each value to a specific variable.

#### Another Example: Converting Temperature
Here is a function that converts a temperature from Celsius to both Fahrenheit and Kelvin

```python
def temperature_conversion(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Calling the function
fahrenheit, kelvin = temperature_conversion(25)
print(f"Fahrenheit: {fahrenheit}, Kelvin: {kelvin}")
# Output: Fahrenheit: 77.0, Kelvin: 298.15
```

#### Why Use Unpacking?
Unpacking simplifies working with functions that return multiple values by clearly associating each value with its respective variable, making code more readable and easier to debug.

