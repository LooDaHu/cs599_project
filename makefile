.PHONY:
	help
	prepare-dev
	run
	rvenv

VENV_NAME?=venv
VENV_ACTIVATE=${VENV_NAME}/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make prepare-dev"
	@echo "       prepare development environment, use only once"
	@echo "make rvenv"
	@echo "       set virtual environment"
	@echo "make run"
	@echo "       run project"


# Install python and set up virtual environment
prepare-dev:
	sudo apt-get -y install python3.6 python3-pip
	python -m venv venv

# enter virtual environment
rvenv:
	source ${VENV_ACTIVATE}

run: rvenv
	${PYTHON} main.py

