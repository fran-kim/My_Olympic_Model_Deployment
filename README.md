# My Olympic Model Deployment

# This is a project elaborating how to deploy a Machine Learning model using Flask API
Using a dataset regarding Summer Olympics Weightlifting records from 2000 to 2020 (https://www.kaggle.com/yuxinc/summer-olympics-weightlifting-records-2000-to-2020?select=to_csv_out.csv), I created a machine learning model that is able to predict how much total weight you can lift based on your bodyweight (If you trained like an olympian of course).

Prerequisites
You must have Scikit Learn, Pandas (for Machine Learning Model) and Flask (for API) installed.

Optional
Seaborn, matplotlib for cleaning, analyzing, and visualizing data prior to creating the model (seen in the MachineLearningModel Python Notebook)


Project Structure
This App has four major parts :
1. app.py - This contains code fot our Machine Learning model to predict employee salaries absed on trainign data in 'hiring.csv' file.
2. weights.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. templates folder - This folder contains the HTML template (index.html and sub.html) to allow user to enter body weight in pounds  and displays the predicted total olympic lift.


