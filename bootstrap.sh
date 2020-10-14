#!/bin/bash 

if test ! $(which brew)
then
  echo "~> Installing Homebrew for you\n"

  # Install the correct homebrew for each OS type
  if test "$(uname)" = "Darwin"
  then
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  elif test "$(expr substr $(uname -s) 1 5)" = "Linux"
  then
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)"
  fi

fi

brew tap Homebrew/bundle

echo "~> setting up tools\n"

echo "~> zsh\n"
mkdir -p $HOME/.zsh
cp -R zsh/*.zsh $HOME/.zsh/
cp -R zsh/zshrc $HOME/.zshrc

mkdir -p $HOME/.zkbd
cp -R zsh/*-256color $HOME/.zkbd

echo "~> git\n"
mkdir -p $HOME/.git
cp -R git/* $HOME/.git
cp -R git/gitconfig $HOME/.gitconfig
cp -R git/gitconfig.lib $HOME/.gitconfig.lib

exit 0
