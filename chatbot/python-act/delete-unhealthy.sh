#!/bin/bash

# Get the IDs of all containers
container_ids=$(docker ps -aq)

# Loop through each container
for container_id in $container_ids; do
    # Get the health status of the container
    health_status=$(docker inspect --format='{{.State.Health.Status}}' $container_id)

    # Check if the container is unhealthy
    if [ "$health_status" = "unhealthy" ]; then
        # Remove the unhealthy container
        docker rm $container_id -f
    fi
done