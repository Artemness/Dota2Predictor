# Dota2Predictor
Predict Dota 2 Winner Given Heros

## Overview:
* Pulled about 5700 professional matches from OpenDota API utilizing requests
* Substituted hero ids with hero names in the dataframe
* Created a dummy variable dataframe for the hero picks for each side
* Ran and optimized Random Forest and Light GBM Classifier Models
* Pickled the Light GBM Model
* Created a Django Interface for Users to use the model

## Pulling Data  
* Utilized OpenAPI to pull hero and win data for 10 heros per match for over 5500 professional matches.

## Data Cleaning and Feature Engineering:
After scraping the data I needed to clean it up for use in the model. Made the following changes:  
* Cleaned up various issues related to apostrophes and spaces in the Hero names
* Did One Hot Encoding for hero name and side combinations
  * First created empty sets for each combination of hero and side
  * Created a loop which edited the hero name with the cleanup issues mentioned above
  * Checked if hero name appeared in one of five columns for each side
* Appended a 1 if hero was present on the side for that match and 0 if not
* Created a data frame off the set for hero and side combination and transposed said data frame
* Concatenated the data frames for each side

## Model Building:  
Created a LightGBM model and a Random Forest Model to predict which side would win the game.

## Model Performance:  
The Random Forest Model proved to be the most effective and outperformed the Light GBM model but not significantly. Therefore chose to package the Light GBM model for production due to better computing speed.  
* Random Forest: 96.5% Accuracy
* Light GBM = 96.4% Accuracy
