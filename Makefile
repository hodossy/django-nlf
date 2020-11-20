.PHONY: lint
lint:
	@python -m black --check django_nlf tests
	@python -m pylint django_nlf


.PHONY: format
format:
	@python -m black django_nlf tests


.PHONY: test
test:
	@python runtests.py $(tc)


.PHONY: coverage
coverage:
	@python -m coverage run --branch runtests.py
	@python -m coverage report --show-missing --include "**/django_nlf/**"


.PHONY: docs
docs:
	@python -m sphinx -b html docs docs/_build


.PHONY: publish
publish:
	@python setup.py sdist bdist_wheel
	@twine upload dist/*

.PHONY: lang
lang:
	@$(MAKE) -C ./django_nlf/antlr
