#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here

    errors = []
    for i in range(len(predictions)):
        errors.append([net_worths[i][0] - predictions[i][0], i]) 
    
    def sortByValue(val):
        return val[0] * val[0]

    errors.sort(key=sortByValue, reverse=True)
    ###print errors

    del errors[:9]

    print len(errors)

    for i, val in enumerate(errors):
        cleaned_data.append([ages[val[1]], net_worths[val[1]], val[0]])

    return cleaned_data

