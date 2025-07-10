name = input("Hello, what's your name?")
print(f"Ok. Nice to meet you {name}!")
age_input = input(f"How old are you {name}?")
age = int(age_input)
bot_age = 1
age_different = age - bot_age 

if age < 10:
    print("Wow, you are still a kid!")
elif age < 20:
    print("Nice, you're already a teenager!")
else:
    print("Okey, i think you are gettin old...")

print(f"You are {age_different} than me. I'm only {bot_age}!")
color = input("What's your favorite color?")
print(f"Oh, {color} is beautiful color!")
print("OK then. Thanks for chatting with me, bye! :)")