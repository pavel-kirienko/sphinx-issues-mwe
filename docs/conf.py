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

autoclass_content = 'bysource'
autodoc_member_order = 'bysource'
autodoc_default_flags = [  # using the deprecated option to appease the readthedocs' builder
    'members',
    'undoc-members',
    'imported-members',
    'show-inheritance',
]

html_theme = 'alabaster'

html_static_path = []
