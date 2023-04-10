PYTHON := poetry run
PACKAGE_DIRECTORY := src
TESTS_DIRECTORY := tests

.PHONY: install
install:
	poetry install --with test,lint

.PHONY: lint
lint:
	$(PYTHON) flake8 $(PACKAGE_DIRECTORY) --exit-zero
	$(PYTHON) isort $(PACKAGE_DIRECTORY) --check --exit-zero
	$(PYTHON) mypy $(PACKAGE_DIRECTORY) --exit-zero

.PHONY: test
test:
	$(PYTHON) pytest $(TESTS_DIRECTORY)

.PHONY: up
up:
	docker-compose --profile api up --build -d

.PHONY: down
down:
	docker-compose --profile api down

.PHONY: migrate
migrate:
	# verify that database is up
	$(PYTHON) alembic upgrade head
