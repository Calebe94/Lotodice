############
# Lotodice #
############

upload:
	@. venv/bin/activate; pip install --upgrade twine; twine upload dist/* --verbose

test:
	@python -m unittest tests.test

build:
	@virtualenv venv
	@. venv/bin/activate; pip install --upgrade build; python -m build

install:
	@pip install .
	install -m 555 script/lotodice-run ~/.local/bin/lotodice-run

clean:
	@rm -fr build dist venv src/lotodice.egg-info src/lotodice/__pycache__

.PHONY: build test install clean
