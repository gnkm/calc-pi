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

readonly MODULE=$(cat registry.toml | grep 'module' | awk '{print $3}' | sed -e 's/"//g')
readonly OWNER=$(cat registry.toml | grep 'owner' | awk '{print $3}' | sed -e 's/"//g')
readonly REGISTRY=$(cat registry.toml | grep 'registry' | awk '{print $3}' | sed -e 's/"//g')
readonly TAG=$(git describe --tags --always --dirty)
readonly IMAGE="${REGISTRY}/${OWNER}/${MODULE}:${TAG}"

docker build \
  -f docker/Dockerfile \
  --no-cache \
  -t "${IMAGE}" \
  .
