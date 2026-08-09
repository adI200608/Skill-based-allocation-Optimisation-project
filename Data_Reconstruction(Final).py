import pandas as pd

# Data reconstruction from previous model
data = [
    ("Andaman & Nicobar", 6.99, 9.7, 0.0003, 0.73, 9.1),
    ("Andhra Pradesh", 0.007, 3.0, 0.0697, -0.10, 4.7),
    ("Arunachal Pradesh", 0.036, 3.9, 0.0010, -0.69, 4.3),
    ("Assam", 0.002, 2.0, 0.0256, 1.00, 1.2),
    ("Bihar", 0.012, 13.3, 0.0897, 0.10, 10.5),
    ("Chandigarh", 0.031, 4.0, 0.0009, -3.41, 7.1),
    ("Chhattisgarh", 0.002, 3.1, 0.0196, -0.36, 5.1),
    ("Delhi", 0.009, 1.9, 0.0138, -0.14, 3.5),
    ("Goa", 6.99, 2.8, 0.0012, -4.49, 3.7),
    ("Gujarat", 6.99, 2.0, 0.0495, 0.03, 1.9),
    ("Haryana", 0.009, 9.0, 0.0208, 0.04, 7.4),
    ("Himachal Pradesh", 0.034, 5.2, 0.0056, 0.11, 4.5),
    ("Jammu & Kashmir", 0.004, 4.4, 0.0103, -0.53, 5.9),
    ("Jharkhand", 0.002, 5.4, 0.0269, -0.28, 7.3),
    ("Karnataka", 0.001, 2.3, 0.0500, -0.05, 4.1),
    ("Kerala", 0.009, 3.6, 0.0277, -0.26, 6.1),
    ("Ladakh", 0.004, 6.1, 0.0002, 61.30, 2.9),
    ("Madhya Pradesh", 0.007, 1.8, 0.0597, -0.13, 3.5),
    ("Maharashtra", 0.002, 2.0, 0.0921, -0.02, 5.2),
    ("Manipur", 6.99, 2.2, 0.0023, -18.30, 3.8),
    ("Meghalaya", 6.99, 1.5, 0.0024, -5.95, 2.1),
    ("Mizoram", 6.99, 0.6, 0.0009, -28.42, 1.1),
    ("Nagaland", 6.99, 4.1, 0.0015, -4.71, 8.5),
    ("Odisha", 0.001, 1.8, 0.0341, -0.25, 3.5),
    ("Punjab", 0.012, 5.8, 0.0227, -0.05, 7.0),
    ("Rajasthan", 0.007, 3.7, 0.0555, -0.06, 5.8),
    ("Sikkim", 0.204, 3.8, 0.0005, -4.32, 4.5),
    ("Tamil Nadu", 0.004, 4.3, 0.0592, -0.13, 5.2),
    ("Telangana", 0.007, 4.4, 0.0234, -0.04, 4.9),
    ("Tripura", 0.012, 1.4, 0.0030, -6.26, 3.2),
    ("Uttarakhand", 0.023, 4.5, 0.0084, -0.14, 6.9),
    ("Uttar Pradesh", 0.004, 2.4, 0.1660, -0.11, 4.2),
    ("West Bengal", 6.99, 2.2, 0.0749, -0.06, 3.5),
    ("Dadra & Nagar Haveli and Daman & Diu", 6.99, 2.5, 0.0003, -40.48, 4.2),
    ("Lakshadweep", 6.99, 11.1, 0.0001, -19.07, 13.4),
    ("Puducherry", 0.212, 5.6, 0.0010, -2.93, 6.7)
]

ri = [
    0.60, 0.70, 0.77, 0.86, 0.89, 0.03, 0.77, 0.02, 0.38, 0.57,
    0.65, 0.90, 0.73, 0.78, 0.61, 0.52, 0, 0.72, 0.55, 0.71,
    0.76, 0.48, 0.71, 0.83, 0.63, 0.75, 0.75, 0.52, 0.56, 0.74,
    0.70, 0.78, 0.68, 0.31, 0.23, 0.32
]

# Create DataFrame
df = pd.DataFrame(data, columns=["State/UT", "Wi", "Final UR", "Pi", "Ki Value", "Initial UR"])
df.insert(0, "No.", range(1, len(df) + 1))
df["Ri"] = ri

# Calculate coefficient and symbolic expression
df["Coefficient"] = df["Wi"] * df["Final UR"] * df["Pi"]
df["Expression"] = df.apply(
    lambda row: f"{row['Coefficient']:.6f} * (1 - x_{row['No.']} * {row['Ki Value']})", axis=1
)

# Final column arrangement
df = df[[
    "No.", "State/UT", "Initial UR", "Final UR", "Ki Value",
    "Wi", "Pi", "Ri", "Expression"
]]

# Export to CSV
df.to_csv("Final_Evaluated_Optimization_Model.csv", index=False)
print("File saved as 'Final_Evaluated_Optimization_Model.csv'")
