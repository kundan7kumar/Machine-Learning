# Titanic Survival Exploration

Decision functions to predict survival outcomes from the 1912 Titanic disaster based on each passenger’s features, such as sex and age. A simple algorithm and increase its complexity until accurately predict the outcomes for at least 80% of the passengers in the provided data. 
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
python -m virtualenv titanic_survival_exploration
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

In a terminal or command window, navigate to the  project directory `titanic_survival_exploration/` (that contains this README) and run one of the following commands:

```bash
ipython notebook titanic_survival_exploration.ipynb
```  
or
```bash
jupyter notebook titanic_survival_exploration.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

### Data
The dataset used in this project is included as `titanic_data.csv`. This dataset is provided by Udacity and contains the following attributes:

**Features**
- `pclass` : Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
- `name` : Name
- `sex` : Sex
- `age` : Age
- `sibsp` : Number of Siblings/Spouses Aboard
- `parch` : Number of Parents/Children Aboard
- `ticket` : Ticket Number
- `fare` : Passenger Fare
- `cabin` : Cabin
- `embarked` : Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

**Target Variable**
- `survival` : Survival (0 = No; 1 = Yes)

## License
@ Kundan Kumar
This project is licensed under the MIT License [LICENSE.md](https://github.com/kundan7kumar/Machine_Learning/blob/master/Project/finding_donors/LICENSE.md) file for details


