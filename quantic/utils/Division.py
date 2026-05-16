# imports
from pathlib import Path


# functions
def Divide(
    value : float | int
) -> tuple[float, int]:
    
    # docstring
    '''

        Paramters
        ---------

            value : float | int
                The value to be divided

        Returns
        -------

            tuple[float, int]
                The divided number & the amount of divides

    '''
    
    # init variables
    divides : int = 0
    flag : bool = True

    # iterate
    while flag is True:

        # verify if ::value is under 1000
        if value <1000:

            flag : bool = False
            break

        # divide by 1000 & increase divides
        value : float = value /1000
        divides : int = divides +1

    # force ::value to be rounded to two decimal places
    value : float = round(
        number=value,
        ndigits=2
    )

    # return correct variables
    return value, divides

