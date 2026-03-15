# Type Checking with Built-In Functions: `type()` and `isinstance()`

### `type()` Function
- **Purpose**: The `type()` function returns the data type of a variable or value, making it especially useful for debugging and confirming variable types.
- **Syntax**: `type(variable)`
- **Examples**:
  ```python
  age = 25
  pi = 3.14
  name = "Alice"
  active = True

  print(type(age))     # Outputs: <class 'int'>
  print(type(pi))      # Outputs: <class 'float'>
  print(type(name))    # Outputs: <class 'str'>
  print(type(active))  # Outputs: <class 'bool'>
  ```

- **Common Use Cases**:
  - **Debugging**: Checking variable types during development can help identify unintended data type changes, which may cause runtime errors.

---

### `isinstance()` Function
- **Purpose**: The `isinstance()` function checks whether a variable is of a specified type (or types), returning `True` if it matches and `False` if not.
- **Syntax**: `isinstance(variable, type)` or `isinstance(variable, (type1, type2, ...))` for multiple types

#### Examples**
```python
score = 10
username = "player1"
completed = True

# Single type check
print(isinstance(score, int))       # Outputs: True
print(isinstance(username, float))  # Outputs: False

# Multiple types check
print(isinstance(completed, (int, bool)))  # Outputs: True
```

#### Common Use Cases
- **Type Checking in Conditional Logic**: `isinstance()` can be useful for conditionally executing code based on type. This is particularly helpful in functions that accept multiple types or handle complex data.
  ```python
  if isinstance(score, int):
      print("Score is an integer")
  elif isinstance(score, float):
      print("Score is a float")
  ```
- **Error Handling**: Use `isinstance()` to validate function arguments, raising errors if the input is of an unexpected type.
  ```python
  def process_data(data):
      if not isinstance(data, list):
          raise TypeError("Expected data to be of type list")
      # Continue processing
  ```

---

### Summary
`isinstance()` works better in conditionals as it supports type inheritance, meaning it will return `True` for subclasses as well. For example, an object of a custom class that inherits from `int` would pass an `isinstance()` check for `int`, but not necessarily a `type()` check.

| Feature           | `type()`                     | `isinstance()`                |
|-------------------|------------------------------|-------------------------------|
| **Purpose**       | Returns the exact type of a variable | Checks if a variable matches a specified type or types |
| **Syntax**        | `type(variable)`             | `isinstance(variable, type)`  |
| **Use in Inheritance** | Does not consider inheritance | Considers inheritance (e.g., subclasses) |
| **Common Use**    | Debugging, confirming data types | Type checking in conditions, function argument validation |

By understanding these functions, you can better manage variable types, debug effectively, and write more flexible code that works with different data types.
