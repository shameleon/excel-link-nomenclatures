#############################
#### virtual environment ####
#############################

# all recipe lines for each target will be provided to a single invocation of the shell
# ONESHELL special target appears anywhere in the makefile then all recipe lines for each target will be provided to a single invocation of the shell.
.ONESHELL:

# make alone will run
.DEFAULT_GOAL := $(VENV)

SRC		:= ./dslr/

# virtual environment, pip and python
VENV		:= ./venv/
ACTIVATE	= $(VENV)bin/activate
V_PIP		= ./venv/bin/pip
V_PY		= ./venv/bin/python
V_FLAKE		= ./venv/bin/flake8 

# all: $(VENV)

$(ACTIVATE): requirements.txt
	@echo "$(CR)➜$(CG) Installing Virtual Environment $(CZ)"
	virtualenv $(VENV)
	@echo "$(CR)➜$(CG) venv pip is installing requirements $(CZ)"
	$(V_PIP) install -r requirements.txt

$(VENV): $(ACTIVATE)

#  list all the Python packages installed in an environment,
list:
	$(V_PY) -m pip list

flake: $(VENV)
	$(V_FLAKE) *.py
	$(V_FLAKE) $(SRC)

clean:
	@echo "$(CG)➜$(CR) Removing __pycache__  $(CZ) ✗"
	find . -type d -name "__pycache__" | xargs rm -rf {};
#	@echo "$(CG)➜$(CR) Removing .pyc files $(CZ) ✗"
#	find -iname "*.pyc" -delete

fclean: clean
	@echo "$(CG)➜$(CR) Removing virtual environment $(VENV) $(CZ)"
	rm -rf $(VENV)

re: fclean $(VENV)

.PHONY: all list flake clean fclean re

# colors
CR:=\033[1;31m
CG:=\033[1;32m
CZ:=\033[0m

# ON:
# source ./venv/bin/activate
# OFF:
# deactivate
# source deactivate