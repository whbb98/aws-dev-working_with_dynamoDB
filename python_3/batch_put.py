'''
    You must replace <FMI_1> with the table name
'''

import boto3, json


def batch_put(food_list):
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('<FMI>')
    with table.batch_writer() as batch:
        for food in food_list:
            product_name = food['product_name_str']
            product_id = food['product_id_str']
            price_in_cents = food['price_in_cents_int']
            description = food['description_str']
            tags = food['tag_str_arr']
            formatted_data  = {
                'product_name': product_name,
                'product_id': product_id,
                'price_in_cents': price_in_cents,
                'description': description,
                'tags': tags
            }
            if 'special_int' in food:
                formatted_data['special'] = food['special_int']
                print("Adding special food item:", product_name, price_in_cents)
            else:
                print("Adding food item:", product_name, price_in_cents)
                pass
           
            batch.put_item(Item=formatted_data)

   
if __name__ == '__main__':
    with open("../resources/website/all_products.json") as json_file:
        food_list = json.load(json_file)['product_item_arr']
    batch_put(food_list)#

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
