# Strings as Objects
Strings in Python are a fundamental and immutable data type used for storing and manipulating text. Because they are objects, they come with a variety of built-in methods to simplify common operations such as formatting, searching, and transforming text.

### Attributes of Strings
- Strings do not have mutable attributes since they are immutable.
- However, you can use **methods** to perform various operations on strings and return new string objects without altering the original.

### Exploring String Behavior

1. **Immutability**
   - Strings cannot be modified after they are created, meaning that operations on strings always result in a new string.
   
   ```python
   text = "hello"
   new_text = text.upper()
   print(text)      # Output: hello (unchanged)
   print(new_text)  # Output: HELLO
   ```

2. **Iterability**
   Strings are iterable, meaning you can loop through each character.
   
   ```python
   for char in "Python":
       print(char)
   # Output:
   # P
   # y
   # t
   # h
   # o
   # n
   ```

3. **Indexing and Slicing**
   Strings support zero-based indexing and slicing to access specific characters or substrings.
   
   ```python
   text = "Python"
   print(text[0])    # Output: P
   print(text[-1])   # Output: n
   print(text[1:4])  # Output: yth
   ```

### Working with Methods
String methods are functions that are called on string objects to perform specific tasks.

```python
text = "   Python is FUN!   "
processed = text.strip().lower().replace("fun", "awesome")
print(processed)  # Output: python is awesome!
```

### Common String Methods

#### `.upper()`
Converts all characters in the string to uppercase.

```python
text = "hello"
print(text.upper())  # Output: "HELLO"
```

#### `.lower()`
Converts all characters in the string to lowercase.

```python
text = "HELLO"
print(text.lower())  # Output: "hello"
```

#### `.strip()`
Removes leading and trailing whitespace (or specified characters).

```python
text = "   hello   "
print(text.strip())  # Output: "hello"
```

#### `.replace(old, new)`
Replaces all occurrences of `old` substring with `new`.

```python
text = "I like cats"
print(text.replace("cats", "dogs"))  # Output: "I like dogs"
```

#### `.split(separator)`
Splits the string into a list of substrings based on the given separator (default is whitespace).

```python
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']
```

#### `.join(iterable)`
Joins elements of an iterable (e.g., list) into a single string, using the string as a separator.

```python
fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))  # Output: "apple, banana, cherry"
```

#### `.find(substring)`
Returns the lowest index where the substring is found; returns `-1` if not found.

```python
text = "hello world"
print(text.find("world"))  # Output: 6
print(text.find("Python"))  # Output: -1
```

#### `.count(substring)`
Returns the number of occurrences of a substring.

```python
text = "banana"
print(text.count("a"))  # Output: 3
```

#### `.startswith(prefix)` / `.endswith(suffix)`
Checks if the string starts or ends with the specified prefix or suffix.

```python
text = "hello world"
print(text.startswith("hello"))  # Output: True
print(text.endswith("world"))    # Output: True
```

#### `.capitalize()`
Capitalizes the first character of the string.

```python
text = "hello world"
print(text.capitalize())  # Output: "Hello world"
```

#### `.title()`
Converts the string to title case (first letter of each word capitalized).

```python
text = "hello world"
print(text.title())  # Output: "Hello World"
```

#### `.isnumeric()` / `.isdigit()`
Checks if all characters in the string are numeric.

```python
text = "12345"
print(text.isnumeric())  # Output: True
print("123abc".isnumeric())  # Output: False
```
