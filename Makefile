PYTHON = python3

VENV_DIR = .venv

REQUIREMENTS = requirements.txt

SCRIPT = main.py

GREEN = \033[0;32m
RED = \033[0;31m
BLUE = \033[0;34m
YELLOW = \033[0;33m

.PHONY: all run clean run-silent

all: venv install

venv:
	$(PYTHON) -m venv $(VENV_DIR)

install: venv
	@sudo apt install -y python3-venv
	@echo "Installing required packages..."
	@sudo apt install -y python3-pip
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)
	@echo "Installation complete."
	@echo "$(GREEN)To use this application, run $(YELLOW)'make run'."
	@echo "$(GREEN)To use this application with silent mode enabled, run $(YELLOW)'make run-silent'."
	@echo "$(GREEN)To clean up, run $(YELLOW)'make clean'."

run:
	sudo $(VENV_DIR)/bin/python $(SCRIPT)

clean:
	rm -rf $(VENV_DIR) __pycache__ *.pyc

.PHONY: all venv install run clean