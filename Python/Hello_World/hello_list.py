#!/usr/bin/env python3

hello_str = "Hello World"

hello_bool = True

hello_tuple = (21, 32)

hello_list = ["Hello, ","this ","is ","a ","list"]

hello_dict = {"first_name":"Liam",
              "last_name":"Fraser",
              "eye_colour":"Blue"}

print(hello_list[0] + hello_list[1] + hello_list[2] + hello_list[3] + hello_list[4])

hello_list[4] += "!"

print(hello_list[4])

print(str(hello_tuple[0]))

print(hello_dict["first_name"] + " " + hello_dict["last_name"] + " has " + hello_dict["eye_colour"] + " eyes.")

print("{0} {1} has {2} eyes.".format(hello_dict["first_name"],
                                     hello_dict["last_name"],
                                     hello_dict["eye_colour"]))
