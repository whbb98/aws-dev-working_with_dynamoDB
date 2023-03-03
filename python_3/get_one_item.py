'''
    You must replace <FMI_1> with the table's Primary Key
'''

import boto3, json
from boto3.dynamodb.conditions import Key


def get_one_item(product):

    DDB = boto3.client('dynamodb', region_name='us-east-1')

    response = DDB.get_item(TableName='FoodProducts',
        Key={
         '<FMI_1>': {'S': product}
         }
        )

    data = response['Item']
    
    print (data)
 
if __name__ == '__main__':
    product = "chocolate cake"
    get_one_item(product)


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
