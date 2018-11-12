# 2018.10.10 Parse the 9G file to get all of the Movie ID

Text = b'product/productId'
movieID = set()
with open('movies.txt', 'rb') as file:
    for line in file:
        if Text ==  line[0:17]:
            movieID.add(line[19:29])


with open('movieID.txt', 'w') as f:
    for movie in movieID:
        f.write(str(movie, encoding='utf-8') + '\n')