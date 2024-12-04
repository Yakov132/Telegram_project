import json
import string
def save_data(data):
    with open("test.json" , "r" , encoding = "utf-8") as file :
        data_from_file_str = file.read()
    data_from_file_json:list[dict] = json.loads(data_from_file_str)
    # data = {"name":"123"}
    data_from_file_json.append(data)

    with open("test.json", "w" , encoding = "utf-8") as file :
        json_output = json.dumps(data_from_file_json , indent = 0 , ensure_ascii = False)
        print (json_output)
        file.write(json_output)
    # file =  open ('file_dict_name','a+')
    # file = open('file_dict_name','w+')
dagits_massa = string.digits
def check_data(massiv):
    for i in massiv:
        print(i)
        if  i in  string.digits : 
            return True
        else :
            return False