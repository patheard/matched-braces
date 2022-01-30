fmt:
	black .

install:
	pip3 install --user -r requirements.txt

lint:
	pylint matched_braces.py

test:
	python -m pytest -s -vv

.PHONY: \
	fmt \
	install	\
	lint \
	test