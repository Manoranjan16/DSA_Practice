import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    table_1 = person.drop(columns=['personId'])
    table_2 = address.drop(columns=['addressId'])
    table_1 = table_1[['firstName', 'lastName']]
    merged_table = pd.concat([table_1, table_2], axis=1)
    return merged_table

table_1 = {
    "personId": 1,
    "lastName": 'Doe',
    "firstName": 'John'
    
}
table_2 = {
    "addressId": 1,
    "Street": '123 Main St',
    "City": 'Anytown',
    "State": 'CA'
}
print(combine_two_tables(table_1, table_2))
