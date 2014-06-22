# cookiecutter-pypackage

[Cookiecutter](http://cookiecutter.rtfd.org) template for a Python package.
Based on <https://github.com/audreyr/cookiecutter-pypackage>.

## Features
- Optional sample CLI using [click](http://click.pocoo.org)
- Testing with [unittest2]() and [nosetest]()
- [TravisCI](http://travis-ci.org/) integratioin
- [Tox](http://testrun.org/tox/) testing: Defaults to test Python 2.6, 2.7, 3.3
- [Sphinx](http://sphinx-doc.org/) docs: Documentation ready for
  generation with, for example, [ReadTheDocs](https://readthedocs.org/)
- Used by [changes](http://changes.rtfd.org) to generate new packages

## Usage

Generate a Python package project:

    cookiecutter https://github.com/michaeljoseph/cookiecutter-pypackage.git
