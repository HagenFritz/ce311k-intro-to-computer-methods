### Customizing Figures in Matplotlib

#### Axes Limits
You can control the visible range of data on your plot using `xlim()` and `ylim()`:

```python
plt.xlim(1, 3)  # Set x-axis limits from 1 to 3
plt.ylim(10, 30)  # Set y-axis limits from 10 to 30
```

#### Axes Ticks
Modify axis ticks for more meaningful data labeling:

```python
plt.xticks([1, 2, 3], ['Low', 'Medium', 'High'])  # Custom x-axis ticks
plt.yticks([10, 20, 30], ['Low', 'Medium', 'High'])  # Custom y-axis ticks
```

---

### Subplots in Matplotlib
`plt.subplots()` is the most versatile way to create multiple plots in one figure:

```python
fig, axs = plt.subplots(nrows, ncols, figsize=(width, height))
```

- **`nrows`, `ncols`**: Define the grid of plots.
- **`figsize`**: Set the size of the overall figure.

#### Example: Stress vs. Strain
Plot stress vs. strain for two materials:
```python
fig, axs = plt.subplots(2, 1, figsize=(5, 10))

axs[0].plot(strain_1, stress_1, label='Material 1')
axs[0].set_title("Stress vs. Strain: Material 1")
axs[0].set_xlabel("Strain (mm/mm)")
axs[0].set_ylabel("Stress (MPa)")
axs[0].grid(True)

axs[1].plot(strain_2, stress_2, label='Material 2')
axs[1].set_title("Stress vs. Strain: Material 2")
axs[1].set_xlabel("Strain (mm/mm)")
axs[1].set_ylabel("Stress (MPa)")
axs[1].grid(True)
```

---

### Twin Axes
Overlay two plots with different y-axes but a shared x-axis.

```python
ax2 = ax1.twinx()
```

#### Example: Wind Speed and Power Output
Compare wind speed with power output and efficiency:
```python
wind_speed = [2, 4, 6, 8, 10, 12, 14]
power_output = [0, 10, 50, 120, 200, 300, 350]
efficiency = [0, 20, 35, 50, 60, 65, 63]

fig, ax1 = plt.subplots()
ax1.plot(wind_speed, power_output, 'b-')
ax1.set_xlabel("Wind Speed (m/s)")
ax1.set_ylabel("Power Output (kW)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(wind_speed, efficiency, 'r--')
ax2.set_ylabel("Efficiency (%)", color='red')
ax2.tick_params(axis='y', labelcolor='red')
```