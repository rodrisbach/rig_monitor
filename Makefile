.PHONY: configure build run

CONFIG_PATH?="config.json"

configure:
	python setup.py $(CONFIG_PATH)
