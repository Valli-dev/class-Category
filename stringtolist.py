s="Mike,koss,2500,password,mike@mail.com"
s='400'
t=int(s)+ int(100)
print(t)
list = str.split(s, ',')
print(list)
last_list = "Mike,koss,2500,password,mike@mail.com"
user_list = str.split(last_list, ',')
print(user_list)
newbal = int(user_list[2]) - t
user_list[2] = newbal
print(user_list[2])
updated_entry= str(user_list)
print(updated_entry)