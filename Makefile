venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -e venv/bin/activate || python -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

install_hooks: venv
	venv/bin/pre-commit install

.PHONY: test clean run install
test: venv
	@(. venv/bin/activate; \
		pip install -e .;\
		coverage run venv/bin/pytest; \
		coverage report -m --fail-under 100 --omit=venv/*;\
		rm -rf outpost.egg-info;\
	)

clean:
	rm -rf venv

run: venv
	@(. venv/bin/activate;\
		gunicorn --bind 0.0.0.0:8000 wsgi;\
 	)

