import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" for index, item in enumerate(data):
    print(index, ":" ,(item)["title"]) """
    
# choice = int(input("Year after?"))
# choice2 = int(input("Before what year?"))

# for item in data:
#     if choice2 > (item)["year"] > choice:
#         print(item["title"]) 

# choice3=int(input("year?"))
# for items in data:
#     if choice3 == items["year"]:
#        print(items["title"], items["year"])
def search():
    like = input("what movie u liek")
    found = 0
    for i in data:
        if like.lower() in i['title'].lower():
            print(f"{i["title"].lower()} is here")
            found +=1
        if found ==0:
            print("no exist")
search()


