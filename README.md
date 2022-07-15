# Predicting Customer Churn

## About the Project
Using Telco Data we will be doing an in depth expoloratory data analysis to discover key drivers of churn. Using that analysis we will create features and develop a predictive machine learning model to estimate customer churn


### Data Dictionary


| Variable          | Meaning          |values          |

| -----------       | -----------                                               | -----------     |

| churn             | whether a customer has left the company (target variable) | Yes, No

| gender            | customer gender                                         | male, female    |

| senior_citizen    | whether a customer is a senior citizen                  | 0 (no), 1 (yes) |

| partner           | whether a customer has a partner                        | Yes, No         |

| dependents        | whether a customer has dependents                       | Yes, No         |

| tenure            | # of months a customer has been with Telco (truncated)  | 1 - 72          |

| phone_service     | whether a customer subscribes to phone service          | Yes, No                           |

| multiple_lines    | whether a customer subscribes to multiple phone lines   | Yes, No, No phone service         |

| online_security   | whether a customer subscribes to online security  | Yes, No, No internet service |

| streaming_tv      | whether a customer subscribes to television streaming | Yes, No, No internet service  |

| streaming_movies  | whether a customer subscribes to movie streaming services | Yes, No, No internet service  |

| paperless_billing | whether a customer has opted in to paperless billing  | Yes, No |

| monthly_charges   | total amount in dollars the customer pays each month  | 18.25 - 118.75  |

| contract_type     | duration of customer's current contract | Month-to-month, One-year, Two-year  |

| internet_service_type | type of internet service to which a customer subscribes | DSL, Fiber optic, No internet service |

| payment_type  | method of the customer's monthly payment  | Mailed check, Electronic check, Credit card (automatic), Bank transfer (automatic)  |

### Goals

By creating a predictive model and identifying customer churn we will be more able to proactively stop customer churn, increase the quality of our customer service, and through that increase profits.


### Initial Questions

1. How do average monthly charges affect churn?

2. Is demographic information such as sex, age, and dependent status affect churn?

3. How is churn affected by tenure?

### Planning

#### To prepare this data i used the following steps

1. Acquire the data using built functions

2. Clean and split data using built functions

3. Use matplotlib, seaborn, and dtale for exploratory data analysis

4. Find drivers of churn

5. Create baseline (73%)

6. Start modeling using selected features, with Decision tree, Random Forest, K-NN, and Logistic Regression

7. Choose the best model and test (logistic regression)

### How to Reproduce

to reproduce this project you will need to: 

- have a copy of Telco.csv

- clone this repository

- use the functions in .py files to acquire and clean data

- used libraries are numpy, pandas, matplotlib, seaborn, sklearn, and dtale


## Conclusion

Our logistic regression model has performed the best with **81% Accuracy** on future data.

We have also Identified some key predictors of churn as well as an 8% improvement over our baseline.

## Key Items

Attributes that contribute to customer churn:

- Customers are more likely to churn in the first **18 months**

- Churning customers have **higher** monthly charges, on average

- Senior citizens are **more** likely to churn

- People with dependents are **more** likely to churn

## Recomendations

- Batter introductory deals for 1 & 2 year contracts do get customers past the 18 month hump

- market towards families and people with dependants

## Next Steps

With more time I would like to gather more data on regional and economic status, as well as test additional models with more features. with this additional time we should hopefully be able to increase our accuracy to an even higher amount.













