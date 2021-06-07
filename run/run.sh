#! /usr/bin/env bash

# print the usage and exit
print_usage_and_exit () {
	cat <<____USAGE 1>&2
Usage   : ${0##*/} <image_id> {build,py,lint,flake,mypy,test,or any other command} ...

Execute docker run command.

positional parameters:
  image_id: Docker image id
  {build, py, lint, flake, mypy, test, or any other command}: command
____USAGE
	exit 1
}

# main script starts here

if [ $# -lt 2 ]; then
  print_usage_and_exit
fi

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

_pylint() {
  local IMAGE_ID=$1
  docker run \
    -v $PWD:/tmp/working \
    -w=/tmp/working \
    --rm \
    -it \
    --name calcpi \
    ${IMAGE_ID} \
    pylint ${@:2}
}

_flake8() {
  local IMAGE_ID=$1
  docker run \
    -v $PWD:/tmp/working \
    -w=/tmp/working \
    --rm \
    -it \
    --name calcpi \
    ${IMAGE_ID} \
    flake8 ${@:2}
}

_mypy() {
  local IMAGE_ID=$1
  docker run \
    -v $PWD:/tmp/working \
    -w=/tmp/working \
    --rm \
    -it \
    --name calcpi \
    ${IMAGE_ID} \
    mypy ${@:2}
}

_pytest() {
  local IMAGE_ID=$1
  docker run \
    -v $PWD:/tmp/working \
    -w=/tmp/working \
    --rm \
    -it \
    --name calcpi \
    ${IMAGE_ID} \
    pytest ${@:2}
}

_unix_command() {
  local IMAGE_ID=$1
  docker run \
    -v $PWD:/tmp/working \
    -w=/tmp/working \
    --rm \
    -it \
    --name calcpi \
    ${IMAGE_ID} \
    ${@:2}
}

# alias of `docker run`
if [ $# -lt 2 ]; then
  print_usage_and_exit
fi

IMAGE_ID=$1

case $2 in
  'py' )
    _python ${IMAGE_ID} ${@:3}
    exit 0;;
  'lint' )
    _pylint  ${IMAGE_ID} ${@:3}
    exit 0;;
  'flake' )
    _flake8  ${IMAGE_ID} ${@:3}
    exit 0;;
  'mypy' )
    _mypy  ${IMAGE_ID} ${@:3}
    exit 0;;
  'test' )
    _pytest  ${IMAGE_ID} ${@:3}
    exit 0;;
  * )
    _unix_command ${IMAGE_ID} ${@:2}
    exit 0;;
esac
