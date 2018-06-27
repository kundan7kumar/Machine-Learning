# Predicting Boston Housing Prices

Built a model which can predict the value of a given house in the Boston real estate market using various statistical analysis tools. Predicted the optimal price for the selling of the house using machine learning.

### Prerequisites

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. Make sure that you select the Python 2.7 installer.

### Installation

A step by step tells how to get a development env running.

First step is to create virtual environment

```
python -m pip install --user virtualenv
```

And then create virtual environment

```
python -m virtualenv boston_housing
```
Now activate virtual environment

```
source env/bin/activate
```
In the virtual environment,install the packages mentioned above.

```
pip install numpy pandas 
```
Install the more packages in the virtual Environment.

```
python -mpip install matplotlib
```
```
pip install -U scikit-learn
```
```
python -m pip install jupyter
```
Also, You can install ananconda which has packages inbuilt to it.

### Run

In a terminal or command window, navigate to the  project directory `boston_housing/` (that contains this README) and run one of the following commands:

```bash
ipython notebook boston_housing.ipynb
```  
or
```bash
jupyter notebook boston_housing.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

### Data

The modified Boston housing dataset consists of 489 data points, with each datapoint having 3 features. This dataset is a modified version of the Boston Housing dataset found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Housing).
**Features**
1.  `RM`: average number of rooms per dwelling
2. `LSTAT`: percentage of population considered lower status
3. `PTRATIO`: pupil-teacher ratio by town

**Target Variable**
4. `MEDV`: median value of owner-occupied homes

## License
@ Kundan Kumar
This project is licensed under the MIT License [LICENSE.md](https://github.com/kundan7kumar/Machine_Learning/blob/master/Project/boston_housing/LICENSE.md) file for details


