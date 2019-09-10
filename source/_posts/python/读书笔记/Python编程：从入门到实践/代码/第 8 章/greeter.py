def greet_user():
    '''显示简单的问候语'''
    print("Hello!")

# greet_user()

# doc = greet_user.__doc__
# print(doc)


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet()