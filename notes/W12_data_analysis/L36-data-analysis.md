# Data Analysis
Once your data is pre-processed and visualized, **data analysis** is where you:

> **Apply logic, rules, or calculations to extract insights or answer a specific question.**

It’s the step where you stop *looking at* the data and start *doing something with it*.

## 🧠 What Happens During Data Analysis?

1. **Apply Rules**
Use thresholds or logic to flag or classify data.

```python
if temp > 100:
    flag = "too hot"
```

2. **Summarize or Aggregate**
Use basic math to describe the data.

```python
avg_temp = sum(temps) / len(temps)
max_co2 = max(co2_levels)
```

3. **Compare Across Groups**
Group and compare data by category (e.g. wind speed by day type).

```python
if day_type == "Weekend":
    weekend_wind.append(speed)
```

4. **Identify Trends or Patterns**
Use your visual exploration to guide logical insights.
- “Most of the weather delays occurred in March”
- “Higher CO₂ levels appear after 2 p.m.”

5. **Make Engineering-Driven Judgments**
This is the real value:
- “Ventilation needs to increase if CO₂ exceeds 800 ppm”
- “This site should plan for ~12 lost days due to snow”
