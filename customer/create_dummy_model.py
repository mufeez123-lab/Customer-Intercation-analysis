import joblib
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Create a simple dummy model
model = RandomForestRegressor(n_estimators=10, random_state=42)

# Train it on some dummy data
X = np.random.rand(100, 3)  # Age, Income, Sentiment
y = np.random.randint(1, 100, 100)  # Random spending scores
model.fit(X, y)

# Save the model
joblib.dump(model, "spending_score_predictor.pkl") 