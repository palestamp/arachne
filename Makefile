

clean:
	@rm -rf `find . -name __pycache__`
	@rm -f `find . -type f -name '*.py[co]' `
	@rm -rf arachno.egg-info
	@rm -rf build
	@rm -rf dist


build: clean
	python setup.py sdist bdist_wheel


publish: build
	twine upload dist/*


.PHONY: build clean