# 🧼 Data Cleaning & Preprocessing

**Data cleaning** is the process of identifying and correcting problems in raw data to make it ready for analysis. This is a crucial first step in any data science or engineering workflow.

> _“Garbage in, garbage out” — if your input data is bad, your results will be too._

### ⚠️ Why Clean Data?

- To **remove errors** (e.g. duplicates, invalid values)
- To **handle missing or incomplete data**
- To **standardize formats** for consistency
- To **prepare for calculations** (e.g. converting types, extracting values)
- To **avoid silent failures** (e.g. string vs float mismatches)

## 🧯 Handle Missing Data

Missing data can come from sensor failures, incomplete forms, or corrupted files.  
Here are common strategies for dealing with missing values:

### 1. **Remove Entry**
```python
cleaned = [value for value in data if value not in ("", None)]
```
- ✅ Use when missing values are rare and won’t bias your results.

### 2. **Use Default Value**
```python
cleaned = [value if value not in ("", None) else 23 for value in data]
```
- ✅ Great for things like temperature where a “typical” value works.

### 3. **Forward Fill**
```python
filled = []
prev = None
for value in data:
    if value in ("", None):
        filled.append(prev)
    else:
        filled.append(value)
        prev = value
```
- ✅ Useful for time-series data with slow variation (e.g. environmental sensors).

## 🚫 Handle Invalid Data

Not all data that *exists* is *valid*.

### 💡 Common CAEE Checks:
- Is the value **physically reasonable**? (e.g. CO₂ < 100 ppm is suspect)
- Is it **within expected range**? (e.g. temperature between -20 to 50 °C)
- Does the value **fit the format**? (e.g. numeric, not text)

### ✅ Filtering Outliers:
```python
valid = [value for value in co2_readings if value >= 300]
```

> Use **domain knowledge** to define rules. Always **document** any filtering that removes data!

## 🧹 Fix Poor Formatting

Messy formatting often comes from:
- Copy-pasting from Excel
- Multiple data sources
- Human error (typos, casing, extra symbols)

### 🔧 Cleaning Strategies

| Problem | Solution |
|--------|----------|
| Extra spaces | `value.strip()` |
| Weird casing | `value.lower()` or `value.upper()` |
| Mixed units | Convert all to same (e.g. `"72 F"` → `22.2`) |
| Special characters | `re.sub(r"[^\w\s]", "", value)` |
| Extract numeric | `value.split()[0]` or regex |

### 🧪 Example: Extract temperature from messy strings
```python
raw_temps = ["23.5C", " 21.0 C", "20C", "invalid"]

cleaned = []
for val in raw_temps:
    try:
        number = float(val.split("C")[0].strip())
        cleaned.append(number)
    except:
        continue
```