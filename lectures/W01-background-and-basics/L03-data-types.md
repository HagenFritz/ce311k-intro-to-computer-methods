# Data Types

### Variables and Data Types
- **Variables** store data, while **Data Types** specify what kind of data is stored.
- Python uses **Dynamic Typing**, meaning you don’t need to declare data types explicitly. However, this can sometimes lead to `TypeError` if incompatible types are mixed.

---

### Integer (`int`)
- **Definition**: Integers are whole numbers, including negative numbers, zero, and positive numbers.
- **Examples**:
  ```python
  i = 0
  y = -10
  age = 31
  ```
- **Common Use**: Integers are used for counting, indexing, and representing whole values.
- **Note**: In some programming languages, there are variations like "short" or "long" integers, but Python’s `int` type automatically manages size.

---

### Float (`float`)
- **Definition**: Floats are numbers that contain decimal points, providing precision.
- **Examples**:
  ```python
  pi = 3.14159
  temperature = -7.3
  ```
- **Common Use**: Floats are useful in scientific and engineering calculations, especially when precision is important (e.g., measurements, prices).
- **Note**: In other languages, "double" is often used to represent high-precision floats, but Python uses `float` for all decimal numbers.

---

### String (`str`)
- **Definition**: Strings are sequences of characters, including letters, numbers, and symbols.
- **Syntax**: Strings can be enclosed in either single or double quotes.
- **Examples**:
  ```python
  name = "Fritz, Hagen"
  email = "HagenFritz@utexas.edu"
  eid = "hef372"
  phrase = "It's up to you!"
  ```
- **Escape Characters**: Special sequences starting with a backslash (`\`) allow for characters like tabs (`\t`) and new lines (`\n`).
  ```python
  sentence = "He said,\t\"Whoa! Did you see that?\"\n"
  ```
- **Multiline Strings**: Defined using triple quotes and span multiple lines.
  ```python
  multiline = """This is a
  multiline string."""
  ```

---

### Boolean (`bool`)
- **Definition**: Booleans represent truth values, such as `True` or `False`.
- **Examples**:
  ```python
  flag = True
  active = False
  ```
- **Use in Program Flow**: Booleans are essential in conditions and control structures (e.g., if statements).
- **Alternative Values**: `True` is often equivalent to `1` and `False` to `0` in calculations.
