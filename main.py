import typer
import pandas as pd
import numpy as np


def main(num_rows: int, num_cols: int):
    # Define number of rows and columns for the random CSV file
    # Generate random data
    data = np.random.rand(num_rows, num_cols)

    # Create a DataFrame
    df = pd.DataFrame(data, columns=[f"Column_{i+1}" for i in range(num_cols)])

    # Save DataFrame to CSV
    file_path = "./random_data.csv"
    df.to_csv(file_path, index=False)


if __name__ == "__main__":
    typer.run(main)
