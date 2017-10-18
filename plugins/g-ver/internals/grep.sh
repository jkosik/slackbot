#!/bin/bash
cat plugins/g-ver/internals/out | grep qcow2 | cut -d">" -f2 | cut -d"<" -f1 | sort -r | head -1
