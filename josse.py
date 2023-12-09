def greetings_according_to_levels():
    if age < 13:
        age_level = 'children'
        print(f"Nice to meet you {name}, we are pleased to see {age_level} in our gathering")
    elif age >= 13 and age < 18:
        age_level = 'Teens'
        print(f"wow glad to see {name}, we are excited to see {age_level} in our gathering")
    elif age >= 18 and age < 40:
        age_level = 'Youths'
        print(f"amaizing its of great joy i welcome you {name}, we are pleased to see {age_level} coming around")
    elif age >= 40 and age < 60:
        age_level = 'Adult'
        print(f"it good to see Mr {name}, it's an honour to see {age_level} coming to this gathering")
    else:
        age_level = 'Elders'
        print(f"it is with joy we welcome MR {name}, we are please to see an {age_level} in our mist")

name = input('')
age = int(input())
greetings_according_to_levels()

    