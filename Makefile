install:
	poetry install
	
brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user ./dist/*.whl

package-install-force:
	python3 -m pip install --force-reinstall --user ./dist/*.whl

make lint:
	poetry run flake8 brain_games