# pip install cudf-cu11 --extra-index-url=https://pypi.nvidia.com
# https://colab.research.google.com/drive/12tCzP94zFG2BRduACucn5Q_OcX1TUKY3?ncid=ref-inpa-686360-vt27#scrollTo=5EoQqNwsTqeP
# https://gist.github.com/Sentdex/469c30385d06719519af13125db85edc

import pandas as pd
# import numpy as np

df = pd.read_csv(
    r"F:\Temp\python_tests\202304.csv",
    names=[
        "Transaction_unique_identifier",
        "price",
        "Date_of_Transfer",
        "postcode",
        "Property_Type",
        "Old/New",
        "Duration",
        "PAON",
        "SAON",
        "Street",
        "Locality",
        "Town/City",
        "District",
        "County",
        "PPDCategory_Type",
        "Record_Status - monthly_file_only",
    ],
    dtype={"price": "int64"},
)

print(df.tail())
