pyrus
=====

This is designed to be a utility module that provides simplified helpers for useful pythonic tasks. This currently includes:
- mplogging - A module that provides an easy queue based method for multiprocessor safe logging
- archives - A module that wraps zipfile and tarfile modules with common method signatures. This also provides native archive file handling if implemented (uses unzip/tar on unix machines) and also facilitates the complete in-memory processing of an archive file.
- checksum - A helper module to handle fingerprinting of in-memory and on-disk objects dynamically.
- download - A module that acts as a multiprocess aware download manager that can handle both async/blocking download requests.

Installation
-----
You can install this using _easy_install_ or _pip_
```bash
easy_install http://github.com/abn/pyrus/tarball/master#egg=pyrus-0.0.1
```

```bash
pip http://github.com/abn/pyrus/tarball/master#egg=pyrus-0.0.1
```
*NOTE:* This is not a stable module yet, so I suggest using a virtualenv.

Setup under a virtualenv
-----
This is one way of setting it up, you can choose to include __--system-site-packages__ if you want any of the global modules to be available.
```bash
# required only once
virtualenv -p $(which python3) --prompt=pyrus.env pyrus.env
# activate the env
source pyrus.env/bin/activate
# required only once, unless you are reinstalling etc.
pip http://github.com/abn/pyrus/tarball/master#egg=pyrus-0.0.1
```

Py´rus
-----
n.  1.  (Bot.) A genus of rosaceous trees and shrubs having pomes for fruit.
