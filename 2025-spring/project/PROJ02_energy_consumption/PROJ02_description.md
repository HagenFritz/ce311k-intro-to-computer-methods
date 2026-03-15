# **Project 2: Building Energy Consumption Predictor**

## **Project Overview**
Energy consumption in buildings depends on a variety of factors, including **weather conditions**, **building design**, **insulation quality**, and **occupancy patterns**. In this project, you will use **TMY (Typical Meteorological Year)** data to estimate the **annual energy consumption** of three different buildings. By calculating **heating** and **cooling** requirements from temperature and humidity (via **Wet-Bulb Temperature (WBT)** for cooling, and **dry-bulb temperature** for heating), you’ll compare how factors such as **building type**, **size**, and **insulation level** affect overall energy usage.

### **Major Questions for Your Proposal**

1. **Location Choice and Building Characteristics**  
   - Which city/location will you choose to run your analysis in? Why did you choose this location? Does it have seasonal variability or not? What would you expect to see in terms of energy consumption at this location?
   - Which building types provided in the JSON file do you think will consume the most energy? Why? 

2. **Wet-Bulb Temperature & Data Handling**  
   How do you plan to calculate the **Wet-Bulb Temperature (WBT)** from the TMY data for cooling energy? Will you calculate it separately and store it in a list or will you calculate it as you iterate through the data? Will you store or preprocess the data in a particular format? How will you handle any data anomalies (e.g., missing hours)?

3. **Visualization Strategy**  
   How will you **visualize** your results (e.g., line plots, bar charts, side-by-side comparisons) to highlight differences in **heating** and **cooling** energy usage among the three building types?

> **Note**: Your final approach can evolve once you begin working with real data. These questions ensure you have a plan and can adapt as needed.

## **Objective**
You will use **hourly TMY data** for a location in the United States (of your choosing) to predict the **annual heating and cooling energy needs** for **three distinct buildings**. By calculating **WBT** for cooling and using **dry-bulb temperature** for heating, you’ll apply **heating and cooling conversion factors** to estimate kWh usage. You’ll then compare the **total energy consumption** across building types with varying insulation quality and system efficiencies.

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
   - Use the [NSRDB Viewer](https://nsrdb.nrel.gov/data-viewer) to find a location (USA only) you are interested in and download the latest TMY data from that location with a 60-minute interval and be sure to choose the option to convert UTC to local time.
  
2. **Energy Prediction Model**
   - Calculate **WBT** for cooling energy using the hourly **temperature** and **humidity** values from the TMY data. Be sure to check for any missing values for either relative humidity or temperature and handle them appropriately.
   - For heating, you will use the **dry-bulb temperature** (provided in the TMY file). Be sure to drop any rows with missing values for temperature or that you dropped from your calculation of WBT.
   - Estimate the Heating, Cooling, and Total energy consumption for each hour in the TMY file, applying the appropriate factors based on the building characteristics in hte JSON file. 

3. **Analysis**
   - Calculate **annual energy consumption** for heating, cooling, and total for each building.
   - Compare the total energy consumption for **different building types** (e.g., residential, commercial, and industrial). Do these results match your expectations from Major Question 1? Do you think these are realistic?
   - Look for trends: Do certain temperatures or times of year drive consumption significantly higher? Why?

4. **Visualization**
   - Provide visuals that help support your analysis based on your answer to Major Question 3. Some visuals to consider: 
      - A bar chart or line graph comparing the energy consumption between different building types.
      - A time series plot showing energy consumption trends over time. These could be between different building types
      - Cumulative energy consumption over the year for each building type.