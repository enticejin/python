import random as random
tem = random.random() * 60
humidity = random.uniform(1, 100.0)
key = random.randint(1, 2)
header = 'INSERT INTO rooms(room_name,foreign_key,temperature,humidity)  VALUES'
footer = "('F6-006', 1, 24.8, 40.0)"
for i in range(1, 30, 1):
    tem = random.random() * 60
    humidity = random.uniform(1, 100.0)
    floo_header = random.randint(6, 7)
    if floo_header ==6 :
        key = 1
    else:
        key = 2
    footer = "(\"F"+str(floo_header)+"-00"+str(i)+"\", "+str(key)+", "+str(tem)[0: 4]+", "+str(humidity)[0: 4]+");"
    all_line = header + footer
    print(all_line)