#!/bin/bash
export PYTHONPATH=$PWD:$PWD/core:$PWD/packages:$PYTHONPATH
echo "snoing setup"
git pull
echo "snoing updated."