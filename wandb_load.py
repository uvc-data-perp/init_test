import wandb
import pandas as pd

def load_data(file_path):
    data = pd.read_csv("InjectionMolding_Raw_Data.csv")
    wandb.init(project="data-preprocessing")
    wandb.log({"raw_data": wandb.Table(dataframe=data.head())})
    return data