#Importing json
import json

#Creating our barebones data library

data = {

    'name': 'Austin Nguyen',
    'age': 22,
    'city': 'Renton, WA',
    'interests':['Soccer','Football','Sweets','Games','Music','Martial Arts'],
    'is_student': True

}


#Creating a Json file and writing the object contents to the json file
with open('data.json','w') as json_file:

        json.dump(data,json_file,indent=4)

print("Data has been written to data.json")

#Reading the contetns of the previously created json_file
with open('data.json','r') as json_file:
        
        #Create an object called loaded_data. Load the json file into the argument parameter.
        loaded_data = json.load(json_file)

#Prints "Succesfully able to read data.json" when it is able to sucessfully
#Prints the loaded data from json_file thanks to the object loaded_data we created
print("Succesfully able to read data.json")
print(loaded_data)

#
loaded_data['age'] = 21 #<-Integers
loaded_data['interests'].append('Secret Hobby')

#Rewrite the changes to our json_file
with open('data.json','w') as json_file:

        json.dump(loaded_data,json_file,indent=4)

print("Data has been rewritten to data.json")