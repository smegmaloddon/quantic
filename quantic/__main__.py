# imports
from pathlib import Path

# user imports
from quantic.utils import Division

# constants
SUFFIXES: list[str] = [
    'k', 'M', 'B', 'T', 'qd', 'Qn', 'sx', 'Sp', 'Oc', 'No', 'Dc', 'Ud', 'Dd', 'Td', 'qdD', 'QnD', 'sxD', 'SpD', 'OcD', 'NoD', 'Vg', 'UVg', 'DVg', 'TVg', 'qtV', 'QnV', 'SeV', 'SPG', 'OVG', 'NVG', 'Tg', 'UTg', 'DTg', 'TTg', 'qtTg', 'QnTg', 'SeTg', 'SpTg', 'OcTg', 'NoTg', 'QdTg', 'QnTg', 'SxTg', 'SpTG', 'OcTG', 'NoTG',
    'Qag', 'UQag', 'DQag', 'TQag', 'QtQag', 'QnQag', 'SxQag', 'SpQag', 'OcQag', 'NoQag', 'Qig', 'UQig', 'DQig', 'TQig', 'QtQig', 'QnQig', 'SxQig', 'SpQig', 'OcQig', 'NoQig', 'Sg', 'USg', 'DSg', 'TSg', 'QtSg', 'QnSg', 'SxSg', 'SpSg', 'OcSg', 'NoSg',
    'Og', 'UOg', 'DOg', 'TOg', 'QtOg', 'QnOg', 'SxOg', 'SpOg', 'OcOg', 'NoOg', 'Ng', 'UNg', 'DNg', 'TNg', 'QtNg', 'QnNg', 'SxNg', 'SpNg', 'OcNg', 'NoNg', 'Ce'
]

# functions
def Run(
    value : float | int,
    suffixes : list[str] = SUFFIXES
) -> str:
    
    # user error
    if len(
        suffixes
    ) is 0 or not isinstance(
        value, (float, int)
    ):
        
        raise Exception(
            'Parameters given do not match /or do not meet the requirements\n Check that suffixes are not empty & value is int | float'
        )

    # docstring
    '''
    
        Parameters
        ----------

            value : float | int
                The value to be divided & used for suffix

            suffixes : list[str]
                ::optional - Replacement for default suffixes

        Returns
        -------

            str
                The number & suffix

    '''

    # init variables
    placeholder : float
    divides : int 
    
    # fetch variables
    placeholder, divides = Division.Divide(
        value=value
    )

    # fetch suffix
    suffix : str = suffixes[divides -1] if len(
        suffixes
    ) >=divides and divides -1 >=0 else '' # if not found, use empty str

    # create number
    number : str = f'{placeholder}{suffix}'

    # return the ::number
    return number