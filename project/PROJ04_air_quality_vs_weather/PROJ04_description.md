# Project 4: Outdoor Air Quality Forecasting

### **Project Overview**
Outdoor air quality is heavily influenced by weather conditions, with factors like temperature, humidity, and wind speed playing a significant role in pollution levels. In this project, students will develop a tool that forecasts air quality levels based on weather conditions, using data to predict the best and worst times of day for air quality. By analyzing how different weather patterns influence air quality, students will develop a simple forecasting model that can help inform people about the air quality in a large city.

### **Objective**
Students will gather forecasted weather data and air quality measurements for a large city (population greater than 500,000) and create a model that predicts air quality based on weather trends. The goal is to develop a tool that can forecast the times of day when air quality will be worst or best, and visualize the forecasted air quality against weather conditions. Students will explore the relationship between various weather conditions and pollution levels, and see how these factors vary across different seasons.

### **Project Definitions**

#### **Weather Parameters**
Students should use the following weather parameters, but can include additional metrics if they choose to:
1. **Temperature**: Warmer temperatures can worsen air quality by increasing the rate of chemical reactions in the atmosphere that form pollutants.
2. **Humidity**: High humidity can contribute to the trapping of pollutants close to the ground.
3. **Wind Speed**: Strong winds can help disperse pollutants, improving air quality.
  
#### **Pollution Levels**
Air quality is typically measured using the **Air Quality Index (AQI)**, which gives an indication of how polluted the air is and how it may affect health. Students will forecast this value using weather data.

#### **Data Sources**
**Forecast API** (e.g., OpenWeatherMap Forecast API) and **Air Pollution API** (e.g., OpenWeatherMap or other air quality data providers):
- **Weather Data**: This will provide forecasted data on temperature, humidity, and wind speed.
- **Air Quality Data**: This will provide real-time and forecasted AQI for the selected city.
  - You will need to sign up to get an API Key which you can use to authenticate via a query parameter.

### **Project Requirements**
1. **Data Collection**
   - Use the **Forecast API** to fetch forecasted weather data for a single large city (population greater than 500,000) for the next few days, focusing on temperature, humidity, and wind speed.
   - Use the **Air Pollution API** to fetch AQI data for the same city.
   - The city should be located in a region where weather patterns are significant in affecting air quality.

2. **Analysis**
   - Analyze the relationship between forecasted weather conditions (temperature, humidity, wind speed) and air quality (AQI).
   - Use a simple regression or other predictive model to forecast air quality based on the weather trends.
   - Identify the times of day when air quality is expected to be the worst or best based on the forecasted weather and AQI.

3. **Visualization**
   - Create **3 scatter plots**, one for each weather parameter (temperature, humidity, wind speed) plotted against air quality (AQI).
   - The scatter plots should clearly show how each weather variable impacts air quality.
   - Ensure the visualizations provide insights into how weather conditions influence the air quality at different times.
