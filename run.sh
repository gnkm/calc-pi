#! /usr/bin/env bash

# print the usage and exit
print_usage_and_exit () {
	cat <<____USAGE 1>&2
Usage   : ${0##*/} <var1> <var2> ...
____USAGE
	exit 1
}

# main script starts here

readonly MODULE='calcpi'
readonly IMAGE="gnkm/${MODULE}"
readonly TAG=$(git describe --tags --always --dirty)

build() {
  docker build \
    -f docker/Dockerfile \
    --no-cache \
    -t "${IMAGE}:${TAG}" \
    .
}

_python() {
  local IMAGE_ID=$1
  docker run \
    -v $PWD:/tmp/working \
    -w=/tmp/working \
    --rm \
    -it \
    --name calcpi \
    ${IMAGE_ID} \
    python ${@:2}
}

# build
case $1 in
  'build' )
    build
    exit 0;;
esac

# alias of `docker run`
IMAGE_ID=$1

case $2 in
  'py' )
    _python ${IMAGE_ID} ${@:3}
    exit 0;;
    'lint' )
        docker run \
            -v $PWD:/tmp/working \
            -w=/tmp/working \
            --rm \
            -it \
            --name calcpi \
            ${IMAGE_ID} \
            pylint ${@:3};;
    'flake' )
        docker run \
            -v $PWD:/tmp/working \
            -w=/tmp/working \
            --rm \
            -it \
            --name calcpi \
            ${IMAGE_ID} \
            flake8 ${@:3};;
    'mypy' )
        docker run \
            -v $PWD:/tmp/working \
            -w=/tmp/working \
            --rm \
            -it \
            --name calcpi \
            ${IMAGE_ID} \
            mypy ${@:3};;
    'test' )
        docker run \
            -v $PWD:/tmp/working \
            -w=/tmp/working \
            --rm \
            -it \
            --name calcpi \
            ${IMAGE_ID} \
            pytest ${@:3};;
    * )
        docker run \
            -v $PWD:/tmp/working \
            -w=/tmp/working \
            --rm \
            -it \
            --name calcpi \
            ${IMAGE_ID} \
            ${@:2};;
esac
