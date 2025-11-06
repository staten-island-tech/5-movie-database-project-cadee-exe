import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

for index, item in enumerate(data):
    print(index, ":" ,(item)["title"])
    
# choice = int(input("Year after?"))
# choice2 = int(input("Before what year?"))

# for item in data:
#     if choice2 > (item)["year"] > choice:
#         print(item["title"]) 

# choice3=int(input("year?"))
# for items in data:
#     if choice3 == items["year"]:
#         print(items["title"], items["year"])
        
movie = input("pick movie")
if movie == item["title"]:
    print(item["title"])
    movie = []
    movie.append
    if len(movie) == len(item["title"]):
        print(f"{movies["title"]}, exists")
    else:
        print(f"{movies} not found")