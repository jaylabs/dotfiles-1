#!/bin/bash

set -e

RUN=$(which brew)

xargs ${RUN} install < brew-list
xargs ${RUN} cask install < brew-list-cask
