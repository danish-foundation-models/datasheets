install:
	@echo "--- 🚀 Installing project dependencies ---"
	uv sync

test:
	@echo "--- 🧪 Running tests ---"
	uv run pytest src/tests/ | tee test_results.log

lint:
	@echo "--- 🧹 Running linters ---"
	uv run ruff format . 			# running ruff formatting
	uv run ruff check . --fix  		# running ruff linting

lint-check:
	@echo "--- 🧹 Check is project is linted ---"
	uv run ruff format . --check						    # running ruff formatting
	uv run ruff check . 							        # running ruff linting

bump-version:
	@echo "--- 🚀 Bumping patch version ---"
	uv run src/datasheets/bump_version.py

generate-sheet:
	@echo "--- 📊 Generating datasheet ---"
	uv run src/datasheets/generate_sheet.py

update-stats:
	@echo "--- 🚀 Recomputing Descriptive statistics ---"
	uv run src/datasheets/update_descriptive_statistics.py

add-datasheet:
	@echo "--- 💾 Adding a new datasheet ---"
	@$(MAKE) generate-sheet
	@$(MAKE) update-stats