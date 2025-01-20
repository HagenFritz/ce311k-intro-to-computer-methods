from errno import EDEADLK
import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import datetime, timedelta
import os

def load_office_hours(config_file):
    """Load office hours from a JSON config file."""
    with open(config_file, 'r') as f:
        return json.load(f)

def create_calendar(oh_data):
    """Create a calendar-like visualization of office hours."""
    # Setup the plot
    fig, ax = plt.subplots(figsize=(15, 8))
    
    # Define the days and times
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = [f"{hour:02d}:00" for hour in range(8, 20)]  # 8 AM to 7 PM
    
    # Create the grid
    n_times = len(times)
    n_days = len(days)
    
    # Draw horizontal and vertical grid lines
    for i in range(n_times + 1):
        ax.axhline(i, color='gray', linewidth=0.5)
    for i in range(n_days + 1):
        ax.axvline(i, color='gray', linewidth=0.5)
    
    # Plot the office hours blocks
    for day, slots in oh_data.items():
        day_idx = days.index(day)
        for slot in slots:
            # Convert time strings to hours and minutes
            start_time = datetime.strptime(slot['start'], '%H:%M')
            end_time = datetime.strptime(slot['end'], '%H:%M')
            
            # Calculate position and duration in hours
            start_hour = start_time.hour + start_time.minute/60.0 - 7  # Subtract 7 to align with our grid
            end_hour = end_time.hour + end_time.minute/60.0 - 7
            duration = end_hour - start_hour
            
            # Adjust y-position for reversed time axis
            y_pos = n_times - start_hour - duration
            
            if slot["name"] == "Class":
                rect = plt.Rectangle(
                    (day_idx, y_pos),
                    1, duration,
                    facecolor='firebrick',
                    alpha=0.5,
                    edgecolor='black',
                    linewidth=2
                )
            elif slot["name"].startswith("Lab"):
                rect = plt.Rectangle(
                    (day_idx, y_pos),
                    1, duration,
                    facecolor='goldenrod',
                    alpha=0.5,
                    edgecolor='black',
                    linewidth=2
                )
            else:
                rect = plt.Rectangle(
                    (day_idx, y_pos),
                    1, duration,
                    facecolor='cornflowerblue',
                    alpha=0.5,
                    edgecolor='black',
                    linewidth=2
                )

            ax.add_patch(rect)
            
            # Add text (adjusted for reversed axis)
            ax.text(
                day_idx + 0.02,
                y_pos + duration - 0.1,
                slot['name'],
                ha='left',
                va='top',
                fontsize=12,
                wrap=True,
                fontweight='bold'
            )
            
            # Add location text
            ax.text(
                day_idx + 0.02,
                y_pos + duration - 0.38,  # Offset slightly below the name
                slot['location'],
                ha='left',
                va='top',
                fontsize=12,
                wrap=True
            )
    
    # Customize the plot
    ax.set_xticks(np.arange(len(days)) + 0.5)
    ax.set_xticklabels(days, fontsize=16)
    ax.set_yticks(np.arange(len(times)))
    ax.set_yticklabels(reversed(times), fontsize=16)
    
    # Remove axis labels and move x-axis to top
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.xaxis.set_ticks_position('top')
    
    # Remove tick marks but keep grid
    ax.tick_params(axis='x', length=0)
    ax.tick_params(axis='y', length=0)
    
    # Set axis limits
    ax.set_xlim(0, n_days)
    ax.set_ylim(0, n_times)
    
    # Adjust layout
    plt.tight_layout()
    return fig

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(script_dir, 'oh_config.json')
    
    # Load the office hours data
    oh_data = load_office_hours(config_file)
    
    # Create and save the calendar
    fig = create_calendar(oh_data)
    output_file = os.path.join(script_dir, 'office_hours_schedule.png')
    fig.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Calendar saved to: {output_file}")

if __name__ == "__main__":
    main()