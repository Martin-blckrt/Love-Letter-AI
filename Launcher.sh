#!/bin/bash

if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 might not be installed.' >&2
  exit 1
else
  python3 -u main.py

fi
