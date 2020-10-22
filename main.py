#Juliana Horvath
#This program will use your Zodiac sign and another person's zodiac sign to tell
#you several different things about you and the other person, like your compatibility,
#your zodiac elements, your lucky numbers, etc.
#Receieved help from Anthony Horvath and my professor Scott Vanselow.
#This line asks for user input of someone else's Zodiac sign.
import random
your_zodiac = input("Enter your Zodiac(all lowercase): ")
#The following lines assign a number to each of the signs in order to find the
#percentage of compatibility in the end.
if your_zodiac == "aquarius":
    your_comp = 87
if your_zodiac == "pisces":
    your_comp = 64
if your_zodiac == "aries":
    your_comp = 93
if your_zodiac == "taurus":
    your_comp = 56
if your_zodiac == "gemini":
    your_comp = 98
if your_zodiac == "cancer":
    your_comp = 82
if your_zodiac == "leo":
    your_comp = 48
if your_zodiac == "virgo":
    your_comp = 67
if your_zodiac == "libra":
    your_comp = 86
if your_zodiac == "scorpio":
    your_comp = 91
if your_zodiac == "saggitarius":
    your_comp = 41
if your_zodiac == "capricorn":
    your_comp = 75
#This line asks for user input of someone else's Zodiac sign.
their_zodiac = input("Enter their Zodiac(all lowercase): ")
#The following lines assign a number to each of the signs in order to find the
#percentage of compatibility in the end.
if their_zodiac == "aquarius":
    their_comp = 87
if their_zodiac == "pisces":
    their_comp = 64
if their_zodiac == "aries":
    their_comp = 93
if their_zodiac == "taurus":
    their_comp = 56
if their_zodiac == "gemini":
    their_comp = 98
if their_zodiac == "cancer":
    their_comp = 82
if their_zodiac == "leo":
    their_comp = 48
if their_zodiac == "virgo":
    their_comp = 67
if their_zodiac == "libra":
    their_comp = 86
if their_zodiac == "scorpio":
    their_comp = 91
if their_zodiac == "saggitarius":
    their_comp = 41
if their_zodiac == "capricorn":
    their_comp = 75
#The following code defines each of the variables that are going to be calculated using
#certain equations.
emo_comp = ((your_comp + their_comp)/2) - 5
#emo_comp is the emotional compatibility and this will tell you how easy
#it is for you talk to this person and have a deep, meaningful relationship with them.
social_comp = ((your_comp * their_comp) ** 0.5) // 2
#social_comp is the social compatibility and this will tell you how comfortable
#you are around this person in a social environment and in social situations.
phy_comp = (your_comp % their_comp) * 1.2
#phy_comp is the physical compatibility and this will tell you how close and attracted
#you are physically to this person.
emo_comp *= 1.05
social_comp *= 1.15
phy_comp *= 1.10
#The following lines of code do the computations, based on the signs you chose, in order to
#find the different compatibilities.
#I used the "if" statements in order to keep the numbers in the 0.0% - 100.0% range
#because some numbers were coming out greater than 100.0% and some less than 0.0%.
if emo_comp > 100:
    print("Emotional " + "Compatibility: ", 100.0, '%')
if emo_comp < 0:
    print("Emotional " + "Compatibility: ", 0.0, '%')
if emo_comp >= 0 and emo_comp <= 100:
    print("Emotional " + "Compatibility: ", format(emo_comp,'.1f'), '%')
if social_comp > 100:
    print("Social " + "Compatibility: ", 100.0, '%')
if social_comp < 0:
    print("Social " + "Compatibility: ", 0.0, '%')
if social_comp >= 0 and social_comp <= 100:
    print("Social " + "Compatibility: ", format(social_comp,'.1f'), '%')
if phy_comp > 100:
    print("Pysical " + "Compatibility: ", 100.0, '%')
if phy_comp < 0:
    print("Pysical " + "Compatibility: ", 0.0, '%')
if phy_comp >= 0 and phy_comp <= 100:
    print("Pysical " + "Compatibility: ", format(phy_comp,'.1f'), '%')
#The following lines of code take the percent calculated from the previous lines of code
#and based on that value, your given a message regarding the compatibility.
if emo_comp >= 65:
    print("Love!" * 3)
else:
    print("No love.")
if social_comp >= 30:
    print("Friends!" *3)
else:
    print("Enemies.")
if phy_comp >= 45:
    print("Kiss!" *3)
else:
    print("No kiss.")

if emo_comp != range(65,100) or social_comp != range(30,100) or phy_comp != range(45,100):
    print("You do not have good compatibility with this person in at least one of the compatibility categories.")

#This portion of code will take your zodiac sign and tell you what your element is.
def get_element(your_zodiac):
    if your_zodiac == "cancer" or your_zodiac == "scorpio" or your_zodiac == "pisces":
        return "Your zodiac element is water."
    elif your_zodiac == "virgo" or your_zodiac == "taurus" or your_zodiac == "capricorn":
        return "Your zodiac element is earth."
    elif your_zodiac == "leo" or your_zodiac == "aries" or your_zodiac == "saggitarius":
        return "Your zodiac element is fire."
    elif your_zodiac == "gemini" or your_zodiac == "libra" or your_zodiac == "aquarius":
        return "Your zodiac element is air."
    else:
        return "Your zodiac sign is invalid. Please type a valid zodiac sign."
print(get_element(your_zodiac))
#This portion of code will take the other person's zodiac sign and tell you what their element is.
def get_element(their_zodiac):
    if their_zodiac == "cancer" or their_zodiac == "scorpio" or their_zodiac == "pisces":
        return "Their zodiac element is water."
    elif their_zodiac == "virgo" or their_zodiac == "taurus" or their_zodiac == "capricorn":
        return "Their zodiac element is earth."
    elif their_zodiac == "leo" or their_zodiac == "aries" or their_zodiac == "saggitarius":
        return "Their zodiac element is fire."
    elif their_zodiac == "gemini" or their_zodiac == "libra" or their_zodiac == "aquarius":
        return "Their zodiac element is air."
    else:
        return "Their zodiac sign is invalid. Please type a valid zodiac sign."
print(get_element(their_zodiac))
#This portion of code compares your element to the other person's element and will tell you
#whether your element matches the other person's element.
if get_element(your_zodiac) == get_element(their_zodiac):
    print("Your element does match the other person's element!")
if not (get_element(your_zodiac) == get_element(their_zodiac)):
    print("Your element does not match the other person's element.")

#This portion of code will take your zodiac sign and calculate the amount of true
#friends you should have in life.
num_friends = 0
for x in range(1):
    number = your_comp
    num_friends += number * 0.1
    print("The amount of true friends you'll have is", int(num_friends), '.')

#This portion of code will tell you what your lucky numbers are.
print("Your lucky numbers are:")
y = 0
while y < 4:
    print(random.randint(1, 30), end=" ")
    y += 1
