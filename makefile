install:
	@echo "--- 🚀 Installing project dependencies ---"
	uv sync

test:
	@echo "--- 🧪 Running tests ---"
	uv run pytest src/tests/ | tee test_results.log

lint:
	@echo "--- 🧹 Running linters ---"
	uv run ruff format . 			# running ruff formatting
	uv run ruff check . --fix  	# running ruff linting

lint-check:
	@echo "--- 🧹 Check is project is linted ---"
	uv run ruff format . --check						    # running ruff formatting
	uv run ruff check **/*.py 						        # running ruff linting

bump-version:
	@echo "--- 🚀 Bumping patch version ---"
	uv run src/dynaword/bump_version.py