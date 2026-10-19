import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


irisset = datasets.load_iris()


# Taking first 50 rows, first column as input
x = irisset.data[:50, 0:1]

# Taking first 50 rows, second column as output
y = irisset.data[:50, 1]

# Fitting the linear regression model
reg = LinearRegression().fit(x, y)

# Predicting values using the model
yPredict = reg.predict(x)

# Checking how accurate the predictions are
mse = mean_squared_error(y, yPredict)
r2 = r2_score(y, yPredict)

print('Train MSE =', mse)
print('Train R2 score =', r2)
print("\n")

# Plotting actual values against predicted values
plt.figure()
plt.scatter(y, yPredict, color='blue', alpha=0.6)

# This line shows where perfect predictions would lie
plt.plot([y.min(), y.max()], [y.min(), y.max()],
         color='red', linestyle='--')

# Adding labels and title to the graph
plt.title('Actual vs Predicted Values')
plt.xlabel('Actual SepalWidth')
plt.ylabel('Predicted SepalWidth')
plt.grid()
plt.show()
