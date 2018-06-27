# Train a Smartcab How to Drive

Applied reinforcement learning to build a simulated vehicle navigation agent. This project involved modeling a complex control problem in terms of limited available inputs, and designing a scheme to automatically learn an optimal driving strategy based on rewards and penalties. 
### Prerequisites

This project requires **Python 2.7** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [Pygame](https://www.pygame.org/wiki/GettingStarted/)

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
python -m virtualenv Smartcab
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

In a terminal or command window, navigate to the  project directory `smartcab/` (that contains this README) and run one of the following commands:

```bash
python smartcab/agent.py
```  
or
```bash
python -m smartcab.agent
```
This will run the agent.py file and execute your agent code.
This will open the Jupyter Notebook software and project file in your browser.

## License
@ Kundan Kumar
This project is licensed under the MIT License [LICENSE.md](https://github.com/kundan7kumar/Machine_Learning/blob/master/Project/smartcab/LICENSE.md) file for details


