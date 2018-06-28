# Stock Market Prediction using Recurrent Neural Net(LSTM model)
### Project Description
In this project, we are going to predict the future closing value of a given stock over a period (next day) in the future. This project uses LSTM model (Long Short Term Memory networks) to predict the adjusted closing price of the google stock based on the historical datasets. Here, we will be going to predict the any given day price of the “GOOGL” stock from New York Stock Exchange Data-Sets
### Prerequisites

This project requires **Python 3** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [Keras](https://keras.io/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. Make sure that you select the Python 3 installer.

### Installation

A step by step tells how to get a development env running.

First step is to create virtual environment

```
python -m pip install --user virtualenv
```

And then create virtual environment

```
python -m virtualenv Capstone
```
Now activate virtual environment

```
source env/bin/activate
```
In the virtual environment,install the tensorflow mee.

```
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-1.0.1-cp35-cp35m-win_amd64.whl
```
Install the more packages like numpy scipy matplotlib,spyder.

```
conda create -n tensorflow python=3.5 numpy scipy matplotlib spyder
```
Install Keras
```
pip install keras
```
### Run

In a terminal or command window, navigate to the  project directory `Capstone/` (that contains this README) and run one of the following commands:

```bash
ipython notebook Stock_prediction.ipynb
```  
or
```bash
jupyter notebook Stock_prediction.ipynb
```

This will open the Jupyter Notebook software and project file in your browser.

## License
@ Kundan Kumar
This project is licensed under the MIT License [LICENSE.md](https://github.com/kundan7kumar/Machine_Learning/blob/master/Capstone-Project/LICENSE.md) file for details


