#!/bin/bash
find  "/root/Documents/Linux_Workshop" -type f -name "*.sh" -exec grep "while" {} \;| cat >>temp.txt
