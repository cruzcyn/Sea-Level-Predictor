import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    # Create scatter plot
    plt.figure(figsize=(16, 8))
    plt.scatter(x, y)

    # Extend year range for prediction:
    years_extended = np.arange(x.min(), 2051, 1)

    # Create and draw the first best fit line, extended:
    first_result = linregress(x, y)
    line = [first_result.slope*year + first_result.intercept for year in years_extended]

    plt.plot(years_extended, line, "r")


    # Create second line of best fit, going from the year 2000, 
    # to a prediction for year 2050
    second_df = df[df["Year"] >= 2000]
    second_x = second_df["Year"]
    second_y = second_df["CSIRO Adjusted Sea Level"]

    second_year_extend = np.arange(second_x.min(), 2051, 1)

    second_result = linregress(second_x, second_y)
    second_line = [second_result.slope*year + second_result.intercept for year in second_year_extend]

    plt.plot(second_year_extend, second_line, "g")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()