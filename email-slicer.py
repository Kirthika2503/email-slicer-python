# An email slicer program

email = input("Enter your email: ")
index = email.index("@")  # A function that returns number/index of the value

username = email[:index]
print(f"Your username is: {username}")

# [index:] returns from the index
# if index=@ then returns from at to the end
# [index+1 :] returns from the value after index
domain = email[index + 1 : ] 
print(f"Your domain is: {domain}")
                             
