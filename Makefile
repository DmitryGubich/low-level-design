shell := uv run

.PHONY: pre-commit
pre-commit:
	$(shell) pre-commit run --all-files

.PHONY: type-checking
type-checking:
	$(shell) pyre

.PHONY: run-tests
run-tests:
	$(shell) pytest -n auto