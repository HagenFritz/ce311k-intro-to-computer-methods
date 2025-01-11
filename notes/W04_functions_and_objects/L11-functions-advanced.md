# Advanced Function Topics

### Docstrings
- A docstring is a multiline string that appears immediately below the function definition.
- It is used to document the purpose, parameters, and return value of a function.
- Helpful for improving code readability and understanding.

```python
def greet(name):
    """
    Greet a person by their name.

    Parameters:
        name (str): The name of the person to greet.

    Returns:
        str: A personalized greeting message.
    """
    return f"Hello, {name}!"
```

---

### Default Parameters
- Default parameters allow you to set a default value for a parameter in a function.
- These parameters become optional when calling the function; the default value is used if no argument is provided.

#### Rules for Default Parameters
1. Parameters with default values **must appear after** parameters without default values in the function definition.
   ```python
   # Correct:
   def example(a, b=10):
       return a + b

   # Incorrect:
   def example(a=10, b):  # SyntaxError
       return a + b
   ```
2. Default parameters are evaluated once when the function is defined, not each time the function is called.

#### Examples: Default Parameters
```python
def calculate_total(price, fee=10, tax=0.05):
    """Calculate the total price including tax."""
    return price * (1+tax) + fee

# Using the default fee and tax rate
total_price = calculate_total(100)  # 115.0

# Overriding the default tax rate but not fee
price_high_tax = calculate_total(100, tax=0.08)  # 118.0

# Overriding the default fee but not tax rate
price_high_fee = calculate_total(100, fee=25)  # 130.0

# Overrding both default parameters
price_high = calculate_total(100, fee=25, tax_rate=0.08)  # 132.0
```

---

### Nested Functions
- A function defined inside another function is called a nested function.
- Useful for encapsulating logic or creating closures.
- The inner function can only be accessed from within the outer function.

```python
def outer_function(params_outer):
    # initial logic/processing

    def inner_function(params_inner):
        # inner function logic/processing
        return value
    
    # Call the inner function now that it is defined
    result = inner_function(arguments)

    # additional logic/processing
    return result
```

#### Example: Nested Functions
```python
def outer_function(message):
    """Outer function that defines an inner function."""
    message_with_intro = "Hello. " + message

    def inner_function(message):
        message_with_outro = message + " Goodbye."
        return message_with_outro

    total_message = inner_function(message_with_intro)
    return total_message

print(outer_function("How are you?"))  # Output: Hello. How are you? Goodbye.
```

#### Benefits of Nested Functions
1. Logical grouping of code for better readability.
2. The inner function can access variables from the outer function's scope (closure).
3. Avoids polluting the global namespace with helper functions.
