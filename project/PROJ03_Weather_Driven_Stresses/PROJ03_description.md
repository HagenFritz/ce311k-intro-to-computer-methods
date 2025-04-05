# **Project 3: Weather-driven Civil Infrastructure Stress Simulator**

### **Project Overview**
Civil infrastructure is subject to stresses induced by varying weather conditions, which can cause deterioration over time. In this project, students will use **TMY (Typical Meteorological Year)** data to estimate the **stress levels** on three types of infrastructure (bridges, roads, buildings) based on temperature fluctuations. They will simulate the **thermal expansion** of materials and analyze how these weather-driven changes can affect the integrity of different types of infrastructure.

### **Objective**
Students will use hourly TMY data to predict the **weather-induced stress** on infrastructure materials, focusing on temperature. The project will involve calculating **thermal expansion** using the **coefficient of thermal expansion (CTE)** for various building materials. Students will then compare the simulated stress on infrastructure made from different materials (steel, concrete, and wood) across the entire year.

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
   - Use the [NSRDB Viewer](https://nsrdb.nrel.gov/data-viewer) to download the **TMY** file for a location of your choice.
   - Choose the “USA & Americas - Typical Meteorological Year” option.
   - Select **Temperature** and **Relative Humidity** attributes.
   - Use the **tmy-2023** file for the most recent data.
   - Set the interval to **60 minutes** and select the option to “Convert UTC to Local Time”.

2. **Simulation Model**
   - Use the hourly **temperature** data from the TMY file to calculate **thermal expansion** for each material (steel, concrete, and wood) at each hour of the year.
   - Calculate the **stress** induced by thermal expansion at each hour of the year for each material using the **coefficient of thermal expansion (CTE)** and **Young’s Modulus** values from the provided material properties table.
   
3. **Analysis**
   - Simulate the **annual stress** on infrastructure due to temperature changes for each material type (see above)
   - Compare the stress levels induced by temperature fluctuations for **steel**, **concrete**, and **wood**. Consider ideas such as (but not limited to): mean changes in expansion/stress, maximum stress events, etc. 
   - Analyze how **temperature extremes** (e.g., heatwaves and cold snaps) contribute to stress and how material properties impact infrastructure resilience.

4. **Visualization**
   - Create a **line plot** for each material to show the **thermal expansion** over the course of the year.
   - Create a **line plot** comparing the **stress levels** for each material across the year, highlighting peak stress events.
   - Visualize and compare the total **annual stress** (cumulative sum) for each material.