PYTHON = python3
MAIN_FILE = main.py
PYCACHE_DIR = __pycache__

run:
	$(PYTHON) $(MAIN_FILE)

clean:
	rm -rf $(PYCACHE_DIR)

fclean: clean

.PHONY: run clean fclean
