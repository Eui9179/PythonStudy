#문제 1
pets = [
    {"name" : "꾸릉이","age":1},
    {"name": "올리","age":7},
    {"name": "초코","age":3}
]

for pet in pets:
    print(pet["name"],pet["age"])

print("================\n")

#문제 2
numbers = [1,2,1,2,4,3,5]
counter = {}

for number in numbers:
    if(number in counter):
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)


print("================\n")

#문제 3
char = {
    "name" : "기사",
    "level" : 12,
    "item":{
        "sword":"검",
        "armor":"방패"
    },
    "skill":["베기","막기","피하기"]
}

for ch in char:
    if(type(char[ch]) is dict):
        for dict_ch in char[ch]:
            print(dict_ch,":",char[ch][dict_ch])

    elif(type(char[ch]) is list):
        for list_ch in char[ch]:
            print(ch,":",list_ch)

    else:
        print(ch,":",char[ch])

