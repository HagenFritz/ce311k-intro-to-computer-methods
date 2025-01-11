# While Loops

### Definition
- A `while` loop repeats a block of code as long as a condition is true.
- Commonly used when the number of repetitions is not predetermined.
- Often expressed as: "Keep doing this until...".

### Syntax
```python
while condition:
    # Code to execute
    # Make sure the condition changes eventually!
```

- **Condition:** The loop will keep running as long as this evaluates to `True`.
- **Indented Block:** All code under the loop must be indented (Python requires indentation for block structures).

---

### Using a Counter Variable
`while` loops often require a **counter variable** to control the number of iterations.

```python
count = 0  # Counter variable
while count < 5:
    print("Count is:", count)
    count += 1  # Increment the counter
```

#### Output
```
Count is: 0
Count is: 1
Count is: 2
Count is: 3
Count is: 4
```

#### Explanation
1. The `count` variable starts at `0`.
2. The loop checks if `count < 5` before each iteration.
3. The `count` is incremented (`count += 1`) to avoid an infinite loop.
4. Once `count` becomes a value of 5, the condition is no longer true and the loop is broken

---

### Boolean Conditions in While Loops
- The condition in a `while` loop can be any Boolean expression.
- You can combine multiple conditions using logical operators like `and`, `or`, and `not`.

```python
temperature = 75
is_humid = True

while temperature < 80 and is_humid:
    print("It's too humid!")
    temperature += 2  # Simulate temperature rising
```

---

### **Infinite Loops**
- A `while` loop runs indefinitely if its condition never becomes `False`.
- Common mistake: Forgetting to modify the condition inside the loop.

```python
while True:
    print("This will run forever!")  # Use Ctrl+C to stop
```

#### Avoiding Infinite Loops
1. Always include a way to modify the condition (e.g., increment a counter).
2. Double-check your logic before running.

---

### Use Cases of While Loops
1. **Condition-Based Iteration:**
   - Repeat a task until a specific condition is met.
   - Example: Simulating a water tank filling until it reaches capacity.

2. **Input Validation:** Repeatedly prompt the user until valid input is provided.
   ```python
   user_input = ""
   while user_input.lower() != "yes":
       user_input = input("Do you want to continue? (yes/no): ")
   print("Thank you for continuing!")
   ```

3. **Simulation:** Simulate real-world processes where the number of iterations is not known upfront (e.g., temperature changes).

---

### Example Problem: Simulating Beam Loads
Write a `while` loop to incrementally add loads to a beam until it reaches the maximum allowable load.

```python
current_load = 0
max_load = 1000

while current_load < max_load:
    print("Current Load:", current_load)
    current_load += 100  # Increment by 100
```

**Output:**
```
Current Load: 0
Current Load: 100
...
Current Load: 900
```
