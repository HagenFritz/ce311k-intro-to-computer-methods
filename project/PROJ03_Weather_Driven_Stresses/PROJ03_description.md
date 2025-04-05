# **Project 3: Weather-driven Civil Infrastructure Stress Simulator**

## **Project Overview**
Civil infrastructure is subject to stresses induced by varying weather conditions, which can cause deterioration over time. In this project, students will use **TMY (Typical Meteorological Year)** data to estimate the **stress levels** on three types of infrastructure (bridges, roads, buildings) based on temperature fluctuations. They will simulate the **thermal expansion** of materials and analyze how these weather-driven changes can affect the integrity of different types of infrastructure.

### Major Questions for Your Proposal
1. **Location and Material Types**  
   - Which location do you plan to analyze for your TMY data? Why did you choose this location? Do you think the conditions at that location will have significant effects on the stress levels of the infrastructure?
   - Which material types do you think will experience significant thermal expansion? Which will experience the greatest stress? Would these effects differ if you chose a different location?
2. **Thermal Expansion Calculation Strategy**  
   How do you plan to apply the thermal expansion formulas across the hourly TMY data? Will you store intermediate values (expansion, stress) for each material in a list or process them on-the-fly? Will you process one material at a time or process each material in parallel for each hour? How will you handle missing or anomalous temperature data?  
3. **Visualization Approach**  
   How will you visualize the expansion and stress results for each material? Will you use line plots, bar comparisons, or some other approach? Will you show cumulative stress over time? How do you think these plots will highlight differences among the materials?

### **Objective**
You will use hourly TMY data from a chosen location in the United States to simulate the thermal expansion and resulting stress in three infrastructure types. By comparing steel, concrete, and wood under identical temperature changes, you will identify how material properties influence stress levels and highlight the role of extreme temperature events.

### **Project Definitions**

#### **Thermal Expansion Calculation**
The **thermal expansion** of a material due to temperature change can be calculated using the formula:

$$
\Delta L = \alpha \times L_0 \times \Delta T
$$

Where:
- **$\Delta L$** is the change in length (m).
- **$\alpha$** is the coefficient of thermal expansion (CTE) (1/°C).
- **$L_0$** is the initial length of the material (m).
- **$\Delta T$** is the change in temperature (°C).

#### **Stress Induced by Expansion**
To calculate the stress induced by expansion:

$$
\sigma = \frac{E \times \Delta L}{L_0}
$$

Where:
- **$\sigma$** is the stress (Pa).
- **$E$** is the Young’s Modulus (Pa) for the material.
- **$\Delta L$** is the expansion (m).
- **$L_0$** is the initial length (m).

#### **Materials Properties**
Here are some material properties that will be used for the simulation:

| Material   | Coefficient of Thermal Expansion (CTE) (1/°C) | Young's Modulus (Pa) |
|------------|----------------------------------------------|----------------------|
| **Steel**  | 12e-6                                       | 200e9                |
| **Concrete** | 10e-6                                     | 30e9                 |
| **Wood**   | 5e-6                                        | 10e9                 |

### **Data Sources**
- **TMY Data**: Hourly temperature and humidity data from the TMY file for a selected location. This data will be used to calculate the temperature fluctuations throughout the year.
- **Material Properties**: Data on the coefficient of thermal expansion (CTE) and Young's Modulus (E) for different materials will be stored in a JSON file.

### **Project Requirements**
1. **Data Collection**
   - Use the [NSRDB Viewer](https://nsrdb.nrel.gov/data-viewer) to find a location (USA only) you are interested in and download the latest TMY data from that location with a 60-minute interval and be sure to choose the option to convert UTC to local time.

2. **Simulation Model**
   - Use the hourly **temperature** data from the TMY file to calculate **thermal expansion** for each material (steel, concrete, and wood) at each hour of the year. Use or update the process you outlined in your proposal for Major Question 2.
   - Calculate the **stress** induced by thermal expansion at each hour of the year for each material using the **coefficient of thermal expansion (CTE)** and **Young’s Modulus** values from the provided material properties table.
   
3. **Analysis**
   - Simulate the **annual stress** on infrastructure due to temperature changes for each material type (see above)
   - Compare steel, concrete, and wood by identifying times of peak stress, cumulative stress over the year, and/or average daily stress. Discuss whether the results match your initial thoughts about material performance from Major Question 1.
   - Analyze how **temperature extremes** (e.g., heatwaves and cold snaps) contribute to stress and how material properties impact infrastructure resilience.

4. **Visualization**
   - Present plots that show expansion and/or stress trends over time, following your proposal from Major Question 3. Consider:
      - line plots of hourly expansion/stress values across the year. Can you highlight extreme events (e.g., heatwaves, cold snaps)?
      - bar comparisons of annual expansion/stress or cumulative stress for each material type
      - side-by-side or grouped comparisons of expansion/stress or cumulative expansion/stress for each material type