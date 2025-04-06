# **Project 5: Earthquake Risk Assessment with USGS Data**

## **Project Overview**
The **U.S. Geological Survey (USGS)** Earthquake Catalog provides near real-time data about earthquakes happening around the world. In this project, you will leverage the **USGS Earthquake Catalog API** to gather recent seismic activity data for a specific region in the United States. By analyzing metrics like **magnitude**, **depth**, and **frequency** of earthquakes, you will build a simple model or visualization that helps illustrate the **seismic risk** for infrastructure or populations within your chosen region.

### **Objective**
You will collect **earthquake data** from the **USGS Earthquake Catalog API** over a given timeframe. Then, you’ll **analyze** the distribution of earthquake events (by magnitude, depth, frequency, etc.) and produce **visualizations** that communicate the seismic risk in that area. This project will help you understand how to query and interpret real-time geophysical data for insights relevant to civil or environmental engineering risk assessments.

### **Major Questions for Your Proposal**

1. **Region and Timeframe Selection**  
   - Will you focus on a particular region in the **United States**? If so, which part of the **United States** do you plan to focus on, and why?  
   - Over what **timeframe** (e.g., the past 30 days, the past year) do you intend to gather earthquake data? 
   - Do you expect the chosen region to show significant seismic activity, or is it an area with relatively few earthquakes?

2. **Data Retrieval and Processing Strategy**  
   - How do you plan to **query the USGS Earthquake Catalog API**? (e.g., bounding coordinates, minimum magnitude filters, date range)  
   - How do you plan to handle potential **missing fields** or **outlier values** (e.g., extremely deep quakes or very high magnitudes)?

3. **Visualization and Risk Indicators**  
   - How will you **visualize** your earthquake data? (e.g., plotting epicenters on a map, creating a time series of magnitudes, or grouping quakes by depth). What visuals will you use to explore the data? What visuals will you use to communicate the seismic risk? 
   - What **risk indicators** (e.g., average magnitude, quake frequency, maximum magnitude) will you highlight to give a sense of the region’s seismic hazard?

> **Note**: Your final approach can adapt as needed once you see the actual data. These questions ensure you have a plan for retrieving, processing, and visualizing USGS earthquake information.

## **Project Definitions**

### **Earthquake Parameters**
- **Magnitude (M)**: A measure of the size or energy released by an earthquake event, commonly reported on the **Moment Magnitude Scale** (similar to the older Richter Scale).  
- **Depth (km)**: How far below the earth’s surface the earthquake originated.  
- **Location (Latitude/Longitude)**: The epicenter coordinates of the earthquake.

### **Seismic Risk Indicators**
- **Frequency**: Number of earthquakes over a specific magnitude threshold within the chosen timeframe.  
- **Max/Min Magnitude**: The strongest and weakest earthquakes recorded in the dataset.  
- **Average Magnitude**: A rough gauge of overall seismic intensity in the region.

## **Data Sources**
- **USGS Earthquake Catalog API**:  
  - [USGS API Documentation](https://earthquake.usgs.gov/fdsnws/event/1/)  
  - Allows filtering by **start time**, **end time**, **bounding box** (min/max lat/lon), and **minimum magnitude**.  
  - Returns JSON data containing details about each earthquake event (time, coordinates, magnitude, depth, etc.).

## **Project Requirements**

1. **Data Collection**  
   - Use the **USGS Earthquake Catalog API** to query earthquakes for a **specific region** (e.g., bounding box around California) and **time period** (e.g., past 30 days) based on your answer to **Major Question 1** (Region and Timeframe Selection).  
   - Save or parse the **JSON** response in a convenient format (CSV, JSON, or direct memory structures i.e. dictionaries).

2. **Analysis**  
   - Parse and process relevant fields like **magnitude**, **depth**, **coordinates**, and **event time**.  
   - Consider your plan from **Major Question 2** (Data Retrieval and Processing Strategy) to handle data anomalies or missing fields.  
   - Identify **risk indicators**—for example, quake frequency above a certain magnitude, average depth, or maximum magnitude in the dataset.

3. **Visualization**  
   - Following **Major Question 3** (Visualization and Risk Indicators), create plots/maps to help you explore the data and communicate your results. Examples:  
     - **static scatter plot** of epicenters (latitude vs. longitude) color-coded by magnitude.  
     - **Time series** of earthquakes by date or magnitude to see trends.  
     - **Histogram** showing the distribution of magnitudes or depths.  
   - Include annotations and thresholds to highlight potential areas of concern.

4. **Data File**
   - Save the primary earthquake data you used to a `csv` or `json` file.