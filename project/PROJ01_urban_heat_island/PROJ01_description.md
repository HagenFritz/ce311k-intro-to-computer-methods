# **Project 1: Urban Heat Island Effect Analysis**

## **Project Overview**
The **Urban Heat Island Effect** refers to the phenomenon where urban areas experience higher temperatures than their rural surroundings, primarily due to human activities and environmental modifications (e.g., buildings, roads, and reduced vegetation). In this project, you will use **real weather forecasts** to analyze temperature differences between **urban** and **rural** areas in **three distinct climate zones** (tropical, temperate, and desert). You’ll compare forecasted temperatures, visualize the differences, and examine how **local climate** influences the severity of the heat island effect.

### **Major Questions for Your Proposal**

1. **City Pairs in Each Climate Zone**  
   Which **urban/rural pairs** are you selecting for each of the three climate zones (tropical, temperate, and desert), and why did you choose those specific cities or regions?

2. **Temperature Metrics**  
   Which metrics (e.g., daily highs, daily lows, means, medians) will you focus on to highlight the Urban Heat Island effect? Briefly explain why these metrics are meaningful for your comparison.

3. **Visualization Strategy**  
   How do you plan to **visualize** your results (e.g., line charts showing urban vs. rural temperatures on the same axes, side-by-side bar charts)? Do you think these will adequately highlight the Urban Heat Island effect? Why or why not?

### **Objective**
You will gather **5-day forecasted temperature data** from the [OpenWeatherMap API](https://openweathermap.org/forecast5) for urban and rural city pairs in **three** climate zones—tropical, temperate, and desert—and explore correlations between temperature, urbanization, and local climate. Your findings should highlight how and why these temperature disparities exist.

### **Project Definitions**

#### **Climate Zones**
- **Tropical Climate**: Cities typically located near the equator with high temperatures year-round and significant rainfall. Example: **Houston, Texas**.
- **Temperate Climate**: Cities with moderate seasonal changes, cooler winters, and warm summers. Example: **Austin, Texas**.
- **Desert Climate**: Cities with very hot summers and mild winters, characterized by low rainfall. Example: **El Paso, Texas**.
  
#### **City Definitions**
  - **Urban City**: Defined as a city with a population of **over 500,000** people. These cities have significant human development, infrastructure, and building density. Examples: **Austin, Texas**.
  - **Rural City**: Defined as a city with a population of **under 100,000** people. These cities have less dense development, more open land, and fewer urban features like large buildings or extensive transportation networks. Examples: **Bastrop, Texas**.

### **Data Sources**
**OpenWeatherMap 5-day Forecast API**: [API Documentation](https://openweathermap.org/forecast5)
- Use this API to retrieve forecasted temperature data for your chosen urban/rural pairs.  
- You will need to sign up for an API key and include it as a query parameter in your requests.  

### **Project Requirements**
1. **Data Collection**
   - Use the **OpenWeatherMap 5-day Forecast API** to collect temperature data for **six total cities** (3 pairs of urban vs. rural, one pair per climate zone) based on your answers to Major Question 1.
   - Use all available data you get from the API for creating summary statistics and visualizations.

2. **Analysis**
   - Calculate the temperature metrics you decided on in your proposal in Major Question 2.
   - Use these metrics as evidence to provide a _written_ analysis of the Urban Heat Island effect based on your data. Some topics to consider: 
      - Any significant disparities that indicate a strong Urban Heat Island effect.
      - How **local climate** (tropical, temperate, desert) influences the severity of the Urban Heat Island effect.
      - How **urbanization** (urban vs. rural) influences the severity of the Urban Heat Island effect.
      - How **time** (day of the week, time of day) influences the severity of the Urban Heat Island effect.

3. **Visualization**
   - Provide visuals that help support your analysis based on your answer to Major Question 3. Some visuals to consider: 
      - A bar chart or line graph comparing the temperature metrics between urban and rural areas.
      - A heat map or choropleth map showing temperature differences between urban and rural areas.
      - A time series plot showing temperature trends over time. These could be between urban and rural areas, and/or between different climate zones.

4. **Data File**
   - Save the data from each at least one of the six cities as either a CSV or a JSON file and submit it/them with your other project files.