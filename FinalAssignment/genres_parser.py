import redis

def genres_parser():
    db = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)
    result = {}
    for key in db.keys():
        movie_id = key[-10:]
        if movie_id == "w_movie_id" or key == "useful_proxy" or key == "raw_proxy":
            continue
        movie = db.hgetall(key)

        raw_genre = ''
        if 'genre' in movie and movie['genre'] != 'None':
            raw_genre = movie['genre']
        else:
            raw_genre = movie['genres']

        if raw_genre in result:
            result[raw_genre] += 1
        else:
            result[raw_genre] = 1

    return result

if __name__ == '__main__':

    print(genres_parser())
