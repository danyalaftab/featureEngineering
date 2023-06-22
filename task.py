from teradataml import DataFrame
from aoa import (
    aoa_create_context,
)

def run(**kwargs):
    aoa_create_context()
    df = DataFrame.from_query("sel * from dbc.dbcinfo")
    print(df)
