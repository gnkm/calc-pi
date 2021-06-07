#! /usr/bin/env bash

readonly MODULE=$(cat registry.toml | grep 'module' | awk '{print $3}' | sed -e 's/"//g')
readonly OWNER=$(cat registry.toml | grep 'owner' | awk '{print $3}' | sed -e 's/"//g')
readonly IMAGE="${OWNER}/${MODULE}"
readonly TAG=$(docker images | ag ${IMAGE} | head -1 | awk '{print $2}')
readonly REGISTRY=$(cat registry.toml | grep 'registry' | awk '{print $3}' | sed -e 's/"//g')
readonly TAGGED_IMAGE="${REGISTRY}/${IMAGE}:${TAG}"

docker push ${TAGGED_IMAGE}
