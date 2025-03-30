.PHONY:
	prec-ommit_on
	pre-commit_off
	lint
	isort

pre-commit_on:
	pre-commit install
pre-commit_off:
	pre-commit uninstall
lint:
	flake8 .
isort:
	isort .
