import pandas as pd
import altair as alt

# Read in Data
cancer = pd.read_csv("data/wdbc.csv")
## Check format with first few rows
# print(cancer.head(5)) # not needed in output, just for testing

## Change label names
cancer["Class"] = cancer["Class"].replace({"M": "Malignant","B":"Benign"})

# Exploratory Data Analysis

## Proportions of each label

print(cancer["Class"].value_counts(normalize=True))

## ScatterPlots of observations - wont show in full code execution
perim_concav = alt.Chart(cancer).mark_circle().encode(
    x=alt.X("Perimeter").title("Perimeter (standardized)"),
    y=alt.Y("Concavity").title("Concavity (standardized)"),
    color=alt.Color("Class").title("Diagnosis")
)

rad_symm = alt.Chart(cancer).mark_circle().encode(
    x=alt.X("Radius").title("Radius (standardized)"),
    y=alt.Y("Symmetry").title("Symmetry (standardized)"),
    color=alt.Color("Class").title("Diagnosis")
) 
