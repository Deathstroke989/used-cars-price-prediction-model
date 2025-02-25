Used Car Price Prediction Model Description

This model predicts the price of a used car based on several features, utilizing a Random Forest Regressor. The process includes data preprocessing, feature encoding, model training, and deployment using Streamlit for user interaction.
Data Loading and Preprocessing:

    Data Loading: Reads a CSV file named "car2.csv" into a pandas DataFrame.

    Missing Value Handling: Removes rows with missing values to ensure data quality.

    Data Cleaning and Transformation:

        AskPrice: Cleans the AskPrice column by removing spaces and commas, then converts it to an integer type.

        kmDriven: Extracts the numeric part of the kmDriven column, removes commas, and converts it to an integer type.

        Dropping irrelevant features: Drops the 'PostedDate' and 'AdditionInfo' columns as they are deemed irrelevant for prediction.

    Feature Encoding:

        Label Encoding: Uses LabelEncoder from scikit-learn to convert categorical features (Brand, model, Transmission, Owner, FuelType) into numerical representations.

        Label Mapping: Stores the mapping between original categories and encoded numerical values for later interpretation and user input in the Streamlit app.

Model Training:

    Feature Selection: Selects the relevant features (Brand, model, Year, Age, kmDriven, Transmission, Owner, FuelType) as independent variables (X) and AskPrice as the dependent variable (y).

    Data Splitting: Splits the data into training and testing sets using train_test_split with an 80/20 ratio and a random_state for reproducibility.

    Model Initialization and Training: Initializes a RandomForestRegressor and trains it on the training data.

    Model Evaluation: Evaluates the model's performance using the test set and prints the R-squared score.

Streamlit Application:

    Streamlit Setup:

        Sets up a full-width layout for the Streamlit app.

        Adds a background image to enhance the user interface.

    User Interface:

        Header and Subheader: Displays a header "Car Price Prediction" and a subheader "Enter the data:".

        Instructions: Provides instructions to the user to enter numerical inputs based on the label mappings.

        DataFrames Display: Displays the label mappings for Brand, model, Transmission, Owner, and FuelType in separate columns to guide the user.

        Input Fields: Creates numerical input fields for each feature (Brand Value, Model Value, year Value, age Value, kmDriven, transmission, Owner Value, fuel type).

    Prediction:

        Collects the user inputs into a list.

        When the "Predict Price" button is clicked, the model predicts the car price based on the input features.

        Displays the predicted price to the user.

Key Components:

    Pandas: Used for data manipulation and preprocessing.

    Scikit-learn: Used for label encoding, data splitting, and training the Random Forest Regressor model.

    Streamlit: Used to create an interactive web application for users to input car features and get price predictions.

This model provides a user-friendly interface for predicting used car prices, leveraging a Random Forest Regressor trained on preprocessed and encoded data.# used-cars-price-prediction-model
