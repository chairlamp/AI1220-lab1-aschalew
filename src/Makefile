DIR ?= ../receipts
ENV_FILE ?= ../.env
PYTHONPATH := $(abspath ..)

run:
	@ set -a; \
	  [ -f $(ENV_FILE) ] && . $(ENV_FILE); \
	  set +a; \
	  if [ -z "$${OPENAI_API_KEY:-}" ]; then \
	    echo "Set OPENAI_API_KEY in environment or $(ENV_FILE) to run the extractor."; \
	    exit 1; \
	  fi; \
	  PYTHONPATH=$(PYTHONPATH) OPENAI_API_KEY=$${OPENAI_API_KEY} python main.py $(DIR) --print
