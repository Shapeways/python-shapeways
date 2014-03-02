Python Shapeways
================

[![Build Status](https://travis-ci.org/Shapeways/python-shapeways.png?branch=master)](https://travis-ci.org/Shapeways/python-shapeways)
[![Coverage Status](https://coveralls.io/repos/Shapeways/python-shapeways/badge.png?branch=master)](https://coveralls.io/r/Shapeways/python-shapeways?branch=master)
[![PyPI version](https://badge.fury.io/py/shapeways.png)](http://badge.fury.io/py/shapeways)
[![Shapeways API Version](http://b.repl.ca/v1/shapeways--api-v1-brightgreen.png)](https://developers.shapeways.com/docs)


Python module for interacting with the [Shapeways](http://www.shapeways.com) api [http://developers.shapeways.com](http://developers.shapeways.com).

## Installation
### PIP
```bash
pip install shapeways
```

### Git
```bash
git clone git://github.com/Shapeways/python-shapeways.git
cd ./python-shapeways
make install

# or

pip install -r requirements.txt
python setup.py install
```

## API

The Latest documentation can be found at [ReadTheDocs](http://pyton-shapeways.readthedocs.org).

Build the sphinx documentation from the `docs` directory.

```bash
git clone git://github.com/Shapeways/python-shapeways.git
cd ./python-shapeways
make docs
```

Open `docs/_build/html/index.html` in a web browser to view documentation.

## Examples
See `examples` directory.

## Versions before 1.0.0

The original client was written and maintained by @pauldw for information about versions earlier
than v1.0.0 please visit [https://github.com/pauldw/shapeways-python](https://github.com/pauldw/shapeways-python)

## License
```
The MIT License (MIT) Copyright (c) 2014 Shapeways <api@shapeways.com> (http://developers.shapeways.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
