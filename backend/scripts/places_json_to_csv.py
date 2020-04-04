import sys
import json
import csv
import re
import os
from array import array 

# Convert to string.
def to_string(s):
    try:
        return str(s)
    except:
        #Change the encoding type if needed
        return s.encode('utf-8')


# Match column name with place model column for load_places.py execution
def to_place_model_column(column):
    place_model_column = {
        'id':'place_id',
        'latitude':'lat',
        'longitude':'lng',
        'rating':'user_rating',
        'review_count':'num_ratings',
        'display_address':'address',
        'city':'area',
        'url':'place_url',
        'title':'place_types'
    }
    if column in place_model_column.keys():
        return place_model_column[column]
    return column


def json_to_csv(node,json_data,csv_file_path = None):
    global reduced_item
    raw_data = json_data
            
    try:
        data_to_be_processed = raw_data[node]
    except:
        data_to_be_processed = raw_data

    processed_data = []
    header = []
    for item in data_to_be_processed:
        reduced_item = {}
        reduce_item(node, item)

        header += reduced_item.keys()

        processed_data.append(reduced_item)

    header = list(set(header))
    header.sort()
    processed_data = list({v['place_id']:v for v in processed_data}.values())
    
    if csv_file_path is not None and os.path.exists(csv_file_path):
        with open(csv_file_path, 'a') as f:
            writer = csv.DictWriter(f, header, quoting=csv.QUOTE_ALL)
            #writer.writeheader()
            for row in processed_data:
                writer.writerow(row)

    print ("Completed json to csv conversion")
    print (f"Total : {len(processed_data)} row, {len(header)} columns")
    
    return processed_data

def reduce_item(key, value):
    #Reduction Condition 1
    if type(value) is list:
        i=0
        for sub_item in value:
            if key in 'display_address, transactions':
                values = ', '.join(value)
                new_key = to_place_model_column(to_string(key))
                reduced_item[new_key] = to_string(values)
                break
            else:
                reduce_item(key+'_'+to_string(i), sub_item)
                i=i+1

    #Reduction Condition 2
    elif type(value) is dict:
        sub_keys = value.keys()
        for sub_key in sub_keys:
            reduce_item(to_string(sub_key), value[sub_key])
    
    #Base Condition
    else:
        new_key = to_place_model_column(to_string(key))
        reduced_item[new_key] = to_string(value)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print ("\nUsage: python json_to_csv.py <node> <json_in_file_path> <csv_out_file_path>\n")
    else:
        #Reading arguments
        node = sys.argv[1]
        json_file_path = sys.argv[2]
        csv_file_path = sys.argv[3]

    with open(json_file_path) as fp:
        json_data = fp.read()

    json_to_csv(node,json_data,csv_file_path)
