import pandas as pd

# Replace "my_excel_file.xlsx" with the name of your Excel file
df = pd.read_excel("freeslide_1.xlsx")

# Extract columns 1, 3, and 5
new_df = df.iloc[:, [0, 2, 4]]

# Save the extracted data to a new Excel file
# Replace "extracted_data.xlsx" with the desired name for the new file
new_df.to_excel("extracted_data_1.xlsx", index=False)

print("Columns 1, 3, and 5 extracted and saved to extracted_data.xlsx")
