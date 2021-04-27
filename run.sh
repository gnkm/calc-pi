#! /usr/bin/env bash

# print the usage and exit
print_usage_and_exit () {
	cat <<____USAGE 1>&2
Usage   : ${0##*/} <var1> <var2> ...
____USAGE
	exit 1
}

# main script starts here

MODULE='calcpi'
IMAGE="gnkm/${MODULE}"
TAG=$(git describe --tags --always --dirty)

# build
case $1 in
    'build' )
        docker build \
            -f docker/Dockerfile \
            --no-cache \
            -t "${IMAGE}:${TAG}" \
            .
        exit 0;;
esac

# alias of `docker run`
IMAGE_ID=$1

case $2 in
    'py' )
        docker run \
            -v $PWD:/tmp/working \
            -w=/tmp/working \
            --rm \
            -it \
            --name calcpi \
            ${IMAGE_ID} \
            python ${@:3};;
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
