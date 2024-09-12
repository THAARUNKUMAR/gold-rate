import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv(r"C:\Users\TK\Downloads\archive (3)\annual_gold_rate.csv")


# Data preprocessing
data.fillna(0, inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Day'] = data['Date'].dt.day
data = data.drop('Date', axis=1)

# Splitting dataset
X = data.drop('INR', axis=1)
Y = data['INR']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, Y_train)

# Define the front-end application
def predict_inr():
    try:
        # Get user input values from the form
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        usd = float(usd_entry.get())
        eur = float(eur_entry.get())
        gbp = float(gbp_entry.get())
        aed = float(aed_entry.get())
        cny = float(cny_entry.get())

        # Prepare the input DataFrame
        user_input = pd.DataFrame({
            'Day': [day],
            'Month': [month],
            'Year': [year],
            'USD': [usd],
            'EUR': [eur],
            'GBP': [gbp],
            'AED': [aed],
            'CNY': [cny]
        }, columns=X.columns)

        # Predict the INR value
        predicted_inr = model.predict(user_input)
        result_label.config(text=f"Predicted INR Value: {predicted_inr[0]:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create the Tkinter window
root = tk.Tk()
root.title("Gold Rate Prediction")

# Create and place input fields and labels
tk.Label(root, text="Day:").grid(row=0, column=0)
day_entry = tk.Entry(root)
day_entry.grid(row=0, column=1)

tk.Label(root, text="Month:").grid(row=1, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1)

tk.Label(root, text="Year:").grid(row=2, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1)

tk.Label(root, text="USD:").grid(row=3, column=0)
usd_entry = tk.Entry(root)
usd_entry.grid(row=3, column=1)

tk.Label(root, text="EUR:").grid(row=4, column=0)
eur_entry = tk.Entry(root)
eur_entry.grid(row=4, column=1)

tk.Label(root, text="GBP:").grid(row=5, column=0)
gbp_entry = tk.Entry(root)
gbp_entry.grid(row=5, column=1)

tk.Label(root, text="AED:").grid(row=6, column=0)
aed_entry = tk.Entry(root)
aed_entry.grid(row=6, column=1)

tk.Label(root, text="CNY:").grid(row=7, column=0)
cny_entry = tk.Entry(root)
cny_entry.grid(row=7, column=1)

# Button to trigger prediction
predict_button = tk.Button(root, text="Predict INR", command=predict_inr)
predict_button.grid(row=8, column=1)

# Label to display prediction result
result_label = tk.Label(root, text="")
result_label.grid(row=9, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
