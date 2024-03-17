PYTHON = python3
MAIN_FILE = src/main.py
PYCACHE_DIR = src/include/__pycache__

all: run

run:
	$(PYTHON) $(MAIN_FILE)

clean:
	rm -rf $(PYCACHE_DIR)

fclean: clean

re:	fclean	all

.PHONY: run clean fclean
