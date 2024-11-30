# Iterating Over Structured Data

### Unpacking Data in Tuples
When iterating over lists of tuples, you can **unpack multiple variables** in the loop.

```python
coords = [(0, 1), (1, 2), (2, 3)]

for x, y in coords:
    print("Coordinate: (" + str(x) + ", " + str(y) + ")")
```

#### Output
```
Coordinate: (0, 1)
Coordinate: (1, 2)
Coordinate: (2, 3)
```

---

### Enumerating Collections
Use `enumerate()` to loop through a list and get **both the index and the value**.

```python
materials = ["Concrete", "Steel", "Timber"]

for index, material in enumerate(materials):
    print(str(index) + ": " + material)
```

#### Output
```
0: Concrete
1: Steel
2: Timber
```

---

### Combining Lists with `zip()`
The `zip()` function combines multiple lists and allows iteration over their elements in parallel.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(name + ": " + str(score))
```

#### Output
```
Alice: 85
Bob: 92
Charlie: 78
```
