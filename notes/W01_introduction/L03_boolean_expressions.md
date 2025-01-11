# Boolean Expressions in Python
Boolean expressions are evaluated to either **True** or **False**. In Python, we use these expressions to make logical comparisons or combine multiple conditions. Boolean expressions are essential for decision-making in programming and are the basis for more complex control structures.

---

### Comparison Operators
Comparison operators are used to compare two values and produce a boolean result (`True` or `False`). These operators are useful for checking relationships between values, such as equality, inequality, and ordering.

#### Common Comparison Operators
- **`==`**: Equal to
- **`!=`**: Not equal to
- **`>`**: Greater than
- **`<`**: Less than
- **`>=`**: Greater than or equal to
- **`<=`**: Less than or equal to

```python
# Equality and Inequality
5 == 5       # True
3 != 4       # True
3 == 4       # False

# Greater than / Less than
10 > 7       # True
2 < 3        # True
4 >= 4       # True
6 <= 5       # False
```

Each of these expressions compares two values and returns `True` or `False` based on the outcome of the comparison.

---

### Logical Operators
Logical operators allow us to combine multiple boolean expressions to form more complex conditions. These operators help us check if **multiple conditions** are true or false simultaneously.

#### Common Logical Operators
- **`and`**: Returns `True` only if **both** expressions are `True`
- **`or`**: Returns `True` if **at least one** of the expressions is `True`
- **`not`**: Returns the opposite boolean value of an expression (`True` becomes `False`, and `False` becomes `True`)

```python
# Using 'and' to check two conditions
5 > 3 and 10 > 7       # True, both conditions are true
5 > 3 and 10 < 7       # False, the second condition is false

# Using 'or' to check at least one condition
5 > 3 or 10 < 7        # True, at least one condition is true
5 < 3 or 10 < 7        # False, both conditions are false

# Using 'not' to invert a boolean value
not (5 > 3)            # False, since 5 > 3 is True, but 'not' inverts it
not (5 < 3)            # True, since 5 < 3 is False, but 'not' makes it True
```

Logical operators allow us to combine expressions, enabling more nuanced boolean checks. For instance, we might want to check if two values are within a range, or if a certain condition does not hold.

---

### Combining Comparison and Logical Operators
By combining comparison and logical operators, we can evaluate multiple conditions in one expression.

```python
age = 25
is_adult = age >= 18 and age < 65  # True if age is between 18 and 64

temperature = 75
is_moderate = temperature > 60 and temperature < 80  # True if temperature is moderate

height = 170
valid_height = height > 150 or height < 200  # True if height is outside range of 150 to 200

# Using 'not' with a combined expression
not_in_range = not (10 < 20 and 20 < 30)  # False, since both conditions are true
```

---

### Boolean Values and Expressions as Variables
Boolean values (`True` and `False`) can be stored in variables, making expressions reusable and more readable.

```python
is_sunny = True
is_warm = False

# Combining stored boolean values
go_outside = is_sunny and is_warm  # False, because only one condition is True

# Assigning a comparison to a variable
score = 85
passing = score >= 60
print(passing)       # True, because 85 is greater than or equal to 60
```

Storing boolean values in variables can simplify expressions, especially when they are used repeatedly. This approach also improves readability by making the conditions clearer.

---

### Summary
Boolean expressions are used to evaluate conditions and return either `True` or `False`. They are foundational in programming for making decisions and combining logical statements. Here’s a quick summary:
   - **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
   - **Logical Operators**: `and`, `or`, `not`
   - **Combining Expressions**: You can combine comparisons using logical operators to evaluate multiple conditions at once.

Boolean expressions are used in nearly all programming scenarios, from checking if a value meets certain criteria to combining multiple conditions for complex checks.
