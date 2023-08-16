#!/bin/bash
nginx -g 'daemon off;'
 
/wait-for-it.sh django:8000 --timeout=0 -- nginx -g 'daemon off;'