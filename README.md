# calc-pi

![Test, Lint](https://github.com/gnkm/calc-pi/actions/workflows/ci.yml/badge.svg)

Calculate Pi with various algorithms.

## Usage

Images: [Package calcpi](https://github.com/users/gnkm/packages/container/package/calcpi)

Make docker image.

```
bash run/build.sh
```

Check docker image ID.

```
docker images | grep calcpi | awk '{print $3}'
```

Show help.

```
bash run/run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) py -m calcpi
```

Calculate Pi.

```
bash run/run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) py -m calcpi gauss_legendre --accuracy 100 -s
```

Run pylint.

```
bash run/run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) lint calcpi
```

Run flake8.

```
bash run/run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) flake
```

Run mypy.

```
bash run/run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) mypy calcpi
```

Run test.

```
bash run/run.sh $(docker images | grep calcpi | awk '{print $3}' | head -1) test
```
