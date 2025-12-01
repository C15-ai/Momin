# 1
# import json
# numbers = {"numbers": [1, 2, 3, 4, 5]}
# with open("numbers.json", "w") as f:
#     json.dump(numbers, f, indent=4)
# 2
# import json
# data = {
#     "users": [
#         {"name": "Ali", "age": 20},
#         {"name": "Vali", "age": 25},
#         {"name": "Gul", "age": 19}
#     ]
# }
# with open("users.json", "w") as f:
#     json.dump(data, f, indent=4)
# 3
# import json
# with open("users.json") as f:
#     data = json.load(f)
#
# data["users"].append({"name": "Gul", "age": 19})
#
# with open("users.json", "w") as f:
#     json.dump(data, f, indent=4)
# 4
# import json
# data = {
#   "products": [
#      {"name": "Pen", "price": 10},
#      {"name": "Bag", "price": 50},
#      {"name": "Shoes", "price": 120}
#    ]
#  }
# ortaca = sum(p["price"] for p in data["products"]) / len(data["products"])
# with open("products.json", "w") as f:
#      json.dump(ortaca, f, indent=4)
# 5
# import json
#
# with open("products.json", "r") as f:
#     data = json.load(f)
#
# filtr = [p for p in data["products"] if p["price"] > 50]
#
# with open("products.json", "w") as f:
#     json.dump(filtr, f, indent=4)

# 6
# import json
# data = {
#     "products": [
#         {"name": "Phone", "price": 300},
#         {"name": "Laptop", "price": 1000},
#         {"name": "Mouse", "price": 20}
#     ]
# }
# for product in data["products"]:
#     product["discaunt"] = 0.1
# with open("shop.json", "w") as f:
#     json.dump(data, f, indent=4)
# 7
# import json
#
# data = {
#     "students": [
#         {"name": "Ali", "score": 85},
#         {"name": "Vali", "score": 67},
#         {"name": "Gul", "score": 92},
#
#         {"name": "Aziz", "score": 74}
#     ]
# }
# passad = []
# failed = []
# for student in data['students']:
#     if student['score'] >= 80:
#         passad.append(student['name'])
#     else:
#         failed.append(student['name'])
# results = {
#     "students": passad,
#     "failed": failed
# }
# with open("students2.json", "w") as f:
#    json.dump(results,f,indent=4)
# 8
# import json
#
# data = {
#     "users": [
#         {
#             "username": "ali",
#             "posts": ["p1", "p2", "p3"]
#         },
#         {
#             "username": "vali",
#             "posts": ["p1"]
#         },
#         {
#             "username": "gul",
#             "posts": []
#         }
#     ]
# }
# stats = []
# for user in data['users']:
#     stats.append({
#         "username": user['username'],
#         "posts_count": len(user['posts'])
#     })
# with open('stats.json', 'w') as f:
#     json.dump(stats,f, indent=4)
# 9
# import json
#
# schols = {
#     "school_name": "IT School",
#     "groups": [
#         {
#             "name": "Group A",
#             "students": ["Ali", "Vali"]
#         },
#         {
#             "name": "Group B",
#             "students": ["Gul", "Aziz", "Lola"]
#
#         }
#     ]
# }
# with open('schols.json', 'w', ) as f:
#     json.dump(schols, f, indent=4)
# 10
# import json
#
# courses = {
#     "name": "Python Basics",
#     "students": ["Ali", "Vali", "Gul"]
# }
# with open('courses.json', 'r') as f:
#     data = json.load(f)
# data['duration_month'] = 3
# with open('courses.json', 'w') as f:
#     json.dump(data, f, indent=4)
# 11
# import json
#
# logs = {
#     "logs": [
#         {"level": "info", "message": "Started"},
#         {"level": "error", "message": "Something failed"},
#         {"level": "warning", "message": "Low memory"},
#         {"level": "error", "message": "DB connection failed"}
#     ]
# }
# stats = {"info": 0, "error": 0, "warning": 0}
# for log in logs["logs"]:
#     level = log["level"]
#     stats[level]  += 1
# with open("logs.json", "w") as f:
#     json.dump(stats, f, indent=4)
# 12
# import json
#
# citys = {
#     "cities": [
#         {"name": "Tashkent", "population": 2500000},
#         {"name": "Samarkand", "population": 530000},
#         {"name": "Bukhara", "population": 280000}
#     ]
#
# }
# total = sum(city['population'] for city in citys['cities'])
# with open("cities.json", "w") as f:
#     json.dump(total, f, indent=4)
import json

