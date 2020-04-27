#!/bin/sh
echo "WARNING: This is UNSAFE! Use only locally or with port only accessible via ssh channel!"
jupyter lab --ip=0.0.0.0 --port=${1:-8080} --allow-root
