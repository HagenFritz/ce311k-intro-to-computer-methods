# Casting (Type Conversion)
- **Definition**: Casting is the process of converting a variable from one data type to another using specific functions.
- **Common Cast Functions**: 
  - `int()` – Converts to an integer
  - `float()` – Converts to a float (decimal)
  - `str()` – Converts to a string
  - `bool()` – Converts to a boolean (`True` or `False`)

### Examples
- **Integer to String**:
  ```python
  age = 25
  age_str = str(age)  # Converts to "25" (a string)
  ```
- **Integer to Float**:
  ```python
  age_float = float(age)  # Converts to 25.0 (a float)
  ```
- **String to Integer**:
  ```python
  year = "2023"
  year_int = int(year)  # Converts "2023" to 2023 (an integer)
  ```
- **Boolean to Integer**:
  ```python
  is_active = True
  is_active_int = int(is_active)  # Converts True to 1
  ```

---

### Cautions with Casting

#### Truncation Versus Rounding
- **Truncation with `int()`**: Converting a float to an integer using `int()` will remove the decimal part (it does not round).
  ```python
  price = 5.99
  price_int = int(price)  # Results in 5, not 6
  ```
- **Rounding Before Casting**: If you want to round to the nearest integer, use `round()` first, then cast.
  ```python
  price_rounded = round(price)  # Results in 6
  ```

#### Conversion Errors
- **Avoiding `ValueError`**: Trying to cast incompatible strings (e.g., containing letters or special characters) to numbers will raise a `ValueError`.
  ```python
  num_str = "123abc"
  num = int(num_str)  # Raises ValueError because "123abc" is not a valid integer
  ```

This addition gives students a comprehensive overview of casting, with helpful examples and common issues to watch out for.
