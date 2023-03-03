
'''
    You must replace <FMI_1> with the table name food_products
    You must replace <FMI_2> with a product name. apple pie
    You must replace <FMI_3> with a444
    You must replace <FMI_4> with 595
    You must replace <FMI_5> with the description: It is amazing!
    You must replace <FMI_6> with a product name: whole pie
    You must replace <FMI_7> with a product name: apple
'''

import boto3
from botocore.exceptions import ClientError

def conditional_put():
    
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    try:
        response = DDB.put_item(
            TableName='FoodProducts',
            Item={
                'product_name': {
                    'S': "apple pie"
                },
                'product_id': {
                    'S': 'a444'
                },
                'price_in_cents':{
                    'N': "595" #number passed in as a string
                },
                'description':{
                    'S': "It is amazing!"
                },
                'tags':{
                    'L': [{
                            'S': "whole pie"
                        },{
                            'S': "apple"
                        }]
                }
            },
            ConditionExpression='attribute_not_exists(product_name)'
        )
    except ClientError as e:
        # Ignore the ConditionalCheckFailedException, bubble up
        # other exceptions.
        if e.response['Error']['Code'] != 'ConditionalCheckFailedException':
            raise

if __name__ == '__main__':
    conditional_put()
    print('Done')

