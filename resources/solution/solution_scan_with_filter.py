'''
    You must replace <FMI_1> with the name of the GSI: special_GSI
    You must replace <FMI_2> with the name of the attribute to use in the filter expression: tags
'''


import boto3, json
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Key, Attr, Not


def scan_menu_items():
    
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('FoodProducts')

    response = table.scan(
                IndexName='special_GSI',
                FilterExpression=Not(Attr('tags').contains('out of stock')))
        
    data = response['Items']
    
    print (data)
 
if __name__ == '__main__':
    scan_menu_items()