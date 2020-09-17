
# https://packaging.python.org/tutorials/packaging-projects/
#
# https://test.pypi.org/project/jitterbit-pkg-bbrummer/

PYTHON=python3.7

package:
	${PYTHON} setup.py sdist bdist_wheel

upload:
	${PYTHON} -m twine upload --repository testpypi dist/*

install:
	${PYTHON} -m pip install --ignore-installed --index-url https://test.pypi.org/simple/ --no-deps jitterbit-pkg-bbrummer

uninstall:
	${PYTHON} -m pip uninstall --yes jitterbit-pkg-bbrummer

clean:
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf build/
