import json

# import mysql.connector
#
#
# conn = mysql.connector.connect(user='admin', host='localhost', database='baza', passwd="fdsfsfds343")
#
# c = conn.cursor()
#
# c.execute("CREATE DATABASE testowa")
#
# conn.close()

# employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
#
# employee_dict = json.loads(employee)
# print(employee_dict)
# print(type(employee_dict))
#
# json_object = json.dumps(employee_dict, indent=4)
# print(json_object)
# print(type(json_object))


var = {
    "Tematy": {
        "Fizyka": 50,
        "Programowanie": 90
    }
}


json_var ="""
{
    "Country": {
        "name": "INDIA",
        "Languages_spoken": [
            {
                "names": ["Hindi", "English", "Bengali", "Telugu"]
            }
        ]
    }
}
"""

zm = json.loads(json_var)
print(zm)

with open("przyklad.json", "r") as p:
    data = json.load(p)
    print(data)
