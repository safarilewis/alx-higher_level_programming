#!/bin/bash
# Sends a POST request with data passed as parameters
curl -sdL "email=test@gmail.com&subject=I&will&always&be&here&for&PLD" "$1"
