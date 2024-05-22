ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here
#----------------------------------------------------
#In list you can change directly using the index:
ft_list[1] = "World!"

#The tuples can't be changed so you have to redefine:
ft_tuple = ("Hello", "France!")

#To change the set you have to use "remove" and "add":
ft_set.remove("tutu!")
ft_set.add("Paris!")

#in a dictionary you can acces by the keyword
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)