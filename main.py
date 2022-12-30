
with open("adventuring_gear.txt", 'r') as textFile:
    data = csv.reader(textFile)

 #   print(data)

for line in data:
    for word in range(len(line)):
        randomWord = random.randrange(len(line))
        print(randomWord)
        print(line[randomWord])

