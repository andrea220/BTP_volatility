import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import statsmodels.api as sm
from statsmodels import regression, stats

def linreg(X,Y):
    # Running the linear regression
    x = sm.add_constant(X) # Add a row of 1's so that our model has a constant term
    model = regression.linear_model.OLS(Y, x).fit()
    return model.params[0], model.params[1] # Return the coefficients of the linear model

def load_BTP_curve(path):
    df = pd.read_excel(path, skiprows=4)
    df.set_index("Unnamed: 1", drop = True, inplace= True)
    df =df[df.columns[df.columns.str.startswith("GBTPGR")]]
    df = df.iloc[2:, :]
    df.columns = [2,3,4,5,6,7,8,9,10,15,20,30]
    df.columns.name = "Tenor"
    df.index.name = "Date"
    df = df.astype('float')
    return df/100

def regime_changes(breakpoint, benchmark):
    xs = np.arange(len(benchmark))
    xs2 = np.arange(breakpoint)
    xs3 = np.arange(len(benchmark) - breakpoint)
    ##
    a, b = linreg(xs, benchmark)
    a2, b2 = linreg(xs2, benchmark[:breakpoint])
    a3, b3 = linreg(xs3, benchmark[breakpoint:])
    #
    Y_hat = pd.Series(xs * b + a, index=benchmark.index)
    Y_hat2 = pd.Series(xs2 * b2 + a2, index=benchmark.index[:breakpoint])
    Y_hat3 = pd.Series(xs3 * b3 + a3, index=benchmark.index[breakpoint:])
    benchmark.plot()
    Y_hat.plot(color='y')
    Y_hat2.plot(color='r')
    Y_hat3.plot(color='r')
    plt.ylabel('Price');

