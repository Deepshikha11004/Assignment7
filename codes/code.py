# code
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as ss
import numpy as np
import seaborn as sns
import weibull

# generate standard weibull distribution of different Shape parameter
gamma_1 = np.random.weibull(a=1,size=1000)
gamma_half = np.random.weibull(a=0.5,size=1000)
gamma_5 = np.random.weibull(a=5,size=1000)
gamma_10 = np.random.weibull(a=10,size=1000)

# plot different Weibull distribution
sns.set_style('darkgrid')
fig, ax = plt.subplots(2,2)
sns.histplot(gamma_1,kde=True,ax= ax[0,0] )
ax[0,0].set_title('Gamma = 1 ')
sns.histplot(gamma_half,kde=True, ax= ax[0,1], legend='Y=0.5')
ax[0,1].set_ylim([0,200])
ax[0,1].set_title('Gamma = 0.5 ')
sns.histplot(gamma_5,kde=True, ax= ax[1,0], legend='Y=5')
ax[1,0].set_title('Gamma = 5 ')
sns.histplot(gamma_10,kde=True, ax= ax[1,1], legend='Y=10')
ax[1,1].set_title('Gamma = 10 ')
plt.show()

# load dataset
specimen_strength = pd.read_csv('tensile strength.txt', header=None)
specimen_strength.head()

# perform weibull analysis
analysis=weibull.Analysis(specimen_strength[0])

# Here, we can fit using two method, mle (maximum likelihood)
# and lr (linear regression). Generally mle is better fit
analysis.fit(method='lr')

# print shape parameter (Beta) and scale parameter (eta)
print(f'shape Parameter: {analysis.beta: .02f}')
print(f'Scale Parameter: {analysis.eta: .02f}')

# print values of different parameters confidence interval
analysis.stats

# generate Weibull probplot
analysis.probplot()
