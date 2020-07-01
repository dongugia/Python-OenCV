import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
input_data = sm.datasets.get_rdataset("Guerry", "HitsData").data

res= smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data= input_data).fit()

print(res.summary())
