#! /usr/bin/env bash

# print the usage and exit
print_usage_and_exit () {
	cat <<____USAGE 1>&2
Usage   : ${0##*/} <docker_file_path>

Execute docker build command.

positional parameters:
  docker_file_path: Dockerfile path
____USAGE
	exit 1
}

# main script starts here

readonly MODULE='calcpi'
readonly IMAGE="gnkm/${MODULE}"
readonly TAG=$(git describe --tags --always --dirty)

docker build \
  -f docker/Dockerfile \
  --no-cache \
  -t "${IMAGE}:${TAG}" \
  ${@:2}
