#!/bin/bash
cd "$(dirname "$0")"
python3 -m pip install deface
python3 flouter.py
