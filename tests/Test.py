# imports
from pathlib import Path
import sys

# # redo root & insert into Path()
# root : Path = Path(
#     __file__
# ).resolve().parent.parent

# # change Path()
# sys.path.insert(
#     0, str(
#         root
#     )
# )

# import quantic
import quantic

if __name__ =='__main__':

    # test with massive number
    number : str = quantic.Run(
        value=123
    )
    
    print(
        f' - massive number : {number}'
    )

    # test with custom suffixes
    number : str = quantic.Run(
        value=123456789,
        suffixes=[
            'lzBozo', 'deez', 'sigma', 'ses'
        ]
    )

    print(
        f' - custom suffixes : {number}'
    )