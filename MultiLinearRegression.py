import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1 : Dataset
X = np.array([
    [1,7],
    [2,6],
    [3,7],
    [4,6],
    [5,8]
])  
Y = np.array([50,55,60,65,70])  
# Step 2 : Train model
model = LinearRegression()
model.fit(X, Y)

# Step 3 : Print coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
