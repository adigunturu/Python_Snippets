import numpy as np

#Cronbach's Alpha is often used to mesure relatabilty between 2 or more variables (in experiment design)
def CronbachAlpha(dataframe):
    dataframe = np.asarray(dataframe)
    datavars = dataframe.var(axis=0, ddof=1)
    tscores = dataframe.sum(axis=1)
    nitems = dataframe.shape[1]

    return (nitems / (nitems-1)) * (1 - (datavars.sum() / tscores.var(ddof=1)))
