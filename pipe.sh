#!/bin/bash

chmod +x pipe.sh
py main.py
py preprocessor.py
py png_to_csv.py
py paint.py


echo "Programa pipe.sh finaliza"