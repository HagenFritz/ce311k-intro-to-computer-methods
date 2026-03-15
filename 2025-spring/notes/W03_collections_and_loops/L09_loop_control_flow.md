# Control Flow in Loops

### Definition
Control flow in loops allows you to modify the behavior of a loop by:
- Exiting the loop early (`break`).
- Skipping certain iterations (`continue`).

---

### The `break` Statement

#### Definition
- The `break` keyword **immediately exits the loop**, regardless of the condition or remaining iterations.
- Commonly used when a specific condition is met, and further processing is unnecessary.

#### Syntax
```python
for item in sequence:
    if condition:
        break
```

#### Example: Stop When a Target is Found
```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        print("Found 3, stopping the loop.")
        break
    print(num)
```

#### Output
```
1
2
Found 3, stopping the loop.
```

#### Explanation
1. The loop iterates over the list of `numbers`.
2. When `num == 3`, the `break` statement exits the loop.
3. Any remaining iterations after the `break` are skipped.

---

### The `continue` Statement

#### Definition
- The `continue` keyword **skips the rest of the code in the current iteration** and moves to the next iteration.
- Useful for **bypassing specific conditions** without breaking out of the loop.

#### Syntax
```python
for item in sequence:
    if condition:
        continue
```

#### Example
```python
for i in range(5):
    if i % 2 == 1:
        continue  # Skip odd numbers
    print(i)
```

#### Output
```
0
2
4
```

#### Explanation
1. The loop iterates through `0` to `4`.
2. If `i` is odd (`i % 2 == 1`), the `continue` statement skips the `print()` line for that iteration.
3. The loop moves to the next value of `i`.

---

### Comparison of `break` and `continue`

| Keyword     | Behavior                                                                 | Use Case Example                     |
|-------------|--------------------------------------------------------------------------|--------------------------------------|
| `break`     | Exits the loop immediately, skipping all remaining iterations.           | Stop searching once a value is found.|
| `continue`  | Skips the current iteration and moves to the next one.                   | Skip invalid or unwanted inputs.     |

---

### Advanced Example: Combining `break` and `continue`
**Problem**: Find the first even number greater than 10 and stop. If no such number exists, print a message.

```python
numbers = [1, 3, 7, 9, 11, 14, 15]

for num in numbers:
    if num <= 10:
        continue  # Skip numbers <= 10
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
```

#### Output
```
Found even number: 14
```
