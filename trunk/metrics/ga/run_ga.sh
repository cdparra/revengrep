#!/bin/bash

for i in $(ls sections); do
   echo processing $i...
  ./gen_alg.py sections/$i results/$i
done


