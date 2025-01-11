# Dictionaries as Objects
Dictionaries in Python are mutable objects that store data in key-value pairs. They provide a flexible and efficient way to manage and retrieve data, making them one of the most widely used data types in Python.

### Attributes of Dictionaries
- Dictionaries are **mutable**, meaning their contents can be modified after creation.
- Keys in dictionaries must be **immutable** (e.g., strings, numbers, or tuples), while values can be of any data type.
- Dictionaries do not allow duplicate keys.

### Exploring Dictionary Behavior
1. **Mutability**
   You can add, modify, or remove key-value pairs in a dictionary.

   ```python
   person = {"name": "Alice", "age": 25}
   person["city"] = "Austin"
   print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Austin'}
   ```

2. **Iterability**
   Dictionaries are iterable, allowing you to loop through keys, values, or both.

   ```python
   data = {"name": "Bob", "age": 30, "city": "Seattle"}
   for key, value in data.items():
       print(f"{key}: {value}")
   # Output:
   # name: Bob
   # age: 30
   # city: Seattle
   ```

3. **Key-Value Pair Access**
   Access values using keys or use `.get()` to retrieve a value safely, providing a default if the key is not found.

   ```python
   person = {"name": "Alice", "age": 25}
   print(person["name"])       # Output: Alice
   print(person.get("city"))  # Output: None
   print(person.get("city", "Unknown"))  # Output: Unknown
   ```

### Working with Methods
Dictionary methods simplify common tasks such as retrieving, updating, or removing key-value pairs.

```python
inventory = {"apples": 5, "bananas": 10}

# Update the inventory
inventory["cherries"] = 15
print(inventory)  # Output: {'apples': 5, 'bananas': 10, 'cherries': 15}

# Remove an item
inventory.pop("apples")
print(inventory)  # Output: {'bananas': 10, 'cherries': 15}
```

### Common Dictionary Methods

#### `keys()`
Returns a view object containing all the keys in the dictionary.

```python
data = {"name": "Alice", "age": 25}
print(data.keys())  # Output: dict_keys(['name', 'age'])
```

#### `values()`
Returns a view object containing all the values in the dictionary.

```python
data = {"name": "Alice", "age": 25}
print(data.values())  # Output: dict_values(['Alice', 25])
```

#### `items()`
Returns a view object containing all key-value pairs as tuples.

```python
data = {"name": "Alice", "age": 25}
print(data.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])
```

#### `get(key, default)`
Returns the value for the specified key; if the key does not exist, returns the default value.

```python
data = {"name": "Alice", "age": 25}
print(data.get("city", "Unknown"))  # Output: Unknown
```

#### `update(other_dict)`
Updates the dictionary with key-value pairs from another dictionary.

```python
info = {"city": "Austin"}
data.update(info)
print(data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Austin'}
```

#### `pop(key)`
Removes and returns the value for the specified key.

```python
inventory = {"apples": 5, "bananas": 10}
count = inventory.pop("apples")
print(count)        # Output: 5
print(inventory)    # Output: {'bananas': 10}
```

#### `copy()`
Use the `copy()` method to create a shallow copy of a dictionary.

 ```python
 original = {"name": "Alice"}
 copy = original.copy()
 copy["age"] = 25
 print(original)  # Output: {'name': 'Alice'}
 print(copy)      # Output: {'name': 'Alice', 'age': 25}
 ```

#### `clear()`
Removes all key-value pairs from the dictionary.

```python
data = {"name": "Alice", "age": 25}
data.clear()
print(data)  # Output: {}
```

