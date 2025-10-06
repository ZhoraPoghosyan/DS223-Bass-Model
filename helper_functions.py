import pandas as pd
import numpy as np

# Function to load and process smart home expenditure data
def load_expenditure_data(path: str) -> pd.DataFrame:
    excel_file = pd.ExcelFile(path)
    data = pd.read_excel(excel_file, sheet_name='Data', skiprows=4, header=None)
    data = data.iloc[:, 1:]
    data.columns = ["Report_Year", "Spending_Amount"]
    data = data.dropna().reset_index(drop=True)
    data["Report_Year"] = data["Report_Year"].astype(str).str.extract(r'(\d+)').astype(int)
    data["Spending_Amount"] = data["Spending_Amount"].astype(float)
    return data.head(6)

# Function to compute adoption using the Bass Diffusion Model
def compute_bass_adoption(time, innovation_rate, imitation_rate, market_size):
    adoption_curve = market_size * (((innovation_rate + imitation_rate) ** 2 / innovation_rate) * np.exp(-(innovation_rate + imitation_rate) * time)) / \
                     ((1 + (imitation_rate / innovation_rate) * np.exp(-(innovation_rate + imitation_rate) * time)) ** 2)
    return adoption_curve
