#!/bin/bash
export PYTHONPATH=$PWD:$PWD/core:$PWD/packages:$PWD/versions:$PYTHONPATH
echo "snoing setup"
printf "%-50s" "Checking for git..."
which git &> /dev/null
test $? -eq 0 && printf "Installed\n" || printf "Not Installed\n"
printf "%-50s" "Checking if this is a git repository..."
git branch &> /dev/null
test $? -eq 0 && USEGIT=1 || USEGIT=0
test $USEGIT -eq 1 && printf "yes\nAttempting update via git pull...\n" || printf "no\n"
test $USEGIT -eq 1 && git pull
