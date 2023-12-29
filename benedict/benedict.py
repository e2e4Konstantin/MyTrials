import benedict as bd

d = bd. benedict()

# set values by keys list
d["profile", "firstname"] = "Fabio"
d["profile", "lastname"] = "Caccamo"
print(d) # -> { "profile":{ "firstname":"Fabio", "lastname":"Caccamo" } }
print(d["profile"]) # -> { "firstname":"Fabio", "lastname":"Caccamo" }

# check if keypath exists in dict
print(["profile", "lastname"] in d) # -> True

# delete value by keys list
del d["profile", "lastname"]
print(d["profile"]) # -> { "firstname":"Fabio" }


# # create a new empty instance
# d = bd.benedict()

# # or cast an existing dict
# df = {1: 'qqq', 2:'yyy'}

# d = benedict.benedict(df)

# # or create from data source (filepath, url or data-string) in a supported format:
# # Base64, CSV, JSON, TOML, XML, YAML, query-string
# d = benedict("https://localhost:8000/data.json", format="json")

# print(d)

# a = benedict(keyattr_dynamic=True) # default False
# a.profile.firstname = "Fabio"
# a.profile.lastname = "Caccamo"
# print(a) # -> { "profile":{ "firstname":"Fabio", "lastname":"Caccamo" } }
