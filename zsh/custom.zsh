#!/bin/zsh

function auto_pipenv_shell {
  if [ -f "Pipfile.lock" ]; then
    pipenv shell
  fi
}

function cd {
    builtin cd "$@"
    auto_pipenv_shell
}
