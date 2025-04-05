#!/usr/bin/env python3
import json
import random
import datetime
import os
from calendar import monthrange

def generate_water_use_data():
    # Building base parameters
    buildings = {
        "ECJ": {"base_usage": 15000, "base_occupants": 170},
        "EER": {"base_usage": 14000, "base_occupants": 150},
        "CPE": {"base_usage": 17000, "base_occupants": 185}
    }
    
    # Month parameters with increasing usage trend
    months = ["March", "April", "May"]
    month_multipliers = {"March": 1.0, "April": 1.1, "May": 1.2}
    
    # Day type parameters
    weekday_multiplier = 1.0
    weekend_multiplier = 0.9  # Less usage on weekends
    
    # Start date (March 1, 2024)
    start_date = datetime.date(2024, 3, 1)
    
    # List to store all data entries
    all_data = []
    
    # Generate data for each day in the three months
    current_date = start_date
    end_date = datetime.date(2024, 5, 31)
    
    while current_date <= end_date:
        month_name = current_date.strftime("%B")
        
        # Skip if not in our target months
        if month_name not in months:
            current_date += datetime.timedelta(days=1)
            continue
        
        # Determine day type
        day_of_week = current_date.weekday()
        if day_of_week < 5:  # Monday to Friday
            day_type = "Weekday"
            day_multiplier = weekday_multiplier
        else:  # Saturday and Sunday
            day_type = "Weekend"
            day_multiplier = weekend_multiplier
        
        # Generate data for each building on this day
        for building, params in buildings.items():
            # Calculate base values with month progression
            base_usage = params["base_usage"] * month_multipliers[month_name]
            base_occupants = params["base_occupants"]
            
            # Add randomness
            usage_variation = random.uniform(0.9, 1.1)  # ±10% variation
            occupant_variation = random.uniform(0.95, 1.05)  # ±5% variation
            
            # Calculate final values with day type consideration
            usage_liters = int(base_usage * usage_variation * day_multiplier)
            occupants = int(base_occupants * occupant_variation * day_multiplier)
            
            # Create data entry
            entry = {
                "building": building,
                "usage_liters": usage_liters,
                "occupants": occupants,
                "day_type": day_type,
                "month": month_name,
                "date": current_date.strftime("%Y-%m-%d")
            }
            
            all_data.append(entry)
        
        # Move to the next day
        current_date += datetime.timedelta(days=1)
    
    return all_data

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Define the output file path
    output_file = os.path.join(script_dir, "water_use.json")
    
    water_use_data = generate_water_use_data()
    save_to_json(water_use_data, output_file)
    print(f"Created water usage data for {len(water_use_data)/3:.0f} days across 3 buildings.")
    print(f"Total entries: {len(water_use_data)}")
    print(f"Data saved to: {output_file}")