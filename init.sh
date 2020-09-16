#!/bin/bash

set -e

RUN=$(which brew)

xargs ${RUN} install < brew-list
xargs ${RUN} install < brew-list-cask
