
# Data Transformations
**Data transformations** are the process of converting raw values into a more useful, consistent, or meaningful format — without changing the underlying meaning of the data.

### ✳️ Why Transform Data?

- To **standardize units** (e.g. ft → m, °F → °C)
- To **simplify calculations** (e.g. convert timestamps to `datetime`)
- To **derive new variables** that are more useful than the raw ones (e.g. `dew point`, `energy per square foot`)
- To **scale or normalize** values for comparison

## 🔧 Common Types of Transformations

### ⚙️ Unit Conversions
Converting data to a consistent unit system (very relevant in engineering!)
```python
# Fahrenheit to Celsius
temp_c = (temp_f - 32) * 5/9
```

1. **Consistency Across Data Sources**
   - Data often comes from multiple systems with different units (e.g. sensors in °F vs. °C).
   - Consistent units avoid errors and make comparison possible.

2. **Interpretability**
   - Some units are more familiar or useful to your audience (e.g. converting mm/hr to in/hr for U.S. teams).

3. **Required for Calculations**
   - Many engineering formulas assume specific units (e.g. SI vs. Imperial).
   - Using the wrong unit can produce incorrect results or fail silently.

### 🧮 Derived Variables
Creating new columns from existing ones
```python
# Air change rate, assuming exponential decay
ACH = 60 * (1 / elapsed_time) * math.log(initial_CO2 / final_CO2)
```

1. **Capture Relationships Between Variables**
   - You might need to combine fields to reveal meaningful behavior (e.g. air change rate from CO₂ levels over time).

2. **Reduce Redundancy in Code**
   - Repeated formulas can be stored as a new variable instead of recalculating every time.

3. **Enable Domain-Specific Analysis**
   - Raw data (e.g. CO₂ levels) isn’t always useful until transformed into something meaningful (e.g. ventilation performance).

### ⚖️ Normalizations
Adjusting values relative to size, time, or scale for fair comparison  
```python
# Energy use per square meter
energy_per_m2 = energy_kwh / area_m2
```

1. **Compare Across Scales**
   - You can’t compare energy use in a small home vs. a skyscraper unless you normalize (e.g. kWh per square foot).

2. **Remove Size Bias**
   - Normalization helps ensure large values don’t dominate your results due to sheer magnitude (e.g. rainfall per day vs. per hour).

3. **Standardize for Thresholds**
   - Some thresholds only make sense on a normalized basis (e.g. 1.5 air changes per hour is meaningful, raw CO₂ decay is not).
