# Creating Customer Segments

Reviewed unstructured data to understand the patterns and natural categories that the data fits into. Used multiple algorithms and both empirically and theoretically compared and contrasted their results. Made predictions about the natural categories of multiple types in a dataset, then checked these predictions against the result of unsupervised analysis.
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
python -m virtualenv customer_segments
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

In a terminal or command window, navigate to the  project directory `customer_segments/` (that contains this README) and run one of the following commands:

```bash
ipython notebook customer_segments.ipynb
```  
or
```bash
jupyter notebook customer_segments.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

### Data


The customer segments data is included as a selection of 440 data points collected on data found from clients of a wholesale distributor in Lisbon, Portugal. More information can be found on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Wholesale+customers).

Note (m.u.) is shorthand for *monetary units*.

**Features**
1) `Fresh`: annual spending (m.u.) on fresh products (Continuous); 
2) `Milk`: annual spending (m.u.) on milk products (Continuous); 
3) `Grocery`: annual spending (m.u.) on grocery products (Continuous); 
4) `Frozen`: annual spending (m.u.) on frozen products (Continuous);
5) `Detergents_Paper`: annual spending (m.u.) on detergents and paper products (Continuous);
6) `Delicatessen`: annual spending (m.u.) on and delicatessen products (Continuous);

## License
@ Kundan Kumar
This project is licensed under the MIT License [LICENSE.md](https://github.com/kundan7kumar/Machine_Learning/blob/master/Project/customer_segments/LICENSE.md) file for details


