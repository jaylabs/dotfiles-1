init:
	./bootstrap.sh
.PHONY: init

bundle:
	brew bundle
.PHONY: bundle

brew-dump:
	brew bundle dump --force
.PHONY: brew-dump

.DEFAULT_GOAL := bundle
