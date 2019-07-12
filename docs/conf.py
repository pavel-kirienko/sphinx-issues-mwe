import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).absolute().parent.parent))
import sphinx_demo

project = 'demo'
copyright = '2019, nobody'
author = 'nobody'

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = []

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

master_doc = 'index'

autoclass_content = 'bysource'
autodoc_member_order = 'bysource'

html_theme = 'alabaster'

html_static_path = []
