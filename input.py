name = input("Your Name")

age = int(input("Age: "))

print(f"Hi my name is {name}, and my age is {age}")

# slicing
name = "abu shahma"
print(name[0:3])
print(f"Hello {name.upper()}")

# sets

nums = {1,2,2,3}
print(nums)
print(2 in nums)

# Dictionaries

user = {"name": "Abu", "role": "Dev"}
user["Stack"] = "Mern"
print(user)
print(user.get("age"))