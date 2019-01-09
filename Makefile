.SILENT: bootstrap
.PHONY: bootstrap
bootstrap:
	./script/bootstrap
	pipenv shell
