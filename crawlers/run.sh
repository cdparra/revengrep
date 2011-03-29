#!/bin/bash
echo "calculating h-index..."
time ./google_scholar.py authors.txt results.txt 100 3
#time ./google_scholar.py short.txt results.txt 100 2

