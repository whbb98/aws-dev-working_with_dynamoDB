'''
    You must replace <FMI_1> with the table name
    You must replace <FMI_2> with the table's Primary Key
'''

import boto3, json


def batch_put(food_list):
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('<FMI_1>')
    with table.batch_writer(overwrite_by_pkeys=['<FMI_2>']) as batch:
        for food in food_list:
            product_name = food['product_name_str']
            price_in_cents = food['price_in_cents_int']
            formatted_item = {
                'product_name': product_name,
                'price_in_cents': price_in_cents  #Boto will "know" this is a number type
            }
            print("Adding food item:", formatted_item)
            batch.put_item(Item=formatted_item)

   
if __name__ == '__main__':
    with open("../resources/test.json") as json_file:
        food_list = json.load(json_file)
    batch_put(food_list)
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
