#!/usr/bin/env python3
"""Python md to HTML converter with YAML

Usage:
    pyconverter.py    FILE [--pandoc_args | -h]

Arguments:
    file           the file to convert

Options:
    -h, --help     Show this screen.
    --pandoc_args  option list of arguments for pandoc
"""
from docopt import docopt

"""
    pyconverter.py uses Pandoc internally to convert a markdown file to an html
    file. The only reason this was necessary was to find a way to keep the damn
    YAML front matter in the converted HTML file. You may pass arbitrary arguments
    to pandoc via optional command line args.
"""

import yaml as ym
import frontmatter as fm
import pypandoc as pd


def main(_args):
    """ Does the things."""
    print("Converting {computer}".format(computer=_args["FILE"]))
    if _args["--pandoc_args"]:
        pdoc_args = _args["--pandoc_args"]
    else:

        filters = ['pandoc-citeproc']
        pdoc_args = ['--mathjax',
                     '--smart'
                     ]
    filename = _args['FILE']
    basename = filename.split('.')[0]

    post = fm.load(filename)
    filedate = post.metadata['date']
    file_frontmatter = ('---\n' + ym.dump(post.metadata) + '---\n')

    output = pd.convert(source=filename,
                        to='html5',
                        format='md',
                        extra_args=pdoc_args,
                        filters=filters)
    out = (file_frontmatter + '\n' + output)

    write_name = (str(filedate) + '-' + basename + '.html')
    # writes file friend for Jekyll
    with open(write_name, mode='w') as f:
        f.write(out)


if __name__ == "__main__":
    main(docopt(__doc__))
