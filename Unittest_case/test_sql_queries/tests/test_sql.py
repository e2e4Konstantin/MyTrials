from code_to_test import function_to_tets
from unittest import mock
import pandas as pd


@mock.patch('code_to_test.sqlite3')
@mock.patch('code_to_test.pd.read_sql_query')
def test_sql_query(read_sql_query_mock, sqlite_mock):
    read_sql_query_mock.return_value = pd.DataFrame({'STD_ADDRESS': ['address 1'],
                                                     'STD_CITY': ['city 1'],
                                                     'STD_STATE': ['state 1']})
    assert function_to_tets().to_dict(orient='list') == {'STD_ADDRESS': ['address 1'],
                                                         'STD_CITY': ['city 1'],
                                                         'STD_STATE': ['state 1']}