# Hypo
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/koji-kojiro/hylang-hypo/blob/master/LICENSE)
[![python](https://img.shields.io/badge/python-2.6%2B%2C%203.3%2B-red.svg)](https://pypi.python.org/pypi/hypo)
[![PyPI](https://img.shields.io/pypi/v/hypo.svg)](https://pypi.python.org/pypi/hypo)  
[Hy](https://github.com/hylang/hy) is a LISP dialect running on a Python virtual machine. **Hypo** allows you to build small applications from Hy source files. Similar to Python's [zipapp](https://docs.python.org/3/library/zipapp.html), **Hypo** creates executable archives.
Since the Hy source files will be compiled into .pyc files, the executable archive will run faster than on interpreter.

## Requirements
- Python >= (2.6, 3.5)
- Hy >= 0.12.1

## Installation
```
$ pip install hypo
```

## Usage
```
$ hypo --help
usage: hypo [options] <targets>

options:
  -o [file]  output name
  --version  show program's version number and exit
  --help     show this message and exit
```

## Example
You can build these source files as follows:
```
$ hypo -o app main.hy iota.hy
```
And you can execute the application as follows:
```
$ ./app
(0L 1L 2L 3L 4L 5L 6L 7L 8L 9L)
```
or
```
$ python app
(0L 1L 2L 3L 4L 5L 6L 7L 8L 9L)
```

### Source files
- iota.hy

```clj
(defn iota [m &optional [n 0] [step 1]]
  (if (>= n m)
    None
    (cons n (iota m (+ n step) step))))
```

- main.hy

```clj
(import [iota [iota]])

(defmain [&rest args]
  (print (iota 10)))
```

## License
Distributed under [MIT License](https://github.com/koji-kojiro/hylang-hypo/blob/master/LICENSE).  

## Author
[Kojiro TANI](https://github.com/koji-kojiro "koji-kojiro") (kojiro0531@gmail.com)

