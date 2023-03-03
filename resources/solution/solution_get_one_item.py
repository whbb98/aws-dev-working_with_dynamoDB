'''
    You must replace <FMI_1> with the table's Primary Key
'''

import boto3, json
from boto3.dynamodb.conditions import Key


def get_one_item(product):

    DDB = boto3.client('dynamodb', region_name='us-east-1')

    response = DDB.get_item(TableName='FoodProducts',
        Key={
         'product_name': {'S': product}
         }
        )

    data = response['Item']
    
    print (data)
 
if __name__ == '__main__':
    product = "chocolate cake"
    get_one_item(product)

