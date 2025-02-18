start:
	@echo "Starting awake script...\n"
	@python3 awake.py &

stop:
	@echo "Stopping awake script...\n"
	@if [ -f awake.pid ]; then \
		kill $$(cat awake.pid); \
		rm -f awake.pid; \
		if [ -f awake.log ]; then \
			MOVED_COUNT=$$(grep -c "Mouse moved." awake.log); \
			echo "Here's the log file summary: Your mouse had moved $$MOVED_COUNT times in this session.\n"; \
			rm -f awake.log; \
		else \
			echo "No log file found.\n"; \
		fi; \
		echo "Program stopped.\n"; \
	else \
		echo "No running instance found.\n"; \
	fi

logs:
	@if [ -f awake.log ]; then \
		echo "Contents of awake.log:\n"; \
		cat awake.log; \
	else \
		echo "No log file found.\n"; \
	fi

status:
	@echo "Checking the pid of awake script...\n";
	@if [ -f awake.pid ]; then \
		echo "Your process PID is $$(cat awake.pid).\n"; \
	else \
		echo "Awake script is not running.\n"; \
	fi

.PHONY: start stop status logs check