# Arithmetic Expressions in Python

### Basic Arithmetic Operations
In Python, you can perform basic arithmetic operations using the following symbols:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`), which returns a float result even if dividing two integers
- Exponentiation (`**`) to raise numbers to a power
- Floor Division (`//`), which returns the largest integer less than or equal to the result
- Modulus (`%`) to get the remainder of a division operation

```python
a = 10
b = 3

add = a + b        # 13
subtract = a - b   # 7
multiply = a * b   # 30
divide = a / b     # 3.3333333333333335
exponent = a ** b  # 1000
floor_div = a // b # 3
modulus = a % b    # 1
```

### Order of Operations (PEMDAS)
Python follows the standard order of operations, often remembered by the acronym **PEMDAS**:
- **P**arentheses: `()`
- **E**xponents: `**`
- **M**ultiplication and **D**ivision: `*`, `/`, `//`, `%` (from left to right)
- **A**ddition and **S**ubtraction: `+`, `-` (from left to right)

```python
result = 3 + 5 * 2  # 13, not 16 (multiplication before addition)
result = (3 + 5) * 2  # 16 (parentheses first)
result = 2 ** 3 + 1  # 9 (exponent before addition)
result = 4 * (2 + 1) ** 2  # 36 (parentheses and exponent first, then multiply)
```

- Using parentheses to group parts of expressions can help clarify the intended calculation order and make complex expressions easier to understand.

### Implicit Casting
When combining integers and floating-point numbers in Python, **implicit casting** (or type conversion) occurs automatically. This means that:
- If you mix `int` and `float` values in an expression, Python will automatically convert the `int` to a `float` to avoid losing precision.

```python
result = 7 + 3.5      # 10.5, result is a float
result = 10 / 2       # 5.0, even though both operands are integers, result is a float
result = 5 + 2        # 7, both operands are integers, result is an integer
```

### Compound Assignment Operators
Python allows **compound assignment** operators to make updating variables more concise. These operators modify and reassign a variable in a single line:
- `+=`, `-=`, `*=`, `/=`, `//=`, and `%=`

```python
total = 10
total += 5    # total = total + 5, so total is now 15
total *= 2    # total = total * 2, so total is now 30
```

### Integer Division vs. Float Division

- **Float Division (`/`)**: The standard division operator always returns a float, even when dividing two integers.
- **Integer (or Floor) Division (`//`)**: This operator divides and rounds down to the nearest whole number, returning an integer result.

**Examples:**
```python
result = 7 / 2    # 3.5 (float division)
result = 7 // 2   # 3 (integer division)
```

### Modulus Operator
The **modulus operator** (`%`) returns the remainder of a division operation. It’s useful for checking divisibility or determining if a number is even or odd.

```python
remainder = 10 % 3   # 1, because 10 divided by 3 leaves a remainder of 1
is_even = 10 % 2 == 0  # True, because 10 is evenly divisible by 2
```

---

### Summary

Understanding arithmetic expressions in Python enables you to perform calculations and create more advanced logic in your code. Here’s a quick recap:
   - **Basic Operations**: `+`, `-`, `*`, `/`, `//`, `**`, `%`
   - **PEMDAS** for order of operations, with parentheses to clarify or adjust order
   - **Implicit Casting** when mixing `int` and `float`
   - **Compound Operators** like `+=` and `*=`
   - **Integer Division** (`//`) vs. **Float Division** (`/`)
   - **Modulus Operator** for remainders and divisibility checks

