# **Project 6: Historic Air Quality Analysis with OpenWeatherMap**

## **Project Overview**
Air quality often exhibits **seasonal** and **long-term** trends, influenced by factors like local emissions, weather patterns, and broader regional phenomena. In this project, you will use the **OpenWeatherMap Air Pollution API** to retrieve **historical** pollutant data for a chosen city or multiple cities. By examining changes over an extended timeframe, you’ll uncover **seasonal patterns**, identify potential **pollutant interactions**, and see how air quality evolves beyond day-to-day fluctuations.

### **Objective**
You will pull **historical air quality** data from the **OpenWeatherMap Air Pollution API** over a chosen period (at least several months) to investigate **seasonal** and **long-term** trends in pollutant levels. By exploring whether certain pollutants spike at specific times of year and how they may correlate with each other, you’ll gain insights into the **complex interactions** that shape a city’s air quality profile over time.

### **Major Questions for Your Proposal**

1. **Historic Timeframe & Location(s)**  
   - Which **city** (or **cities**) will you study, and how far back will you gather data (e.g., 6 months, 1 year, multiple years)? Please note data are only available until 2020.  
   - What **seasonal** shifts do you anticipate (e.g., winter pollution peaks, summer ozone spikes)?  
   - Are there local events or emission sources you suspect might show up in the data (e.g., heavy traffic periods, industrial changes, fires)?

2. **Data Retrieval & Analysis Approach**  
   - How will you **access the historical endpoints** of the **OpenWeatherMap Air Pollution API**?  
   - Which **statistical** or **exploratory** methods (e.g., monthly averages, rolling means, correlation analysis) will you use to expose **seasonal** or **long-term** trends?  
   - How do you plan to handle **incomplete** or **inconsistent** data points?

3. **Pollutant Interactions**  
   - Which **pollutants** (CO, NO, NO₂, O₃, SO₂, PM₂.₅, PM₁₀, NH₃) will you focus on, and why?  
   - Do you expect any **relationships** among pollutants?  
   - How will you test or illustrate these interactions?

4. **Visualization of Seasonal & Comparative Insights**  
   - What **visuals** (line charts, boxplots, heatmaps) will you create to highlight **seasonal** or **year-to-year** changes in pollutant levels and AQI?  
   - If you compare **multiple cities**, how will you display differences or similarities?  
   - Will you incorporate **AQI** to show overall air quality trends alongside specific pollutant fluctuations?

## **Project Definitions**

### **Historic Air Quality Data**
- Encompasses a series of time-stamped pollutant concentrations (e.g., CO, NO₂, O₃, PM₂.₅) and **AQI** values.

### **Seasonal & Inter-Pollutant Trends**
- **Seasonal Effects**: Temperature, humidity, and sunlight can dramatically alter chemical reaction rates, thus influencing pollution levels.  
- **Pollutant Interactions**: For example, NO₂ and O₃ can exhibit inverse correlations under certain sunlight conditions.

## **Data Sources**

**OpenWeatherMap Air Pollution API (Historic Endpoints)**: [API Documentation](https://openweathermap.org/api/air-pollution)
- The API provides **historic** data for pollutants, including CO, NO, NO₂, O₃, SO₂, PM₂.₅, PM₁₀, NH₃, and overall **AQI** starting from 27th November 2020.
- You will need an API key to access historical records.

## **Project Requirements**

1. **Data Collection**  
   - Select **one or more** cities and define a **time period** (e.g., 6 months, 1 year, longer if available).  
   - Retrieve the **historic air quality** data (pollutants + AQI) from OpenWeatherMap for each relevant date/time and location.
   - Store the data in a structured format and handle **missing** or **anomalous** entries as needed.

2. **Analysis**  
   - Compute **descriptive statistics** (e.g., monthly averages, daily highs, rolling means) to reveal **seasonal** or **year-to-year** variations.  
   - Investigate **pollutant interactions** and discuss potential reasons for these relationships.  
   - Compare **AQI** across different times of the year or among multiple cities, if applicable.

3. **Visualization**  
   - Present **time-series** plots (line, bar charts, etc.) to display pollutant levels and AQI over the chosen period.  
   - Include **boxplots** or **heatmaps** to highlight seasonal changes or pollutant correlations.  
   - If using multiple cities, create **side-by-side** or **layered** visuals demonstrating how different regions differ or align in terms of pollution patterns.

4. **Data File**
   - Save the primary air quality data you used to a `csv` or `json` file.
