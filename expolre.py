import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats



def chi2_test(data_for_category1, data_for_category2, alpha=.05):
    '''
    This function takes in two array-like objects of categorical data (two columns
    of a pandas dataframe is the intended use case) and uses scipy.stats to 
    conduct a chi^2 test for independence. 
    It prints crosstabs of the observed and expected values, and determines whether to 
    reject the null hypothesis based on a given value of alpha. 
    '''
    # create dataframe of observed values
    observed = pd.crosstab(data_for_category1, data_for_category2)
    
    # conduct test using scipy.stats.chi2_contingency() test
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    # round the expected values
    expected = expected.round(1)
    
    # output
    print('Observed\n')
    print(observed.values)
    print('------------------\nExpected\n')
    print(expected)
    print('------------------\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')
    
    # evaluate the hypothesis against the established alpha value
    if p < alpha:
        print('\nReject H0')
    else: 
        print('\nFail to Reject H0')




def dependent_churn(train):
    
    churn_rates = (pd.DataFrame(train.groupby(by='dependents_encoded').mean().churn_encoded)
                   .reset_index()
                   .sort_values(by='churn_encoded'))
    sns.barplot(data = churn_rates,
                x = 'dependents_encoded', 
                y = 'churn_encoded')
    plt.axhline(train.churn_encoded.mean(), 
                    ls='--', 
                    color='grey')
    plt.title('Churn Rate by Dependants')
    plt.show()