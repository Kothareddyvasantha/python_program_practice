#dictionary
"""
A dictionary is a ordered collection , which is mutuable ,but it does not allow duplicates
dictionary is mutuable but keys in dictionary are inmutuable (we can delete entire key value pair but cannot change the key)

"""
emp_dict = {}
emp_dict1 = dict()
print("the empty dictionary using in built function is {}".format(emp_dict1))
dict_a ={"name":"John", "Age":25}
type_dic =type(dict_a)
print("the type is {}".format(type_dic))
len_dic =len(dict_a)
print("length of dictionary is {}".format(len_dic))

dict_a = {"name": "John", "Age": 25}
val_name =dict_a["name"]
print("the value of name is {}".format(val_name))
val_age =dict_a ["Age"]
print("the value of age is {}".format(val_age))
# val_sal =dict_a ["salary"]
# print("the value of salary is {}".format(val_sal))

dict_b ={"apple": "Its red in color", "banana": "Its in yellow color"}
val_apple =dict_b.get("apple")
print("the value of key apple is {}".format(val_apple))
val_banana =dict_b.get ("banana")
print("the value of key banana is {}".format(val_banana))
val_grape =dict_b.get("grape")
print("the value of key grape is {}".format(val_grape))

dict_a["name"] ="Alex"
print("the value after changing value is {}".format(dict_a))
dict_a["salary"] =25000
print("the value of dict_a is {}".format(dict_a))
dict_a.update({"emp code":12345})
print("the value of dictionary after updating is {}".format(dict_a))