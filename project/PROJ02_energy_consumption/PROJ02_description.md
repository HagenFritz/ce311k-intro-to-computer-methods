# **Project 2: Building Energy Consumption Predictor**

### **Project Overview**
Energy consumption in buildings is influenced by weather conditions, building design, insulation, and occupancy patterns. In this project, students will use **TMY (Typical Meteorological Year)** data to estimate the **annual energy consumption** of three different buildings. By calculating **heating** and **cooling** energy requirements based on temperature and humidity (through Wet-Bulb Temperature), students will compare the energy consumption of buildings with different characteristics, such as size, insulation, and heating/cooling system efficiency.

### **Objective**
Students will use hourly TMY data for a location of their choosing to predict the annual heating and cooling energy requirements for three buildings. They will calculate the **heating** and **cooling** demands over the entire year using **Wet-Bulb Temperature (WBT)** for cooling and dry-bulb temperature for heating, applying specific **conversion factors** for each. The students will then compare the energy consumption across three building types with varying insulation levels.

### **Project Definitions**

#### **Wet-Bulb Temperature Calculation**
The **Wet-Bulb Temperature (WBT)** can be calculated using the following approximation:

$$
T_{wb} = T \times \arctan(0.151977 \times \sqrt{RH + 8.313659}) + \arctan(T + RH) - \arctan(RH - 1.676331) + 0.00391838 \times RH^{3/2} \times \arctan(0.023101 \times RH) - 4.686035
$$

Where:
- **$T$** is the dry-bulb temperature (°C).
- **$RH$** is the relative humidity (as a percentage).
- **$T_{wb}$** is the Wet-Bulb Temperature (°C).

#### **Energy Consumption Prediction Formula**
After calculating **WBT** for cooling, and using the dry-bulb temperature for heating, the energy consumption formulas will use different conversion factors for **heating** and **cooling**:

#### **Heating Energy**
$$
\text{Heating Energy (kWh)} = \sum \left(\text{Dry-Bulb Temperature} \times \text{Building Area} \times \text{Insulation Factor} \times \text{Heating Conversion Factor}\right)
$$

Where:
- **Heating Conversion Factor** varies by building type (see below)
- **Insulation Factor** varies by building type (see below)
  
#### **Cooling Energy**
$$
\text{Cooling Energy (kWh)} = \sum \left(\text{WBT} \times \text{Building Area} \times \text{Insulation Factor} \times \text{Cooling Conversion Factor}\right)
$$

Where:
- **Cooling Conversion Factor** varies by building type (see below)
- **Insulation Factor** varies by building type (see below)

#### **Conversion Factors**
The **conversion factors** are assigned differently for **heating** and **cooling** and depend on the building type. The factors reflect the varying efficiency of different building types.

| Building Type   | Heating Conversion Factor (kWh per °C per square foot) | Cooling Conversion Factor (kWh per °C per square foot) |
|-----------------|--------------------------------------------------------|-------------------------------------------------------|
| **Industrial**   | 0.015                                                  | 0.018                                                 |
| **Residential**  | 0.020                                                  | 0.022                                                 |
| **Commercial**   | 0.025                                                  | 0.028                                                 |

### **Data Sources**
- **TMY Data**: Hourly temperature and humidity data from the TMY file for a selected location. This data will span the entire year and be used to calculate heating and cooling energy consumption using WBT and dry-bulb temperature.
- **Building Information**: JSON file will contain the building type, square footage, insulation factor, and heating/cooling conversion factors

### **Project Requirements**
1. **Data Collection**
   - Use the [NSRDB Viewer](https://nsrdb.nrel.gov/data-viewer) to find a location (USA only) you are interested in
   - Choose option for "USA & Americas - Typical Meteorological Year"
   - **Select Attributes**: Check off the "Temperature" and "Relative Humidity" attributes (and any others you are interested in)
   - **Select Year**: Choose the "tmy" data file with the latest year - most likey "tmy-2023"
   - **Select Interval**: Choose "60 minutes"
   - Check the box to "Convert UTC to Local Time"
   - Input your email and click the "Download" button
  
2. **Energy Prediction Model**
   - Calculate **WBT** for cooling energy using the hourly **temperature** and **humidity** values from the TMY data.
   - For heating, you will use the **dry-bulb temperature** (provided in the TMY file)
   - Estimate the Heating, Cooling, and Total energy consumption for each hour in the TMY file, applying the appropriate factors based on the building characteristics:

3. **Analysis**
   - Calculate **annual energy consumption** for heating, cooling, and total for each building.
   - Compare the total energy consumption for **different building types** (e.g., residential, commercial, and industrial).
   - Explore how **insulation quality** and **building type** affect energy consumption, particularly for buildings with poor versus good insulation.

4. **Visualization**
   - Create a line plot for each building (3 plots) to compare the **predicted energy consumption** for each building over the course of the year. Each plot should have the heating, cooling, and total energy consumption as separate lines. 
   - Visualize and compare the heating, cooling, and total energy requirements for each building type. You should create a line plot for each comparison (3 plots): heating, cooling, and total.
