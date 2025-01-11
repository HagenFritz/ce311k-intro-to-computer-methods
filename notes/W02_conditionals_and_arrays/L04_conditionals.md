# Conditionals

### Basics
- **Conditionals:** Allow you to execute certain blocks of code only when specific conditions are true.
- **Boolean Expressions:** These evaluate to either `True` or `False`. The result determines whether the code inside a conditional block runs.
  - Example: `temperature > 80.0` returns `True` if `temperature` is greater than 80.

#### Important Points
1. **`if` Statement**
   - Used to specify a block of code that runs only if a condition evaluates to `True`.
   - Example:
     ```python
     temperature = 75.0
     if temperature > 80.0:
         print("It's warm!")
     ```

2. **Indentation in Python**
   - Python uses **indentation** (not brackets or keywords) to define blocks of code.
   - The code inside an `if` statement must be indented, or Python will throw an error.
   - Example:
     ```python
     if temperature > 80.0:
         print("It's warm!")  # Correct
     print("This runs regardless.")  # Runs no matter the condition
     ```

3. **Execution Flow:**
   - The program checks if the condition is true. If so, it executes the indented block. After the block is complete, it continues with the next statement.

---

### Multiple Conditions
1. **`else`**
   - Provides a "catch-all" block to execute code when the `if` condition is false.
   - Example:
     ```python
     humidity = 0.9
     if humidity > 0.95:
         print("It is probably raining")
     else:
         print("It is likely not raining")
     ```

2. **`elif`**
   - Stands for "else if." It allows you to check additional conditions when the previous conditions are false.
   - Example:
     ```python
     temperature = 70
     if temperature > 75:
         print("It is warm!")
     elif temperature > 65:
         print("It is pleasant!")
     else:
         print("It is cold")
     ```

#### Additional Notes
- Only one block of an `if-elif-else` chain will execute, even if multiple conditions are true. Python evaluates conditions in order from top to bottom.
- Good practice: Keep conditions mutually exclusive to avoid confusion.

---

### Nested Conditionals
- You can place one `if` block inside another. This is useful when multiple levels of conditions need to be checked.
- Example:
  ```python
  temperature = 80
  humidity = 0.6

  if temperature > 75:
      if humidity > 0.5:
          print("It is warm and humid")
      else:
          print("It is warm and dry")
  else:
      print("It is not warm")
  ```

#### Additional Notes
- **Readability Concerns:** Nested conditionals can get complex and hard to read. Use them sparingly or refactor into separate functions when possible.
- **Alternatives:** Sometimes, logical operators (`and`, `or`) can simplify nested conditionals:
```python
if temperature > 75 and humidity > 0.5:
    print("It is warm and humid")
```

---

### Boolean Variables and Logical Operators
Logical operators allow for more compact and readable conditions, reducing the need for deeply nested `if` statements.

1. **Boolean Variables**
   - You can assign a boolean value (`True` or `False`) to a variable and use it in conditions.
   - Example:
     ```python
     is_humid = True
     if is_humid:
         print("It is humid")
     ```

2. **Logical Operators**
   - Combine multiple conditions with `and`, `or`, and `not`.
   - **`and`:** Both conditions must be `True`.
     ```python
     if is_humid and temperature > 75:
         print("It is warm and humid")
     ```
   - **`or`:** At least one condition must be `True`.
     ```python
     day_of_week = "Sat"
     is_sun = True
     if day_of_week == "Sat" or is_sun:
         print("It is the weekend!")
     ```
   - **`not`:** Negates a condition.
     ```python
     if not is_humid:
         print("It is dry")
     ```
     
---

### Tips and Additional Considerations

1. **Testing Conditions**
   - Use print statements to debug conditions and understand which branch of code is executing.
   - Example:
     ```python
     temperature = 65
     if temperature > 75:
         print("Condition 1: Warm")
     elif temperature > 65:
         print("Condition 2: Pleasant")
     else:
         print("Condition 3: Cold")
     ```

2. **Avoid Overlapping Conditions**
   - Ensure that conditions in an `if-elif-else` chain are mutually exclusive to avoid unexpected behavior.
   - Example:
     ```python
     score = 85
     if score >= 90:
         print("Grade: A")
     elif score >= 80:  # This block won't interfere with the first
         print("Grade: B")
     ```

3. **Boolean Expressions in Variables**
   - Store conditions in variables for better readability.
   - Example:
     ```python
     is_adult = age >= 18
     if is_adult:
         print("You are an adult.")
     ```

4. **Use Comments for Complex Conditions**
   - Add comments to explain the logic behind conditions.
   - Example:
     ```python
     if day_of_week == "Sat" or day_of_week == "Sun":
         # True if it's the weekend
         print("It's the weekend!")
     ```
