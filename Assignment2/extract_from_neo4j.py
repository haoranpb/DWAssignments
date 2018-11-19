from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "123"))

def extract(tx):
    result = tx.run("MATCH (actor:Actor)-[:ACTED_IN]->(movie:Movie)<-[:DIRECTED]-(director:Director)"
        "RETURN actor.name, director.name, count(movie)"
        "ORDER BY count(movie) DESC")
    return [(record['actor.name'], record['director.name'], record['count(movie)']) for record in result]

with driver.session() as session:
    with open('./result.txt', 'w') as file:
        for line in session.read_transaction(extract):
            if len(line[1]) > 3:
                file.write(line[0] + ' | ' + line[1] + ' | ' + str(line[2]) + '\n')
