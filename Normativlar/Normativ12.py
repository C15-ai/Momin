# 1
with open("students.txt", "r") as f:
    data = f.readlines()
    print(data)
# 2
for line in data:
    print(line)
# 3
new = []
for line in data:
    name,score = line.split("-")
    score = int(score)
    if score < 80:
        new.append(name)
        new.append(score)
        print(new)
#4
for line in data:
    name,score = line.split("-")
    score = int(score)
    if score < 80:
        score += 5
        new.append(name)
        new.append(score)
        print(new)
#5
with open("students.txt", "w") as f:
   for line in new:
       f.write(line)




