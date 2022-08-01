# Water_wells_Project

*by: __Nick Kimani__*

# Repo structure

```
├── Code                            # Contains anything that is coding oriented
│   ├── custom_functions.py
│   ├── Water_wells EDA.ipynb
│   └── Water_wells ML.ipynb
├── Data                            # Contains all data used in solving this project
│   ├── Cleaned_data.csv 
│   ├── training features.csv
│   └── training targets.csv
├── Images                          # Contains all images used or produced in this project
│   ├── Images produced from the notebooks e.g Confusion matrix of extraction_type_class and status_group.png
│   ├── Images imported for use in the notebooks e.g water_wells.png
├── Proj 3 Alt.pdf                  # Project Presentation file
└── README.md
```

[Link to the presentation file.](https://github.com/Nickimani/Water_wells_Project/blob/main/Proj%203%20Alt.pdf)

# Problem Understanding

Tanzania, as a developing country, struggles with providing clean water to its population of over 57,000,000. There are many water points already established in the country, some are functional, but some are in need of repair while others have failed altogether.

The Government of Tanzania is interested in:

> 1) Finding out the waterpoints in need of repairs and those that have completely failed.

> 2) Identifying patterns in waterpoints that don't function as desired.

This can be done by building a __classifier__ that takes in the attributes of a waterpoint and determines whether it is __functional__, __functional needs repair__ or __nonfunctional__. 

By being able to build a good classifier, the government can be able to:

> 1) Easily determine waterpoints that are in need of repairs and those that have completely ceased functioning.

> 2) Identify patterns in non-functional waterpoints and guide against them when building wells in future.

By building a good classifier, the lives of the people of Tanzania can be changed. In that their *living standards* will be *improved* due to having better access to clean water.

# Data understanding 

The original dataset to be used in solving this problem had 59400 rows of data. However, after some adjustments, the data that made it to modelling has __57,336__ rows. This is due to some cleaning that I did. 

Each __row__ in the data represents a __waterpoint__.

The original data had a lot of features and most of them were explaining the same thing but in a hierachy. The features that made it to the model are:

The predictors:

    1. amount_tsh - Total Static Head (amount water available to waterpoint)
    2. gps_height - Altitude of the well
    3. longitude - GPS coordinate
    4. latitude - GPS coordinate
    5. population - Population around the well
    6. extraction_class - The kind of extraction the waterpoint uses
    7. management_group - How the waterpoint is managed
    8. payment_type - What the water costs
    9. quality_group - The quality of the water
    10. quantity_group - The quantity of water
    11. source_class - The source of the water
    12. type_group - The kind of waterpoint
    13. public_meeting - True/False
    14. scheme_management - Who operates the waterpoint
    15. permit - If the waterpoint is permitted
    16. region_code - Geographic location (coded)
    17. age - The age of a well at the time it was recorded
    
The target:

    1. status_group - The target feature for this problem
    
- It has 3 classes therein, namely:
    
    1. functional - The well is operational and there are no repairs needed
    2. functional needs repair - The well is operational, but needs repairs
    3. non functional - The well is not operational

This sort of data is enough for building a model.

# Data cleaning

In cleaning the data I first checked for duplicates and found none. Then I proceeded to check for nan values in the data and found a couple of them in various features. I filled these nan values with the medians for the respective features. 

After that I eliminated the features that are hierachical by dropping those features in the hierachy group that give too much or too little. In short I looked for a balance in the details provided by a feature.

Then I did some feature engineering and created an `age` feature by using the `date_recorded` and `costruction_year` features.

# Modelling

Having cleaned the data and feature selected those important to this problem, I began modelling. 

I had the approach of using a tree classifier and a KNN classifier then picking either of the two depending on which one performs better.

After some model tuning I found that the KNN classifier performs better. Although the difference in accuracy between it and the tree classifier was below 0.0008 the tree classifier had a considerably larger log loss. So I decided that the KNN performs better of the two.

However, I ended up using a random forest ensemble as the final model because it had a higher accuracy and substantially lower log loss. Although random forest usually takes longer to train and has a high computational complexity, for this problem, I decided to use it as the time it takes to compute is bearable considering the accuracy that it has.

The scoring method used is accuracy score. As I was working the problem I discovered that accuracy, recall, and precision scores for this problem output the same values. S I decided to stick to accuracy score as it is appropriate for this problem and it's also easy to interpret.

# Results

![final_model_av_accuracy](https://user-images.githubusercontent.com/104377216/182044374-5dd7a4c6-ca76-40e7-99ff-af3ba5782fb8.png)

The __final model__ I used is a __random forest ensemble__. It had an average accuracy score of __~79.4%__.

![final_model_class_accuracy](https://user-images.githubusercontent.com/104377216/182044377-ccae2091-1cbf-4066-9623-477e5a315162.png)

However, when __breaking down__ the above score, the accuracy when predicting the __majority class__ (functional) is __~92%__ and that for the __non functional__ class (not minority) is __~72%__. Considering that some potentially useful features were dropped due to some reasons I point out in the notebook, this accuracies are good enough to justify applying the model.
