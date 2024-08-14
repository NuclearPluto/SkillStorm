phonebook = {"Dan Pickles" : "(123) 456-7890",
             "Randolph Scott" : "(456) 789-0123",
             "Howard Johnson" : "(789) 123-4567"}

print(phonebook["Dan Pickles"])
print(phonebook.get("Howard Johnson"))
print(phonebook.get("Bob Iger", "This name is not registered"))