# Start Neo4j
docker-compose up -d

# View logs
docker-compose logs -f neo4j

# Stop Neo4j
docker-compose down

# Stop and remove volumes (⚠️ deletes all data)
docker-compose down -v