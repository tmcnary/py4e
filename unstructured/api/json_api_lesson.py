#JSON api lesson from youtube
#https://www.youtube.com/watch?v=9N6a-VLBa2I

import json
people_string = '''
{
    "people": [
        {
            "name": "Tony",
            "favoriteNumber": 8,
            "isProgrammer": true,
            "hobbies": ["Motorcycling", "Collecting Hobbies"],
            "friends": [{
                "name": "Sarah",
                "favoriteNumber": 37,
                "isProgrammer": true
            }]
        },
        {
            "name": "Lucy",
            "favoriteNumber": null,
            "isProgrammer": false,
            "hobbies": ["Motorcycling", "Collecting Boys"],
            "friends": [{
                "name": "Sarah",
                "favoriteNumber": 37,
                "isProgrammer": true
            }]
        }
    ]
}
'''

data = json.loads(people_string)
#prints a list of people
print(type(data['people']))
for person  in data['people'] :
    print(person)

#prints details of friends
for person in data['people'] :
    print(person['friends'])
    for friend in person['friends'] :
        print(friend['name'])
    for hobby in person['hobbies']:
        print("- hobby:" + hobby)