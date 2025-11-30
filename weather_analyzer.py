import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Setup
OUTPUT_DIR = 'output'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("--- Starting Weather Analysis ---")
    
    # 1. Load Data
    print("1. Loading Data...")
    df = pd.read_csv('sample_weather_data.csv')
    
    # 2. Clean Data
    print("2. Cleaning Data...")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.dropna(subset=['Temperature'])
    df['Rainfall'] = df['Rainfall'].fillna(0)
    df['Month'] = df['Date'].dt.month_name()
    
    # 3. Statistical Analysis
    print("3. Computing Statistics...")
    stats = {
        'mean_temp': df['Temperature'].mean(),
        'max_rain': df['Rainfall'].max(),
        'mean_humid': df['Humidity'].mean()
    }
    
    # 4. Visualization
    print("4. Generating Plots...")
    
    # Plot A: Temperature Trend
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Temperature'], color='#d62728')
    plt.title('Daily Temperature Trend')
    plt.xlabel('Date')
    plt.ylabel('Temp (°C)')
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{OUTPUT_DIR}/temperature_trends.png', dpi=300)
    plt.close()
    
    # Plot B: Rainfall Bar Chart
    plt.figure(figsize=(10, 6))
    monthly_rain = df.groupby('Month')['Rainfall'].sum().sort_values()
    plt.bar(monthly_rain.index, monthly_rain.values, color='#1f77b4')
    plt.title('Total Rainfall by Month')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/monthly_rainfall.png', dpi=300)
    plt.close()
    
    # Plot C: Scatter
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Temperature'], df['Humidity'], alpha=0.5, c='green')
    plt.title('Temperature vs Humidity')
    plt.xlabel('Temp (°C)')
    plt.ylabel('Humidity (%)')
    plt.grid(True)
    plt.savefig(f'{OUTPUT_DIR}/humidity_vs_temp.png', dpi=300)
    plt.close()

    # 5. Export
    print("5. Exporting Reports...")
    df.to_csv(f'{OUTPUT_DIR}/cleaned_weather_data.csv', index=False)
    
    with open(f'{OUTPUT_DIR}/summary_report.md', 'w') as f:
        f.write(f"# Weather Analysis Report\n\n")
        f.write(f"- **Average Temp:** {stats['mean_temp']:.2f}°C\n")
        f.write(f"- **Max Rainfall:** {stats['max_rain']:.2f}mm\n")
        f.write(f"- **Avg Humidity:** {stats['mean_humid']:.2f}%\n")
        
    print("✓ Analysis Complete! Check the 'output' folder.")

if __name__ == "__main__":
    main()

