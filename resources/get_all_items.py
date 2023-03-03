"""

    You must replace <FMI_1> with the table name
"""

import boto3, json


def get_all_items():
    import boto3

    DDB = boto3.resource('dynamodb', region_name='us-east-1')

    table = DDB.Table('food_products')

    response = table.scan()
    data = response['Items']

    while response.get('LastEvaluatedKey'):
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    
    print (data)
 
if __name__ == '__main__':
    get_all_items()


