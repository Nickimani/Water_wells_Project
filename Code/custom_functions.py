import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

# # Make a plotting class
# class plottingData(object):
#     """ 
#     This class allows you to plot scatterplots, bar, histograms, and lineplots for your data.
#     """
#     def __init__(self, dataframe, xcols, ycols, ):
#         self.dataFrame = dataframe
#         self.x_cols = xcols
#         self.y_cols = ycols

## I'll get back to this later



# A function to drop columns
def drop_cols(dataframe, column=list(), inplace=False):
    'Takes in dataframe and column(s) and drops the specified columns.'
    
    if inplace == True:
        # for inplace dropping
        dataframe.drop(columns=column, inplace=True)
        
        return dataframe    
    else:
        # otherwise
        return dataframe.drop(columns=column, inplace=False)
    


# A function that returns a descending sorted list of values in a series
def sorted_series(df, column):
    "Sorts a column in a dataframe in descending order."
    # sort the column
    sorted_series = df[column].sort_values(ascending=False)
    
    return sorted_series



# A function for plotting scatterplots
def scatterPlot(dataframe, xcol, ycol):
    """
    A function that takes in a dataframe and x and y columns that are involved in the plotting. 
    The xcol and ycol should be in the same dataframe.
    Returns a scatterplot of the columns.
    """    
    # set the figure and axes
    fig, ax = plt.subplots(figsize=(7, 5))
    # plot the scatterplot chart
    dataframe.plot(x = xcol, 
                   y = ycol,
                   kind = 'scatter',
                   ax = ax,
                   title = f'Scatterplot of {xcol} against {ycol}.',
                   xlabel = xcol,
                   ylabel = ycol
                  );



# A function to plot a confusion matrix
def confusionMatrix(dataframe, xcol, ycol):
    """
    Takes in a dataframe, xcol and ycol that sould be in the dataframe and plots a confusion matrix for the columns specified. 
    Returns a confusion matrix.
    """
    # make a cross tab of the columns in use
    # and eliminate the 'All' column and row that come with the result
    confusion_matrix = pd.crosstab(dataframe[ycol], dataframe[xcol], rownames=[ycol], colnames=[xcol], margins=True, ).iloc[:-1, :-1]
    
    # create the axes
    fig, ax = plt.subplots(figsize=(7, 5))
    
    # plot a heatmap of the confusion matrix created above
    sns.heatmap(confusion_matrix, 
                # setting the axis
                ax = ax,
                # enabling labels
                annot = True,                
               );

    
# A function for plotting a histogram
def histPlot(dataframe, column):
    """
    Takes in a dataframe and a column of continuous data and returns a histogram of the column.
    """
    # set the figure
    fig, ax = plt.subplots(figsize=(7, 5))
    x = dataframe[column]
    
    # plot the chart
    # bar hist
    ax.hist(x, bins=100, density=True)
    # line hist
    ax.hist(x, bins=100, density=True, histtype='step')
    
    # set the details
    ax.set_xlabel(column)
    ax.set_ylabel('Density')
    ax.set_title(f'A histogram of {column}.');
    


# A function for plotting a bargraph 
def barPlot(dataframe, column):
    """
    Takes in a dataframe and a column of categorical data and returns a bargraph of the column.
    """
    # set the figure
    fig, ax = plt.subplots(figsize=(7, 5))
    x = dataframe[column]
    
    # plot the chart
    ax.bar(x, x)    
    
    # set the details
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    ax.set_title(f'A bargraph of {column}.');