# 2-fayl
# 1
# import json
#
# orders = {
#     "orders": [
#         {
#             "id": 1,
#             "customer": "Ali",
#             "total_price": 120.5,
#             "status": "paid"
#         },
#         {
#             "id": 2,
#             "customer": "Vali",
#             "total_price": 75,
#             "status": "pending"
#         },
#         {
#             "id": 3,
#             "customer": "Soli",
#             "total_price": 200,
#             "status": "paid"
#         }
#     ]
# }
# total = 0
# for order in orders["orders"]:
#     if order["status"] == "paid":
#         total += order["total_price"]
# with open("orders.json", "w") as a:
#     json.dump(orders, a,indent=4)
# print(total)
# 2
# import json
#
# with open("orders_items.json", "r") as f:
#     data = json.load(f)
# for order in data["orders"]:
#     s = sum(item["qty"] for item in order["items"])
#     print(f"Buyurtma {order["id"]}: Jami {s} ta mahsulot")
# 3
# import json
#
# data = {
#     "students": [
#         {
#             "name": "Ali",
#             "grades": [80, 90, 75]
#         },
#         {
#             "name": "Vali",
#             "grades": [60, 70, 65]
#         },
#         {
#             "name": "Gul",
#             "grades": [95, 100, 90]
#         }
#     ]
# }
#
# with open("students.json", "w") as f:
#     json.dump(data, f, indent=4)
# for i in data['students']:
#     avg = sum(i['grades']) / len(i['grades'])
#     if avg >= 80:
#         print(i['name'])
# import json
#
# data = {
#     "categories": [
#         {
#             "name": "Electronics",
#
#             "products": [
#                 {"name": "Phone", "price": 300},
#                 {"name": "Laptop", "price": 1000}
#             ]
#         },
#         {
#             "name": "Books",
#             "products": [
#                 {"name": "Python 101", "price": 25},
#                 {"name": "Algorithms", "price": 40},
#                 {"name": "Data Science", "price": 35}
#             ]
#         }
#     ]
# }
#
#
# with open("shop.json", "r") as f:
#     data = json.load(f)
# for i in data['categories']:
#     print(f"{i['name']}:{len(i['products'])} ta mahsulot")
# 5
# import json
# with open("shop.json", "r") as f:
#      data = json.load(f)
# max_p = None
# for i in data["categories"]:
#     for j in i["products"]:
#         if max_p is None or j["price"] > max_p["price"]:
#             max_p = j
# print("Eng qimmat mahsulot:", max_p['name'],max_p['price'])
# 6
# import json
#
# data = {
#     "users": [
#         {
#             "username": "ali",
#             "posts": [
#                 {"title": "My first post", "likes": 5},
#                 {"title": "Python tips", "likes": 10}
#             ]
#         },
#         {
#             "username": "vali",
#             "posts": [
#                 {"title": "Travel blog", "likes": 3}
#             ]
#         },
#         {
#             "username": "gul",
#             "posts": []
#         }
#     ]
# }
# with open('blog.json', "w") as f:
#     json.dump(data, f, indent=4)
# not_user = []
# for i in data['users']:
#     count = len(i['posts'])
#     print(f"{i['username']}", "-", count, " ta post")
#     if count == 0:
#       not_user.append(i['username'])
# print("posti yoqlar", not_user)

# 7
# import json
#
# with open("blog.json", "r") as f:
#     data = json.load(f)
# best = None
# for i in data["users"]:
#     for j in i["posts"]:
#         if best is None or j["likes"] > best["likes"]:
#             best = {
#                 "username": i["username"],
#                 "title": j["title"],
#                 "likes": j["likes"],
#
#             }
# print(best)
# with open("blog.json", "w") as f:
#     json.dump(best, f, indent=4)
# 8
# import json
# with open("library.json", "r") as f:
#     data = json.load(f)
#
# authors = {}
# for i in data['books']:
#     a = i['author']
#     authors[a] = authors.get(a, 0) + 1
# for name, count in authors.items():
#     print(f"{name}: {count} ta kitob")
# with open("library.json", "w") as f:
#     json.dump(authors, f, indent=4)
# 9
# import json
#
# with open("library.json", "r") as f:
#     data = json.load(f)
# for i in data["books"]:
#     if i["year"] < 2000:
#         print(i["title"])
# 10
# import json
#
# with open("cart.json","r") as f:
#     data = json.load(f)
# items = data["cart"]["items"]
# total_q = sum(i["qty"] for i in items)
# total_s = sum(i["price"]* i["qty"] for i in items)
# print(total_q)
# print(total_s)
# 11
# import json
#
# data = {
#     "users": [
#         {"username": "admin1", "role": "admin", "active": 'true'},
#         {"username": "user1", "role": "user", "active": 'true'},
#         {"username": "user2", "role": "user", "active": 'false'},
#         {"username": "moder1", "role": "moderator", "active": 'true'}
#     ]
# }
# with open("users_role.json", "w") as f:
#     json.dump(data, f, indent=4)
# counts = {"admin": 0, "user": 0, "moderator": 0}
# for i in data["users"]:
#     if i["active"]:
#         counts[i["role"]] += 1
# print(counts)
# 12
# import json
#
# data = {
#     "countries": [
#         {
#             "name": "CountryA",
#             "cities": [
#                 {"name": "City1", "population": 100000},
#                 {"name": "City2", "population": 250000}
#             ]
#         },
#         {
#             "name": "CountryB",
#             "cities": [
#                 {"name": "City3", "population": 50000},
#
#                 {"name": "City4", "population": 300000},
#                 {"name": "City5", "population": 150000}
#             ]
#         }
#     ]
# }
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=4)
# for i in data['countries']:
#     total_pop = sum(city["population"] for city in i['cities'])
# for city in i['cities']:
#     print(i["name"],":", total_pop)
# 13
# import json
#
# with open("movies.json", "r") as f:
#     data = json.load(f)
# filtr = [m for m in data["movies"] if m["rating"] > 8]
# for m in filtr:
#     print(m["title"])
# oldes = min(filtr, key=lambda x: x["year"])
# print(oldes["title"])
# 14
# import json
# with open("courses.json","r") as f:
#     data = json.load(f)
# max_courses = max(data['courses'], key=lambda i: len(i['students']))
# for i in data['courses']:
#     print(i["name"], "-", len(i["students"]))
# print(max_courses["name"])
# 15
# import json
# with open("discount.json","r") as f:
#     data = json.load(f)
#
# for i in data['products']:
#     if i["discount"] < 0:
#         new_price = i["price"]-i["price"] * i["discount"]
#         print(i["name"],"->",new_price)
