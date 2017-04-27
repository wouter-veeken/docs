#!/usr/bin/env python
import os

import jinja2
import yaml

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = jinja2.Environment(
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.join(PATH, 'data')),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def load_styles():
    out = os.path.join('content', 'showcase.md')
    with open(out, 'w+') as o, open(os.path.join('data', 'styles.yml')) as d:
        html = render_template('showcase.md', {'data': yaml.load(d)})
        o.write(html)


if __name__ == '__main__':
    load_styles()
