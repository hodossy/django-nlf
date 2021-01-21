.PHONY: lint
lint:
	@python -m black --check django_nlf tests
	@python -m pylint django_nlf


.PHONY: format
format:
	@python -m black django_nlf tests manage.py setup.py


.PHONY: test
test:
	@python manage.py test $(tc)


.PHONY: coverage
coverage:
	@python -m coverage run manage.py test
	@python -m coverage report


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


# All commands that can be proxied to manage.py
.DEFAULT:
	@python manage.py $@ $(PARAMS)
