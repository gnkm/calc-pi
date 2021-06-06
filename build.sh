#! /usr/bin/env bash

# print the usage and exit
print_usage_and_exit () {
	cat <<____USAGE 1>&2
Usage   : ${0##*/}

Execute docker build command.
____USAGE
	exit 1
}

# main script starts here

readonly MODULE='calcpi'
readonly OWNER='gnkm'
readonly TAG=$(git describe --tags --always --dirty)
readonly IMAGE="ghcr.io/${OWNER}/${MODULE}:${TAG}"

docker build \
  -f docker/Dockerfile \
  --no-cache \
  -t "${IMAGE}" \
  .
