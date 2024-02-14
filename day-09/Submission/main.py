file = open('story.txt', 'r')

counter = 0
count = 0
lines = file.readlines()
for line in lines:
    counter += 1
    if(line != '\n'):
        count += 1

file.close()

print("The number of lines in 'story.txt' is:",counter)
print("The number of lines in 'story.txt' without the empty line:",count)