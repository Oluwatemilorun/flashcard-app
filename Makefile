PG_URI = postgresql://testuser:testpw@database
DB_NAME = flashcard
SERVER = @docker-compose exec server
DB = @docker-compose exec database

start:
	docker-compose up -d --build

build:
	docker-compose build

init-db:
	docker-compose stop server
	$(DB) bash -c "echo 'create database $(DB_NAME)' | psql $(PG_URI)"
	docker-compose start server
	$(SERVER) bash -c "source venv/bin/activate && flask db migrate -m 'Initial migration.' && flask db upgrade"

recreate-db:
	docker-compose stop server
	$(DB) bash -c "echo 'drop database $(DB_NAME)' | psql $(PG_URI) && echo 'create database $(DB_NAME)' | psql $(PG_URI)"
	docker-compose start server
	$(SERVER) bash -c "source venv/bin/activate && flask db upgrade"

start-psql:
	$(DB) psql $(PG_URI)/$(DB_NAME)

start-bash:
	$(SERVER) bash

# Run linters.
lint:
	$(SERVER) bash -c "mypy . && flake8 . && black --check --diff ."

# Format code.
format:
	$(SERVER) bash -c "black ."
