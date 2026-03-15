# Exceptions and Error Handling

### Exceptions
- Exceptions are a subset of runtime errors that occur when something unexpected happens during program execution.
- Unlike syntax errors, exceptions are not detected until the program is run.
- They **interrupt the normal flow** of a program but can be handled to prevent crashes.

#### Common Types of Exceptions
- **`ZeroDivisionError`**: Dividing by zero.
  ```python
  print(10 / 0)  # Raises ZeroDivisionError
  ```
- **`ValueError`**: Passing invalid data to a function.
  ```python
  int("hello")  # Raises ValueError
  ```
- **`IndexError`**: Accessing a list element that doesn’t exist.
  ```python
  lst = [1, 2, 3]
  print(lst[5])  # Raises IndexError
  ```
- **`FileNotFoundError`**: Trying to access a file that doesn’t exist.
  ```python
  open("nonexistent.txt")  # Raises FileNotFoundError
  ```
- **`KeyError`**: Accessing a dictionary key that doesn’t exist.
  ```python
  data = {"a": 1}
  print(data["b"])  # Raises KeyError
  ```
- **`NameError`**: Using a variable that hasn’t been defined.
  ```python
  print(unknown_var)  # Raises NameError
  ```
- **`TypeError`**: Performing an operation on incompatible types.
  ```python
  print(5 + "string")  # Raises TypeError
  ```

---

### Error Handling with `try-except`
- Exception handling allows programs to **recover from errors gracefully** rather than crashing.
- Use `try-except` blocks to anticipate and handle common runtime exceptions.

#### **Basic Syntax**
```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to run if that exception occurs
```

**Example: Handling Division by Zero**
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("You can't divide by zero!")
```

**Example: Catching Multiple Exceptions**
- You can catch multiple exceptions and handle them differently.
- **`finally` Clause**: Code inside the `finally` block always runs, whether or not an exception occurred. Useful for cleanup tasks like closing files.
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
finally:
    print("Thank you for using the program.")
```

---

### Error Handling Principles

#### 1. Fail Fast Principle
- Detect and handle errors as early as possible before they propagate further.
- Validate input or check preconditions at the start to catch issues early.

**Example: Input Validation**
```python
age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age: Age cannot be negative.")
```

**Example: Checking Preconditions**
```python
if length < 0 or width < 0:
    print("Dimensions must be non-negative.")
```

#### 2. Graceful Degradation
- Allow the program to continue running in a reduced capacity rather than crashing entirely.
- Provide alternatives or fallback options for situations that might cause errors.

**Example: Using Default Settings**
```python
try:
    file = open("config.txt", "r")
    settings = file.read()
except FileNotFoundError:
    print("Configuration file not found. Using default settings.")
```

**Example: Skipping Invalid Data**
```python
data = ["10", "abc", "20", "xyz"]

for item in data:
    try:
        num = int(item)
        print("Valid number:", num)
    except ValueError:
        print(f"Skipping invalid data: {item}")
```

#### 3. Avoid Silent Failures
- Never suppress errors without logging or providing feedback.
- Always inform the user or developer about what went wrong.

**Example: Log and Provide Feedback**
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}. Cannot perform division.")
```

**Example: Handle Unexpected Issues**
```python
try:
    items = [1, 2, 3]
    print(items[5])  # Invalid index
except IndexError as e:
    print(f"Error: {e}. Index out of range.")
```

---

### Best Practices for Error Handling
1. **Write Simple Code**: Avoid writing too much code in one line or function. Break it into smaller, testable pieces.
2. **Anticipate Edge Cases**: Think about unusual scenarios, such as:
     - Dividing by zero.
     - Passing an empty list or file.
     - Receiving unexpected input from users.
