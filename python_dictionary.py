""""
A dictionary is a ordered collection, which is mutable ,but does not allow duplicates.
Dictionaries are used to store the data as key value pairs.
Note: dictionary itself is mutable but inside the keys are immutable (we can delete entire key value pair but cannot change key)

"""
emp_dict = ()
emp_dict1 = dict()
print("the empty dictionary using inbuilt function is {}".format(emp_dict1))
dict_a = {"name": "John", "Age": 25}
type_dict =type(dict_a)
print("the type is {}".format(type_dict))
len_dict = len(dict_a)
print("the length of dict is {}".format(len_dict))

dict_a = {"name": "John", "Age": 25}
val_age = dict_a["Age"]
print("value of age is {}".format(val_age))
dict_a = {"name": "John", "Age": 25, "salary": 25000}
# val_sal = dict_a["salary"]
# print("the value of salary is {}".format(val_sal))

dict_b = {"apple": "Its red in colour", "banana": "Its yellow in colour"}
val_apple = dict_b.get("apple")
print("the value of apple is {}".format(val_apple))
val_grape = dict_b.get("grapes")
print("The value of grape is {}".format(val_grape))
"""""
when we use get keyword to fetch a value ,if there is no existing value it will return none
when we use normal assignment method to fetch a value,if there is no existing value it will through an error
"""""
dict_a["name"] = "Alex"
print("the value after changing is {}".format(dict_a))
dict_a.update({"emp code": 168086})
print("the value after updating is {}".format(dict_a))
dict_c = {"fruits": ["apple","banana", "orange"], "vegetables": {"green":"peas", "red": "carrot"}}
dict_frt_get = dict_c.get("fruits")
print("the value of fruits using get method is {}".format(dict_frt_get))
dict_frt = dict_c["fruits"]
print("the value of fruits is {}".format(dict_frt))
dict_veg_get = dict_c.get("vegetables")
print("the value of vegetables using get method is {}".format(dict_veg_get))
dict_veg = dict_c["vegetables"]
print("the value of vegetables is {}".format(dict_veg))

dict_red_get = dict_c.get("vegetables").get("red")
print("the value of key red using get is {}".format(dict_red_get))
dict_red = dict_c["vegetables"]["red"]
print("the value of key red is {}".format(dict_red))

car_details = {"name": "Maruthi 800", "Manufacturer year": 2000, "Engine": "Diesel","color": "white"}
# to fetch keys
keys_dict = car_details.keys()
print("the keys of car details is {}".format(keys_dict))
lst_dict_keys = list(car_details.keys())
print("the list of car details are {}".format(lst_dict_keys))
# to fetch values
val_dict = list(car_details.values())
print("the list of values of car details are {}".format(val_dict))

#items
item_car_det = list(car_details.items())
print("the list of items of car details are {}".format(item_car_det))

#clear -It deletes all the elements of key value pair of dictionary
dict_a ={"name": "John", "Age": 25}
dict_a.clear()
print("the value after clearing is {}".format(dict_a))

#pop -It deletes particular key mentioned to delete
car_details ={"name": "Maruthi 800", "Manufacturer": 2000,"Engine": "Diesel", "color": "white"}
car_details.pop("Engine")
print("the dictionary after deleting engine key value pair is {}".format(car_details))

#pop item -it deletes the last item or last key value pair
car_details.popitem()
print("the value of dict after popitem is {}".format(car_details))

dict_x = {"fruits": ["apple", "banana"]}
dict_val =dict_x.get("fruits")
print("the value after getting fruits is {}".format(dict_val))
print(dict_val)
dict_val.extend(["grapes", "orange"])
print(dict_val)
dict_x["fruits"]= dict_val
print("the value of dict_x after extending is {}".format(dict_x))















