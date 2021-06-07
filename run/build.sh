#! /usr/bin/env bash

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
