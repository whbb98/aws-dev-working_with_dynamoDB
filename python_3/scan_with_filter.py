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
                IndexName='<FMI_1>',
                FilterExpression=Not(Attr('<FMI_2>').contains('out of stock')))
        
    data = response['Items']
    
    print (data)
 
if __name__ == '__main__':
    scan_menu_items()
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
