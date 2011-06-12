#!/bin/bash

for i in $(ls sections); do
   echo processing $i...
  ./bf_alg.py sections/$i results/$i
done


