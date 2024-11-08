### Casting (Type Conversion)
- **Definition**: Casting is the process of converting a variable from one type to another using specific functions.
- **Common Cast Functions**: 
  - `int()` – Converts to integer
  - `float()` – Converts to float
  - `str()` – Converts to string
  - `bool()` – Converts to boolean

#### Examples
- **Integer to String**:
  ```python
  age = 25
  age_str = str(age)  # Converts to "25"
  ```
- **Integer to Float**:
  ```python
  age_float = float(age)  # Converts to 25.0
  ```
- **Caution on Truncation**: Converting a float to an integer removes the decimal part, known as truncation (not rounding).
  ```python
  height = 5.9167
  height_int = int(height)  # Results in 5
  ```
- **Errors in Casting**: Attempting to convert incompatible strings to numbers will raise a `ValueError`.
  ```python
  num_str = "6.023x10^23"
  num = float(num_str)  # Raises a ValueError
  ```
