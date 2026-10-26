
# Boston Housing Price Prediction using Linear Regression

## 📌 Project Overview

This project implements a **Multiple Linear Regression** model using Python and Scikit-learn to predict the median value of owner-occupied homes (`MEDV`) using the Boston Housing dataset.

The model is trained on housing-related features and evaluated on separate training and testing datasets to understand its prediction performance.

## 🎯 Objectives

-   Load and process the Boston Housing dataset using Pandas.
-   Separate input features (`X`) and the target variable (`y`).
-   Split the dataset into training and testing sets.
-   Train a Linear Regression model using Scikit-learn.
-   Evaluate model performance using Mean Squared Error (MSE) and R² score.
-   Visualize actual versus predicted house prices using Matplotlib.

## 🛠️ Technologies Used

-   **Python** — Programming language
-   **Pandas** — Dataset loading and manipulation
-   **Scikit-learn** — Model training and evaluation
-   **Matplotlib** — Data visualization

## 📂 Dataset

**File:** `BostonHousing.csv`

The dataset contains information about housing characteristics and neighborhood conditions.

-   **Input features:** The selected columns from the dataset used for prediction.
-   **Target variable:** `MEDV`, the median value of owner-occupied homes, measured in thousands of dollars.

For example, a predicted `MEDV` of `25` represents a median home value of $25,000 in the dataset's original units.

Ensure that the CSV file contains the expected columns and is available at the file path specified in the Python code.

## ⚙️ Installation and Setup

### 1. Clone the repository

bash

```
git clone https://github.com/jvedant1001-ship-it/Machine-Learning-Lab.git
cd Machine-Learning-Lab

```

### 2. Create a virtual environment

bash

```
python -m venv venv

```

Activate it on Windows:

bash

```
venv\Scripts\activate

```

On macOS/Linux:

bash

```
source venv/bin/activate

```

### 3. Install dependencies

bash

```
pip install pandas scikit-learn matplotlib

```

### 4. Run the program

Navigate to the folder containing the Python script and dataset, then run:

bash

```
python your_script_name.py

```

Replace `your_script_name.py` with the actual Python filename.

## 🧠 Implementation

The project follows these steps:

1.  **Data loading:** Read `BostonHousing.csv` using Pandas.
2.  **Feature selection:** Select the input columns and target column.
3.  **Train-test split:** Divide the data into training and testing sets.
4.  **Model training:** Fit a Linear Regression model on the training data.
5.  **Prediction:** Generate predictions for both training and testing data.
6.  **Evaluation:** Calculate MSE and R² scores for both datasets.
7.  **Visualization:** Plot actual MEDV values against predicted MEDV values.

## 📊 Evaluation Metrics

### Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values. A lower MSE generally indicates more accurate predictions.

### R² Score

Measures how well the model explains the variation in the target variable. A score closer to 1 generally indicates a better fit.

## 📈 Visualization

The program generates an **Actual vs Predicted Values** scatter plot.

-   **Blue dots:** Actual and predicted house values for individual test samples.
-   **Red dashed line:** The ideal prediction line where predicted values equal actual values.

Points closer to the red line indicate more accurate predictions.

## ⚠️ Notes

-   The code assumes the target variable is in column index `13` and the input features are in columns `0` through `10`. Verify these indices against your CSV file.
-   The Boston Housing dataset is a legacy dataset and has known limitations. Use it for educational purposes rather than real-world housing valuation.
-   Model performance depends on the dataset, selected features, and train-test split.

## 👨‍💻 Author

**Vedant Joshi**

GitHub: [jvedant1001-ship-it](https://github.com/jvedant1001-ship-it)

----------

_Built as part of my hands-on learning journey in Machine Learning._
