#!/bin/bash
# This script returns the size of the respose body type
curl -so /dev/null "$1" -w "%{size_download}"