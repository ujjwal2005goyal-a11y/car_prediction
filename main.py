import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle

# Load dataset
df = pd.read_csv("car_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove invalid prices
df = df[df["price"] != "Ask For Price"]

# Clean price
df["price"] = df["price"].str.replace(",", "")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Clean kms
df["kms_driven"] = df["kms_driven"].str.replace(" kms", "")
df["kms_driven"] = df["kms_driven"].str.replace(",", "")
df["kms_driven"] = pd.to_numeric(df["kms_driven"], errors="coerce")

# Clean year
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

# Drop missing
df = df.dropna()

# Feature engineering
from datetime import datetime
current_year = datetime.now().year
df["Car_Age"] = current_year - df["Year"]

# Drop unnecessary columns
df = df.drop(["Car_Name", "Year"], axis=1)

# Convert categorical → numeric
df = pd.get_dummies(df, drop_first=True)

# Split
X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(X.columns, open("columns.pkl", "wb"))

print("✅ Model trained successfully")