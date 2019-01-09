.SILENT: bootstrap
.PHONY: bootstrap
bootstrap:
	./script/bootstrap
	pipenv shell

.SILENT: run
.PHONY: run
run:
	pipenv run ansible-playbook playbooks/main.yml
