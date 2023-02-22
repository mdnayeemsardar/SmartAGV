import pandas as pd

# Replace "my_excel_file.xlsx" with the name of your Excel file
df = pd.read_excel("extracted_data.xlsx")

# Add 1.1 to the values in the first column
df.iloc[:, 0] += 1.1
# Add 7.0 to the values in the second column
df.iloc[:, 1] += 7.0


# Save the updated data to a new Excel file
# Replace "updated_excel_file.xlsx" with the desired name for the new file
df.to_excel("updated_excel_file.xlsx", index=False)

print("Values in first column and second column updated and saved to updated_excel_file.xlsx")
