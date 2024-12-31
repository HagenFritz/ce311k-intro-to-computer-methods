# Built-in Functions in Python
Python comes with a variety of **built-in functions** that are available without the need to import any additional modules. These functions simplify common programming tasks and help make your code more efficient. They are:
- Predefined and always available.
- Aimed at common operations like type conversion, mathematical calculations, string manipulations, and more.
- Can be combined with user-defined functions for more complex logic.

---

### Commonly Used Built-in Functions

#### Type Conversion Functions
Convert data types

```python
int("42")        # Converts string to integer -> 42
float("3.14")    # Converts string to float -> 3.14
str(123)          # Converts integer to string -> '123'
bool(0)           # Converts to Boolean -> False
list("hello")    # Converts string to list -> ['h', 'e', 'l', 'l', 'o']
```

#### Input and Output Functions
- **`input()`**: Reads input from the user as a string.
  ```python
  name = input("Enter your name: ")
  print(f"Hello, {name}!")
  ```

- **`print()`**: Outputs data to the console.
  ```python
  print("Hello, World!")
  print(42, "is a number", sep=" - ")  # Output: 42 - is a number
  ```

#### Math and Numeric Functions
Perform mathematical operations.

```python
abs(-10)          # Absolute value -> 10
pow(2, 3)         # Exponentiation -> 2^3 = 8
round(3.14159, 2) # Round to 2 decimal places -> 3.14
max(1, 5, 10)     # Maximum value -> 10
min(1, 5, 10)     # Minimum value -> 1
sum([1, 2, 3])    # Sum of iterable -> 6
```

#### String Manipulation Functions
Work with strings.
```python
len("hello")          # Length of string -> 5
chr(97)                # Convert ASCII code to character -> 'a'
ord('a')               # Convert character to ASCII code -> 97
```

#### Iterable Functions
Work with lists, tuples, and other iterable objects.

```python
all([True, True, False])    # Check if all elements are True -> False
any([True, False, False])   # Check if any element is True -> True
enumerate(["a", "b", "c"]) # Get index and value pairs -> [(0, 'a'), (1, 'b'), (2, 'c')]
zip([1, 2], ["a", "b"])    # Combine iterables -> [(1, 'a'), (2, 'b')]
```

---

### Tips for Using Built-in Functions**
**Read the Documentation:** Use `help(function_name)` to understand what a function does.
```python
help(len)
```

- **Chain Functions Together:** Combine built-in functions for efficient code.
  ```python
  data = "1,2,3,4"
  numbers = list(map(int, data.split(",")))
  print(sum(numbers))  # Output: 10
  ```

- **Understand Edge Cases:** Test built-in functions with unexpected input to see how they behave.
  ```python
  print(int("42.0"))  # ValueError
  ```

---

### More Examples
1. Use `len()` to find the length of a string.
   ```python
   word = "python"
   print(len(word))          # Output: 6
   ```

2. Find the maximum and minimum of a list using `max()` and `min()`.
   ```python
   numbers = [10, 20, 30, 5, 15]
   print(max(numbers))       # Output: 30
   print(min(numbers))       # Output: 5
   ```

3. Use `zip()` to pair two lists and `list()` to convert the result to a list of tuples.
   ```python
   names = ["Alice", "Bob", "Charlie"]
   scores = [85, 90, 95]
   paired = list(zip(names, scores))
   print(paired)             # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 95)]
   ```

4. Use `input()` to get a number from the user, double it, and print the result.
   ```python
   num = int(input("Enter a number: "))
   print(num * 2)
   ```

