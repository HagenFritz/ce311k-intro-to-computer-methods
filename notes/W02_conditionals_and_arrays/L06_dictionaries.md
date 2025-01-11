# Dictionaries

### Definition
- A dictionary is an **unordered collection** of **key-value pairs**.
- Keys are used to uniquely identify data, and values store the associated information.
- Unlike lists, dictionaries do not maintain a fixed order.
- Keys must be immutable types (e.g., `str`, `int`, `tuple`), while values can be of any data type.
- Keys must be unique; duplicate keys will overwrite the earlier values.

---

### **Creating a Dictionary**
Dictionaries can be created using two methods:
1. **Using Curly Braces `{}`**:
   ```python
   person = {"name": "Hagen", "age": 31}
   ```

2. **Using the `dict()` Constructor**:
   ```python
   person = dict(name="Hagen", age=31)
   ```
   
---

### Accessing and Modifying Dictionaries
1. **Accessing Values**: Use the key to retrieve its associated value.
   ```python
   print(person["name"])  # Output: Hagen
   ```

2. **Adding or Updating Values**: Add new keys or update existing ones by assigning values.
   ```python
   person["is_student"] = False
   person["age"] = 32  # Update existing key
   ```

3. **Removing Values**: Use `del` to remove a key-value pair.
   ```python
   del person["is_student"]
   ```

---

### Nested Dictionaries
Dictionaries can hold other dictionaries as values, allowing for hierarchical or grouped data.
  
```python
person = {
    "name": "Hagen",
    "employment": {
        "University of Texas at Austin": {
          "job_title": "Lecturer",
          "start_year": 2025
        },
        "Rogers-O'Brien Construction": {
          "job_title": "Software Engineer",
          "start_year": 2022
        }
    }
}
```

#### Accessing Nested Data
Nested dictionaries are ideal for representing hierarchical data like organizational charts, user profiles, or complex JSON structures.

```python
print(person["employment"]["University of Texas at Austin"]["job_title"])
# Output: Lecturer
```

---

### **Why Use Dictionaries?**
1. **Key-Based Access**: Dictionaries allow direct lookup of values using descriptive keys rather than numeric indices, making data easier to read and understand.
     ```python
     print(person["name"])  # Output: Hagen
     ```

2. **Organization**: Dictionaries provide a structured way to group and access related data.
3. **Similarity to JSON**: Dictionaries closely resemble **JSON** (JavaScript Object Notation), which is widely used for storing and exchanging data in web applications.

---

### **Best Practices**
1. **Use Descriptive Keys**: Choose meaningful names for keys to make dictionaries more readable.

2. **Avoid Mutable Keys**: Keys must be immutable types like strings, integers, or tuples.

4. **Logical Structure**: Group related data in nested dictionaries to create a clear hierarchy.
