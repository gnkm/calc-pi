#! /usr/bin/env bash

# print the usage and exit
print_usage_and_exit () {
	cat <<____USAGE 1>&2
Usage   : ${0##*/}

Execute docker push command.
____USAGE
	exit 1
}

# main script starts here

readonly MODULE='calcpi'
readonly OWNER='gnkm'
readonly IMAGE="${OWNER}/${MODULE}"
readonly TAG=$(docker images | ag ${IMAGE} | head -1 | awk '{print $2}')
readonly TAGGED_IMAGE="ghcr.io/${IMAGE}:${TAG}"

docker push ${TAGGED_IMAGE}
