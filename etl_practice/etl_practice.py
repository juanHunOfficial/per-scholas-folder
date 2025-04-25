import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 


log_file = "log_file.txt" # for logging the process 
target_file = "transformed_data.csv" # where we want our finished data to go

def extract_from_csv(file):
    dataframe = pd.read_csv(file)
    return dataframe

def extract_from_json(file):
    dataframe = pd.read_json(file, lines=True)
    return dataframe

def extract_from_xml(file):
    dataframe = pd.DataFrame(columns=[
        "car_model", 
        "year_of_manufacture",
        "price",
        "fuel"
    ])
    tree = ET.parse(file)
    root = tree.getroot()
    for car in root:
        car_model = car.find("car_model").text
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        dataframe = pd.concat([
            dataframe,
            pd.DataFrame([{
                "car_model": car_model, 
                "year_of_manufacture": year_of_manufacture,
                "price": price,
                "fuel": fuel
            }])
        ], ignore_index=True)
    return dataframe

def extract():
    extracted_data = pd.DataFrame(columns=[
        "car_model", 
        "year_of_manufacture",
        "price",
        "fuel"
    ])

 # processing for all the csv files
    for csv_file in glob.glob("*.csv"):
        if csv_file != target_file: # make sure your ignoring the target file we made to store or extracted and transformed data.
            extracted_data = pd.concat([
                extracted_data,
                pd.DataFrame(extract_from_csv(csv_file))
            ], ignore_index=True)

 # proceessing for all the json files
    for json_file in glob.glob("*.json"):   
        extracted_data = pd.concat([
            extracted_data, 
            pd.DataFrame(extract_from_json(json_file))
        ], ignore_index=True)

 # process for all the xml files
    for xml_file in glob.glob("*.xml"):
        extracted_data = pd.concat([
            extracted_data,
            pd.DataFrame(extract_from_xml(xml_file))
        ], ignore_index=True)

    return extracted_data

def transform(data):
    data['price'] = round(data.price, 2)
    return data

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file) 

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started") 
extracted_data = extract() 
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended") 
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended") 
 
# Log the beginning of the Loading process 
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended") 
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended") 