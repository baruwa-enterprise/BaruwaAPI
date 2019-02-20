.PHONY: sdist check upload test default

default: test

sdist:
	@echo "Building tarball"
	python setup.py sdist bdist_wheel

check:
	twine check dist/*

upload:
	twine upload dist/*

test:
	nosetests
