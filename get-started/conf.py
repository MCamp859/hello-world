# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

SOURCE_DIR = os.path.dirname(__file__)
LATEX_DIR = os.path.join(SOURCE_DIR, '_latex')
PREAMBLE_FILE = os.path.join(LATEX_DIR, 'preamble.tex')
TITLE_PAGE_FILE = os.path.join(LATEX_DIR, 'title_page.tex')

# -- Project information -----------------------------------------------------

project = u'Edge Insights for Fleet'
copyright = u'2022, Intel'
author = u'Intel'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''

# conditions
os_version = "Linux"

rst_prolog = """
.. |EIF| replace:: Edge Insights for Fleet
"""
def setup(app):  # register variables you'd like to use here
    app.add_config_value('os_version', '', 'env')
    
# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#    'sphinx.ext.autodoc',
#    'sphinx.ext.doctest',
#    'sphinx.ext.intersphinx',
#    'sphinx.ext.todo',
#    'sphinx.ext.coverage',
#    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
#    'sphinx.ext.viewcode',
#    'sphinx.ext.githubpages',
#    'breathe',                           #todd-mod
#    'exhale'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
if os_version == 'Linux':
    master_doc = 'index'
else:
    master_doc = 'index_m'


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# MCamp copied theme options from EI for AMR, needs updates 18May22

html_theme_options = {
    'repository_url': 'https://github.com/intel-innersource/documentation.robotics.mobile',
    'path_to_docs': 'get_started_guide',
    'use_edit_page_button': True,
    'repository_branch': 'main',
    'search_bar_text': 'Search the doc...',
}



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinx-infodevdoc'


# -- Options for LaTeX output ------------------------------------------------

#latex_engine = 'xelatex'
#PDF_TITLE = 'Information Development Template'
#
#with open(PREAMBLE_FILE, 'r', encoding='utf-8') as f:
#    PREAMBLE = f.read()
#
#with open(TITLE_PAGE_FILE, 'r', encoding='utf-8') as f:
#    TITLE_PAGE = f.read().replace('<PDF_TITLE>', PDF_TITLE)
#
#
#latex_elements = {
#    # The paper size ('letterpaper' or 'a4paper').
#    #
#    'extraclassoptions': 'openany,oneside',
#    'babel' : '\\usepackage[english]{babel}',
#    'papersize': 'a4paper',
#    'releasename':" ",
#    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
#    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
#    'fncychap':  '',
#    #'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
#
#    'figure_align':'htbp',
#    # The font size ('10pt', '11pt' or '12pt').
#    #
#    'pointsize': '12pt',
#
#    # Additional stuff for the LaTeX preamble.
#    #
#    'preamble': PREAMBLE,
#
#    'maketitle': TITLE_PAGE,
#    # Latex figure (float) alignment
#    #
#    # 'figure_align': 'htbp',
#    'sphinxsetup': \
#        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
#        verbatimwithframe=true, \
#        TitleColor={rgb}{0,0.686,0.941}, \
#        HeaderFamily=\\rmfamily\\bfseries, \
#        InnerLinkColor={rgb}{0,0.686,0.941}, \
#        OuterLinkColor={rgb}{0,0.686,0.941}',
#
#    'tableofcontents':' '
#}
#
#latex_logo = '_latex/intel_logo.png'
## Grouping the document tree into LaTeX files. List of tuples
## (source start file, target name, title,
##  author, documentclass [howto, manual, or own class]).
#latex_documents = [
#    (master_doc, 'sphinx-infodev.tex', u'sphinx-infodev Documentation',
#     u'Intel', 'manual'),
#]

#breathe_projects = {                                       #todd-mod
#    project: "../doxygen/xml"
#}
#breathe_default_project = project

# Setup the exhale extension
#exhale_args = {                                            #todd-mod
#    # These arguments are required
#    "containmentFolder":     "./api",
#    "rootFileName":          "library_root.rst",
#    "rootFileTitle":         "Library API",
#    "doxygenStripFromPath":  "..",
#    "fullApiSubSectionTitle": 'Full API'
#}


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'sphinx-infodev', u'sphinx-infodev Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'sphinx-infodev', u'sphinx-infodev Documentation',
     author, 'sphinx-infodev', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- IDZ DITAXML config --------------------------------------------

# Put ditaxml output in a flat directory
ditaxml_make_flat=True

# Generate ditaxml file names from page titles instead of RST file names
# ditaxml_flat_map_to_title=True

# Generate ditaxml filenames from RST filenames only for page titles longer than 50 characters
# ditaxml_shorten_alias = True

# -- Metadata for IDZ DITAXML --------------------------------------------

ditaxml_topic_meta={}
ditaxml_topic_meta["audience"]="guid:etm-aa2a8ffb0e5b41fe85bf2f5d50a71cf2" #Software Developer
ditaxml_topic_meta["content type"]="Get Started Guide"
ditaxml_topic_meta["description"]="Prerequisites and installation instructions"
ditaxml_topic_meta["document title"]="Edge Insights for Fleet"
ditaxml_topic_meta["download url"]=""
ditaxml_topic_meta["IDZ custom tags"]="guid:etm-086ec8c4b4074875b84ba0e35d214cf5" #product documentation
ditaxml_topic_meta["keywords"]="None"
ditaxml_topic_meta["language"]="en"
ditaxml_topic_meta["location"]="us"
ditaxml_topic_meta["menu"]="/content/data/globalelements/US/en/sub-navigation/idz/developer-sub-navigation-breadcrumb"
ditaxml_topic_meta["menu parent page"]="/content/www/us/en/developer/topic-technology/edge-5g/edge-solutions/fleet-recipes"
ditaxml_topic_meta["operating system"]=""
ditaxml_topic_meta["programming language"]=""
ditaxml_topic_meta["software"]=""
ditaxml_topic_meta["primaryOwner"]="Camp, Mary (mary.camp@intel.com)"
ditaxml_topic_meta["programidentifier"]="idz"
ditaxml_topic_meta["published date"]="05/18/2022"
ditaxml_topic_meta["resourcetypeTag"]="guid:etm-c326ac0dddbc45cbb916bec3c0e56d03" #Get Started
ditaxml_topic_meta["secondary contenttype"]=""
ditaxml_topic_meta["security classification"]="Public Content"
ditaxml_topic_meta["shortDescription"]="Get Started with Edge Insights for Fleet"
ditaxml_topic_meta["shortTitle"]="Edge Insights for Fleet Get Started Guide"
ditaxml_topic_meta["noindexfollowarchive"]="false"
ditaxml_prod_info={}
ditaxml_prod_info["prodname"]="Edge Insights for Fleet"
ditaxml_prod_info["version"]="2022.2"
ditaxml_data_about={}
ditaxml_data_about["intelswd_aliasprefix"]={"datatype":"webAttr","value":"edge-insights-fleet-doc"}
