'''
    You must replace <FMI_1> with the table name
    You must replace <FMI_2> with the table's Primary Key
'''

import boto3, json


def batch_put(food_list):
    DDB = boto3.resource('dynamodb', region_name='us-east-1')
    table = DDB.Table('FoodProducts')
    with table.batch_writer(overwrite_by_pkeys=['product_name']) as batch:
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