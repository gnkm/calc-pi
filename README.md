# calc-pi

![Test, Lint](https://github.com/gnkm/calc-pi/actions/workflows/ci.yml/badge.svg)

Calculate Pi with various algorithms.

## Usage

Make docker image.

```
bash run.sh build
```

Check docker image ID.

```
docker images | grep calcpi | awk '{print $3}'
```

Show help.

```
bash run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) py -m calcpi
```

Calculate Pi.

```
bash run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) py -m calcpi gauss_legendre --accuracy 100 -s
```

Run pylint.

```
bash run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) lint calcpi
```

Run flake8.

```
bash run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) flake
```

Run mypy.

```
bash run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) mypy calcpi
```

Run test.

```
bash run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) test
```
