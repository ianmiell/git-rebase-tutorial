#!/bin/bash
# Example for running
DOCKER=${DOCKER:-docker}
IMAGE_NAME=%s
CONTAINER_NAME=$IMAGE_NAME
DOCKER_ARGS=''
while getopts "i:c:a:" opt
do
    case "$opt" in
    i)
        IMAGE_NAME=$OPTARG
        ;;
    c)
        CONTAINER_NAME=$OPTARG
        ;;
    a)
        DOCKER_ARGS=$OPTARG
        ;;
    esac
done
${DOCKER} run -d --name ${CONTAINER_NAME} git_rebase_tutorial    ${DOCKER_ARGS} ${IMAGE_NAME}  /bin/sh -c 'sleep infinity'
