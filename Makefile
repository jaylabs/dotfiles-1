init:
	./bootstrap.sh
.PHONY: init

bundle:
	brew bundle
.PHONY: bundle

dump:
	brew bundle dump --force
.PHONY: dump

.DEFAULT_GOAL := bundle
