#!/bin/bash
until
  
  python3 main.py
  
  [ "python3" -ne 127 ]
do

  echo You might not have python3 installed...
  
done
