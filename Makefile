init:
	./bootstrap.sh
.PHONY: init

bundle:
	brew bundle
.PHONY: bundle

.DEFAULT_GOAL := bundle
