# Nested Loops

### Definition
- A **nested loop** is a loop inside another loop.
- The **inner loop** runs completely for each iteration of the **outer loop**.
- Commonly used for tasks involving grids, tables, or combinations of elements.

---

### How Nested Loops Work
- The **outer loop** controls one dimension (e.g., rows).
- The **inner loop** controls another dimension (e.g., columns).

#### Example: Simple Grid of Coordinates
```python
for i in range(3):  # Outer loop for rows
    for j in range(3):  # Inner loop for columns
        print("(" + str(i) + ", " + str(j) + ")", end=" ")
    print()  # Move to the next line
```

#### Output
```
(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)
```

---

#### Example: Multiplication Table
Nested loops can calculate values for a grid, like a multiplication table.

```python
for i in range(1, 4):  # Outer loop for rows
    for j in range(1, 4):  # Inner loop for columns
        print(str(i * j), end=" ")  # Multiply row and column numbers
    print()  # Move to the next line
```

#### Output
```
1 2 3
2 4 6
3 6 9
```

---

### **Tips for Nested Loops**
1. Use clear variable names (`i`, `j`) to avoid confusion.
2. Use `print()` to debug and understand the flow of nested loops.
3. Avoid unnecessary nesting to keep code readable.
