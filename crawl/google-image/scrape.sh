#!/bin/bash

# Define the number of instances to run
rm core.*
NUM_INSTANCES=110

echo "Total instance: $NUM_INSTANCES"

for ((i=0; i<$NUM_INSTANCES; i++)); do
	/home/ubuntu/hafiz-scrape-work/scrape-google-image-old/scrape_env/bin/python main_extended.py &
done

# Wait for all instances to finish
wait

echo "All instances have finished."
