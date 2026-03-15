# For Loops

### Definition
- A `for` loop is used to iterate over a sequence of elements, such as a list, tuple, string, or range.
- Often expressed as: "Do this for each item in the sequence."
- Unlike `while` loops, `for` loops iterate over predefined sequences, so they cannot run infinitely

### Syntax
```python
for variable in sequence:
    # Code to execute
```

- **`variable`**: Represents the current item in the sequence during each iteration.
- **`sequence`**: The collection of items (e.g., list, range, or string) that the loop will iterate through.
- The loop ends once all items in the sequence are processed.

---

### Using the `range()` Function
`for` loops often use iterators like `range()` to generate a sequence of numbers.

```python
for i in range(5):
    print("Iteration:", i)
```

#### Output
```
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
```

#### Explanation
1. `range(5)` generates numbers from `0` to `4`.
2. Each number is assigned to the variable `i` during each iteration.
3. The loop runs for each value in the range.

---

### Iterating Through Collections
`for` loops are commonly used to iterate over elements in a collection using the `in` keyword.

```python
elements = ['a', 'b', 'c']

for element in elements:
    print(element)
```

#### Output
```
a
b
c
```

**Explanation**:
- The loop assigns each element from the list `['a', 'b', 'c']` to the variable `element` during each iteration.
- The loop finishes after reaching the last element.

---

### Practical Example: Calculating Cumulative Load
Iterate through a list of load values and calculate the cumulative load on a beam.

```python
loads = [100, 200, 150, 300]
total_load = 0

for load in loads:
    total_load += load  # Add each load to the total
    print("Current Total Load:", total_load)
```

#### Output
```
Current Total Load: 100
Current Total Load: 300
Current Total Load: 450
Current Total Load: 750
```

---

### Common Use Cases of For Loops
1. **Processing Collections**: Iterate over lists, tuples, or strings to process each item.
   ```python
   names = ["Alice", "Bob", "Charlie"]
   for name in names:
       print(f"Hello, {name}!")
   ```

2. **Working with Numbers**: Use `range()` to perform repetitive tasks a fixed number of times.
   ```python
   for i in range(3):
       print("This is loop number", i)
   ```

4. **Simulating Processes**: Calculate cumulative values (e.g., total costs, loads).
