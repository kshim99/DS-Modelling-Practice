import pandas as pd
import altair as alt

# Read in Data
cancer = pd.read_csv("data/wdbc.csv")
# Check format with first few rows
print(cancer.head(5))


