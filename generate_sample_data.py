import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data():
    print("Generating sample weather data...")
    np.random.seed(42)
    dates = [datetime(2023, 1, 1) + timedelta(days=x) for x in range(730)]
    
    # Generate data
    df = pd.DataFrame({
        'Date': dates,
        'Temperature': np.random.normal(25, 8, 730),
        'Humidity': np.random.uniform(30, 90, 730),
        'Rainfall': np.random.exponential(2, 730) * np.random.binomial(1, 0.3, 730),
        'Wind_Speed': np.random.uniform(0, 25, 730)
    })
    
    # Add some noise (missing values) for cleaning task
    mask = np.random.random(730) < 0.02
    df.loc[mask, 'Temperature'] = np.nan
    
    df.to_csv('sample_weather_data.csv', index=False)
    print("✓ Created 'sample_weather_data.csv'")

if __name__ == "__main__":
    generate_data()
