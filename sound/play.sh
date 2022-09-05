#!/bin/sh

for wavfile in $*
do
  aplay --quiet $wavfile
done
