🌸 Iris Dataset — Simple Linear Regression

A beginner-friendly Machine Learning project that uses Simple Linear Regression to predict sepal width from sepal length using the Iris dataset and Python's Scikit-learn library.

📌 Project Overview

This project demonstrates the fundamentals of a supervised machine learning regression model. Using the Iris dataset, the model learns the relationship between two flower measurements and generates predictions that can be compared with the actual values.

The implementation focuses on understanding the model-training process, evaluating prediction errors, and visualizing model performance using Matplotlib.

🎯 Objectives
Understand the fundamentals of Simple Linear Regression.
Load and explore the Iris dataset using Scikit-learn.
Train a linear regression model using selected features.
Predict sepal width from sepal length.
Evaluate the model using Mean Squared Error (MSE) and the R² score.
Visualize actual versus predicted values using a scatter plot.
📊 Dataset Information

The project uses the built-in Iris dataset available through sklearn.datasets.

The dataset contains 150 flower samples across three Iris species. This implementation selects only the first 50 samples, corresponding to Iris setosa.

Parameter	Description
Dataset	Iris
Selected samples	50
Input feature (X)	Sepal length
Target variable (y)	Sepal width
Machine Learning task	Regression
Algorithm	Simple Linear Regression

Note: The model uses one input feature to predict one continuous numerical value.

🛠️ Technologies Used
Python — Programming language
Scikit-learn — Dataset loading, model training, and evaluation
Matplotlib — Data visualization
⚙️ How It Works
Load the dataset: Import the Iris dataset using datasets.load_iris().
Select features: Use sepal length as the independent variable and sepal width as the target.
Train the model: Fit a LinearRegression model on the selected 50 samples.
Generate predictions: Predict sepal width using the trained model.
Evaluate performance: Calculate MSE and the R² score.
Visualize results: Plot actual values against predicted values and add a reference line representing perfect predictions.
📈 Actual vs. Predicted Values

The visualization compares the actual sepal width values on the X-axis with the model's predicted sepal width values on the Y-axis.

Blue points: Individual actual-versus-predicted observations.
Red dashed line: The ideal reference line, where predicted values equal actual values.
Points closer to the line: Indicate smaller prediction errors.
Points farther from the line: Indicate larger prediction errors.

The plot provides a quick visual understanding of how closely the model's predictions match the observed values.

📏 Model Evaluation Metrics
Mean Squared Error (MSE)

MSE measures the average squared difference between actual and predicted values. Lower values indicate smaller prediction errors.

R² Score

The coefficient of determination, or R² score, measures how well the model explains the variation in the target variable relative to a baseline prediction. A score closer to 1 generally indicates a better fit.

The script prints both metrics to the console:

Train MSE = <calculated value>
Train R2 score = <calculated value>


The exact values are calculated when the script runs. These are training-set metrics because the model is evaluated on the same samples used for fitting.

🚀 Getting Started
Prerequisites

Make sure Python 3 and pip are installed on your system.

1. Clone the repository
git clone https://github.com/jvedant1001-ship-it/Machine-Learning-Lab.git

2. Navigate to the project directory
cd Machine-Learning-Lab

3. Install the dependencies
pip install scikit-learn matplotlib

4. Run the Python script
python Proj_01_IRIS_Linear_Regression.py


The program prints the training MSE and R² score, then displays the actual-versus-predicted scatter plot.

📂 Project File

Proj_01_IRIS_Linear_Regression.py

💡 Key Learnings

Through this project, I practiced:

Implementing a regression algorithm with Scikit-learn.
Selecting input features and target variables.
Training a model and generating predictions.
Evaluating regression performance with MSE and R².
Visualizing model predictions and interpreting residual differences.
🔭 Future Improvements
Split the dataset into training and testing sets.
Evaluate the model on unseen data.
Plot a regression line against the original observations.
Experiment with additional features and compare model performance.
Explore other regression algorithms and their evaluation metrics.
👨‍💻 Author

Vedant Joshi

GitHub: @jvedant1001-ship-it
LinkedIn: Vedant Joshi

⭐ If you find this project useful for learning the fundamentals of Machine Learning, feel free to explore the repository and share your feedback!

Part of my journey toward building practical skills in Python and Machine Learning.