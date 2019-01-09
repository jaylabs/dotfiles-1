#!/bin/zsh

function cd {
  builtin cd "$@"
  if [ -f "Pipfile.lock" ]; then
    pipenv shell
  fi
}
