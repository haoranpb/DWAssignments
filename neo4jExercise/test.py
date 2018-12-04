from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "123"))

def add_actor(tx, actor, movie):
    tx.run("MERGE (actor:Actor{name: $actor_name})", actor_name=actor)
    tx.run("MERGE (movie:Movie{id: $movie_id})", movie_id=movie)
    tx.run("MATCH (actor:Actor), (movie:Movie)"
        "WHERE actor.name={actor_name} AND movie.id={movie_id}"
        "MERGE (actor)-[:ACTED_IN]->(movie)", actor_name=actor, movie_id=movie)

def add_director(tx, director, movie):
    tx.run("MERGE (director:Director{name: $director_name})", director_name=director)
    tx.run("MERGE (movie:Movie{id: $movie_id})", movie_id=movie)
    tx.run("MATCH (director:Director), (movie:Movie)"
        "WHERE director.name={director_name} AND movie.id={movie_id}"
        "CREATE (director)-[:DIRECTED]->(movie)", director_name=director, movie_id=movie)

with driver.session() as session:
    with open('../0tcadmi.txt', 'r') as file:
        for line in file:
            director_name = line[13: line.find('actorname') - 1]
            actor_name = line[line.find('actorname') + len('actorname') + 1: line.find('productidline') - 1]
            movie_id = line[line.find('productidline') + len('productidline') + 1: line.find('nameofmovie') - 1]
            session.write_transaction(add_actor, actor_name, movie_id)
            session.write_transaction(add_director, director_name, movie_id)
