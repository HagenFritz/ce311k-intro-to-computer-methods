# Data Encoding

**Encoding** is the process of converting **non-numeric (usually categorical)** data into a format your code or analysis can work with — most often numbers.

> Computers can’t “understand” strings like `"Low"`, `"Medium"`, or `"High"` the way humans do — we need to **translate** that information into a usable numerical form.

### ✳️ Why Do We Encode?

1. ✅ **To make comparisons/calculations possible**
   - You can’t compare `"Low"` < `"Medium"` unless you assign numbers.

2. 📊 **To allow plotting and aggregation**
   - Encoded values can be averaged, grouped, or graphed.

3. 🔄 **To simplify downstream analysis**
   - Once encoded, you can use conditionals, filters, or math without string handling.


## 🔢 Common Encoding Strategies

1. **Manual Mapping**: Define a dictionary to convert values

```python
priority_map = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

priority_score = priority_map.get("High")
# Output: 3
```

---

### 2. **Binary Encoding (Yes/No, On/Off)**: Convert simple flags into 0 and 1

```python
status = "On"
encoded = 1 if status == "On" else 0
```

---

### 3. **Bucket/Range Encoding**: Convert numeric values into labeled categories, then encode

```python
temp = 82

if temp < 70:
    level = "Cool"
elif temp < 80:
    level = "Comfortable"
else:
    level = "Hot"

level_map = {"Cool": 1, "Comfortable": 2, "Hot": 3}
encoded = level_map[level]
```
