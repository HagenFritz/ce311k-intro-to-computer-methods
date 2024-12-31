# Lists as Objects
Lists in Python are versatile and mutable objects used to store collections of items. Because they are objects, lists come with various methods to add, remove, or manipulate elements, making them an essential data type.

### Attributes of Lists
- Lists are **mutable**, meaning their contents can be changed after creation.
- Lists do not have fixed sizes, allowing dynamic addition or removal of elements.
- Elements in a list can be of different data types.

### Exploring List Behavior

1. **Mutability**
   Lists can be modified directly by adding, removing, or altering their elements.

   ```python
   fruits = ["apple", "banana", "cherry"]
   fruits[1] = "blueberry"
   print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
   ```

2. **Iterability**
   Lists are iterable, meaning you can loop through each element.

   ```python
   numbers = [1, 2, 3, 4]
   for num in numbers:
       print(num)
   # Output:
   # 1
   # 2
   # 3
   # 4
   ```

3. **Indexing and Slicing**
   Lists support zero-based indexing and slicing to access or modify specific elements or subsets of elements.

   ```python
   fruits = ["apple", "banana", "cherry", "date"]
   print(fruits[0])    # Output: apple
   print(fruits[-1])   # Output: date
   print(fruits[1:3])  # Output: ['banana', 'cherry']
   ```

### Working with Methods
List methods provide a variety of tools for managing and manipulating lists.

```python
numbers = [3, 1, 4, 1, 5]

# Add elements
numbers.append(9)
print(numbers)  # Output: [3, 1, 4, 1, 5, 9]

# Sort the list
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

# Remove an element
numbers.pop(2)
print(numbers)  # Output: [1, 1, 4, 5, 9]
```

### Common List Methods

#### `append(item)`
Adds an item to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

#### `extend(iterable)`
Adds all elements of an iterable (e.g., another list) to the end of the list.

```python
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
```

#### `insert(index, item)`
Inserts an item at the specified index.

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

#### `remove(item)`
Removes the first occurrence of the specified item.

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']
```

#### `pop(index)`
Removes and returns the item at the specified index. If no index is specified, removes the last item.

```python
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print(last_fruit)  # Output: cherry
print(fruits)      # Output: ['apple', 'banana']
```

#### `sort()`
Sorts the elements of the list in ascending order (by default).

```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5]
```

#### `reverse()`
Reverses the order of the elements in the list.

```python
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # Output: [3, 2, 1]
```

#### `count(item)`
Returns the number of occurrences of the specified item.

```python
numbers = [1, 2, 2, 3]
print(numbers.count(2))  # Output: 2
```

#### `index(item)`
Returns the index of the first occurrence of the specified item.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # Output: 1
```

#### `copy()`
To avoid modifying the original list when creating a copy, use slicing or the `copy()` method.

 ```python
 original = [1, 2, 3]
 copy = original.copy()
 copy.append(4)
 print(original)  # Output: [1, 2, 3]
 print(copy)      # Output: [1, 2, 3, 4]
 ```
