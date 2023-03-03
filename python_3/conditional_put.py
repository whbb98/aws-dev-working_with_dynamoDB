'''
    You must replace <FMI_1> with the table name FoodProducts
    You must replace <FMI_2> with a product name. apple pie
    You must replace <FMI_3> with a444
    You must replace <FMI_4> with 595
    You must replace <FMI_5> with the description: It is amazing!
    You must replace <FMI_6> with a tag: whole pie
    You must replace <FMI_7> with a tag: apple
'''

import boto3
from botocore.exceptions import ClientError

def conditional_put():
    
    DDB = boto3.client('dynamodb', region_name='us-east-1')
    
    try:
        response = DDB.put_item(
            TableName='<FMI_1>',
            Item={
                'product_name': {
                    'S': '<FMI_2>'
                },
                'product_id': {
                    'S': '<FMI_3>'
                },
                'price_in_cents':{
                    'N': '<FMI_4>' #number passed in as a string (ie in quotes)
                },
                'description':{
                    'S': "<FMI_5>"
                },
                'tags':{
                    'L': [{
                            'S': '<FMI_6>'
                        },{
                            'S': '<FMI_7>'
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


"""
Copyright @2021 [Amazon Web Services] [AWS]
    
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
