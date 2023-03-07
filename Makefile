test:
	poetry run pytest tests -vv

format:
	poetry run isort --profile=black .
	poetry run black .
