# Vale Docs [![Build Status](https://travis-ci.org/ValeLint/docs.svg?branch=master)](https://travis-ci.org/ValeLint/docs)

This repository houses the documentation and website source for [Vale](https://github.com/ValeLint/vale). We write our documentation in [Markdown](http://commonmark.org/) and use [MkDocs](http://www.mkdocs.org/) to build it.

### Running Locally

You'll need [Python 2.7+](https://www.python.org/downloads/) installed. Then, just enter the following commands:

```bash
$ git clone https://github.com/ValeLint/docs.git
$ cd docs
$ pip install -r requirements.txt
$ mkdocs serve
```

### Linting

We follow 18F's [content guidelines](https://pages.18f.gov/content-guide/) with the following additions:

<!-- vale off -->

- Use standard American English spelling (e.g., "color" instead of "colour").
- Capitalize "Vale" unless specifically referring to the binary (in which case it should be in a code span&mdash;i.e., `vale`).
- Use correct tech terminology: JavaScript, HTML, etc.

We also use [`awesome_bot`](https://github.com/dkhamsing/awesome_bot) to check that all our links are working.

