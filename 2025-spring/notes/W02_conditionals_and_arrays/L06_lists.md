# Arrays and Lists

### What Are Arrays?

#### Definition
- An array is a data structure that stores multiple elements in a single, **ordered collection**.
- Arrays are efficient for memory usage, provide indexed access to elements, and typically contain values of the same type.

#### Lists in Python
Python’s `list` is a flexible and dynamic data type similar to arrays but supports mixed data types and variable sizes.

```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "apple", True]
```

#### Why Use Lists?
- Lists are versatile and easy to manipulate, making them a great starting point for learning data structures.
- Lists support operations like appending, removing, and slicing, which we’ll explore in later sections.

---

### Accessing List Elements

#### Zero-Based Indexing
- Python uses zero-based indexing, meaning the first element of the list has an index of `0`.
- **Negative Indices:** allow you to access elements from the end of the list, where `-1` is the last element.
- **IndexError:** Accessing an index outside the valid range raises an `IndexError`.

```python
fruits = ["apple", "banana", "cherry", "orange"]

print(fruits[0])   # Output: apple
print(fruits[2])   # Output: cherry
print(fruits[-1])  # Output: orange
print(fruits[4])   # Raises IndexError (list has only 4 elements)
```

---

### List Slicing
- **Definition:** Slicing allows you to access a subset of a list using the syntax `list[start:end]`.
- **Inclusive Start, Exclusive End:** The start index is **inclusive**, and the end index is **exclusive**.

#### Omitted Indices
  - Leaving out the start index defaults to `0`.
  - Leaving out the end index defaults to the end of the list.

```python
fruits = ["apple", "banana", "cherry", "orange"]

print(fruits[1:3])  # Output: ['banana', 'cherry']
print(fruits[:2])   # Output: ['apple', 'banana']
print(fruits[2:])   # Output: ['cherry', 'orange']
```

#### Additional Notes
- **Using Steps:**
  - You can add a third argument to the slice syntax to specify a step.
  - Example:
    ```python
    print(fruits[::2])  # Output: ['apple', 'cherry']
    print(fruits[::-1])  # Output: ['orange', 'cherry', 'banana', 'apple'] (reverses the list)
    ```
- **Practical Tip:** Slicing doesn’t modify the original list. It creates a **new list** with the selected elements.

---

### Simple List Operations
- **Concatenation (`+`):**
  - Combine two lists into one.
    ```python
    combined_list = [1, 2, 3] + [4, 5, 6]
    print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]
    ```

- **Repetition (`*`):**
  - Repeat a list multiple times.
    ```python
    numbers = [1, 2, 3] * 3
    print(numbers)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
    ```

- **Equality Comparison (`==`):**
  - Check if two lists are equal in content and order.
    ```python
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [3, 2, 1]
    print(list1 == list2)  # Output: True
    print(list1 == list3)  # Output: False
    ```
---

### Tips and Additional Considerations

1. **Dynamic Nature of Lists:** Lists in Python can grow or shrink dynamically

2. **Index Ranges and Edge Cases:** Accessing an out-of-range index raises an error, but slicing with an out-of-range end index doesn’t:
   ```python
   print(fruits[10:])  # Output: []
   ```

3. **Immutability:** Unlike tuples, lists are mutable, meaning you can modify them directly.
     ```python
     fruits[1] = "blueberry"
     print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
     ```
