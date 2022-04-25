.PHONY: all configure build run

CONFIG_PATH?="config.json"

all:
		configure run
configure:
		@python setup.py $(CONFIG_PATH)

build:
		docker-compose build

run:
		@docker-compose up -d --build
