# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import re
import datetime

# The theme to use for HTML and HTML Help pages
import sphinx_bootstrap_theme

now = datetime.datetime.now()
sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------

project = 'honeybee-radiance-command'
copyright = '{}, Ladybug Tools'.format(str(now.year))
author = 'Ladybug Tools'

# The full version, including alpha/beta/rc tags
release = ''

# for example take major/minor
version = ''

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinxcontrib.fulltoc',
    'sphinx.ext.napoleon',
    'sphinx_click.ext'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# html_theme = 'alabaster'
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-inverse",
    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",
    'navbar_pagenav': True,
    'source_link_position': "nav",
    'bootswatch_theme': "united",
    'bootstrap_version': "3",
}

# on_rtd is whether we are on readthedocs.org
# on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# if not on_rtd:  # only import and set the theme if we're building docs locally
#    import sphinx_rtd_theme
#    html_theme = 'sphinx_rtd_theme'
#    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    '**': ['localtoc.html']
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'lbtoolsdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'honeybee-radiance-command.tex', 'honeybee-radiance-command Documentation',
     'Ladybug Tools', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'honeybee-radiance-command', 'honeybee-radiance-command Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'honeybee-radiance-command', 'honeybee-radiance-command Documentation',
     author, 'honeybee-radiance-command', 'One line description of project.',
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

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for autodoc extension --------------------------------------------
autodoc_default_options = {
    'inherited-members': True,
}

autodoc_member_order = 'groupwise'

# -- CLI documentation  -------------------------------------------------------
"""Improves the CLI documentation section.

In order to have separate html pages for each module inside library\\cli
additional documentation reST files(.rst) need to be generated in docs\\cli folder.

Note:
    This process assumes that each CLI module represent a group of subcommands.
"""
# Activate this CLI documentation process.
custom_cli_docs = True
# Override existing reSt files found in docs//cli folder.
cli_overwrite = False

# Repository/library hash table.
# If respository not found in table, the module name will be extracted from the
# modules.rst file in the project folder.
# Format: {repository_name: library_name}
ht_repo_lib = {}

# Library/command hash table.
# Created to address CLI tool names that differ from their library name beyond
# the underscore(_) to dash(-) difference.
# Format: {library_name: tool_name}
ht_lib_tool = {}


def create_cli_files():
    """Generate additional files required by sphinx to build well structured
     CLI documentation pages.

    The process consists in generating reST files with sphinx-click directives
    for each click group detected in the library's cli folder and updating
    the index.rst file to include a list of the click groups found.

    Returns:
        1 on success.
        0 if no update was generated.
        -1 on error.
    """

    # Get CLI data from library
    proj_folder = os.path.dirname(__file__)
    result = get_cli_data(proj_folder)
    if not result:  # return if no CLI module found.
        return 0

    ht_cli, lib_name, tool_name = result

    # Prepare docs folder and reST files to create.
    doc_folder = os.path.join(proj_folder, 'cli')
    if not os.path.isdir(doc_folder):
        os.mkdir(doc_folder)

    # Create new groups only list by excluding CLI groups that have a reST file.
    # inside docs/cli
    def get_missing_groups():
        ht_new_cli_groups = {}
        for mod_name in ht_cli.keys():
            if mod_name + ".rst" not in os.listdir(doc_folder):
                ht_new_cli_groups[mod_name] = ht_cli[mod_name]
        return ht_new_cli_groups

    # Prepare all/missing group list.
    if not cli_overwrite:
        ht_missing_cli = get_missing_groups()
        if not ht_missing_cli:
            print("[CLI]: No new CLI files created.")
            return 0
    else:
        ht_missing_cli = ht_cli

    # Create CLI reST files for each module(command group) found.
    if not write_cli_files(ht_missing_cli, lib_name, tool_name, doc_folder):
        return -1

    # Update/Create CLI index file with command group section included.
    if not update_cli_index(os.path.join(doc_folder, 'index.rst'),
                            list(ht_cli.keys())):
        return -1

    # Update package index file to include CLI docs section
    update_doc_index(proj_folder, lib_name)

    return 1


def get_cli_data(project_folder):
    """Retrieve CLI data found inside a specified respository.

    Args:
        project_folder: the documentation path that contains the files to
        extract CLI data from.

    Returns:
        A tuple with three elements.

        -   ht_mod_group:
            A dictionary with module file names and the corresponding
            group names found.

        -   lib_name: The name of the library found in the repository.

        -   tool_name: The name of the command line tool that is used for this
            library.
    """
    print("[CLI data]: Retrieveing CLI data from {}".format(project_folder))

    # Check in hash table for a library name based on repository name.
    repo_path = os.path.abspath(os.path.join(project_folder, os.pardir))
    repo_name = os.path.split(repo_path)[1]

    # Look up the library name in hashtable.
    if repo_name in ht_repo_lib:
        lib_name = ht_repo_lib[repo_name]
    # Otherwise exract library name from modules.rst file heading and replace
    # dash(-) to underscore(_).
    else:
        modules_file = os.path.join(os.path.join(project_folder, 'modules.rst'))
        with open(modules_file, 'r') as mod_file:
            lines = mod_file.readlines()
        lib_name = lines[0][0:-1]
        lib_name.replace("-", "_")

    # Check in hash table for a command line tool name that is different
    # from its library name beyond the underscore(_) to dash(-) difference.
    tool_name = ht_lib_tool[
        lib_name] if lib_name in ht_lib_tool else lib_name.replace("_", "-")

    lib_path = os.path.abspath(os.path.join(repo_path, lib_name))
    if not os.path.isdir(lib_path):
        print("[CLI data]: Cannot find library path")
        return None

    cli_path = os.path.join(lib_path, 'cli')
    if not os.path.isdir(cli_path):
        print("[CLI data]: No CLI library found")
        return None

    # Get CLI module names and their corresponding group names as a dictionary.
    ht_mod_group = get_cli_groups(cli_path)

    if ht_mod_group == {}:
        print("[CLI data]: No CLI modules detected in /cli folder.")
        return None

    # Return library data
    return ht_mod_group, lib_name, tool_name


def get_cli_groups(cli_path):
    """Retrieve CLI group data found inside a specified cli path.

    Args:
        cli_path: the path that contains the CLI modules to extract group
        data from.

    Returns:
        A dictionary with module file names and the corresponding
        group names found.
    """
    module_names = [os.path.splitext(file)[0] for file in os.listdir(cli_path)
                    if os.path.splitext(file)[1] == ".py"]

    # Look for group function names inside their CLI module. Assume (1) group
    # and (1) function per module. Assumme possible multiple groups and
    # functions in '__init.py'.

    init_text = ""
    ht_groups = {}
    for name in module_names:
        with open(os.path.join(cli_path, name + ".py"), 'r') as cli_file:
            text = cli_file.read()
        # Use regex pattern to get function name after click group decorator
        fnd = re.findall(r'^@click\.group\(.*\n(@click.*\n){0,2}def\s(\w*)\s*\(\):\n',
                         text, flags=re.MULTILINE)
        # Add multiple commands found in each group inside '__init__.py'
        if name == "__init__":
            init_text = text
            for result in fnd:
                options, cli_comm = result
                comm_exp = r'^@' + cli_comm + r'.command\(\'([\w-]+)'
                im = re.findall(comm_exp, text, flags=re.MULTILINE)
                if im or 'version_option' in options:
                    # add sub-group key with list of commands to the
                    # 'main' group dict. key
                    if 'main' not in ht_groups:
                        ht_groups['main'] = {}
                    ht_groups['main'][cli_comm] = list(im)
        else:
            # Store module function name and initial command name in hash table.
            if fnd:
                ht_groups[name] = [fnd[0][1], fnd[0][1]]

    # Check if any group/function has a new command name specified inisde
    # "add_command" function.
    if init_text:
        named_groups = re.findall(
            r'add_command\( *([\w-]+) *, *(name=)? *\'([\w-]+)\' *\)',
            init_text, flags=re.MULTILINE)
        for group in named_groups:
            cli_func, tr, cli_comm = group
            for file in ht_groups:
                # 'main' groups are excluded, assumes not used in CLI.
                if file != 'main' and ht_groups[file][0] == cli_func:
                    ht_groups[file][1] = cli_comm

    return ht_groups


def write_cli_files(ht_cli_data, lib_name, tool_name, doc_folder):
    """Writes a reST file with CLI directives for each click group provided.

    Args:
        ht_cli_data: A dictionary containing the names of the reSt CLI files
            that will be generated and their corresponding CLI group name.
        lib_name: The name of the library the click groups belong to. For
            example ``honeybee_energy``, ``dragonfly`` or ``honeybee_radiance``
            are possible library names.
        tool_name: The command line tool name for the specified library. For
            instance ``honeybee-energy`` is the CLI tool used for the
            honeybee_energy library.
        doc_folder: The path where the CLI documentation files will be saved.
    """

    # Creating missing CLI reST files.
    group_filenames = ht_cli_data.keys()
    print("[CLI files]: Creating ({}) CLI rst files: {}...".format(
        len(group_filenames), list(group_filenames)))

    # Write sphinx-click directive with options for each CLI group.
    for file in group_filenames:
        cli_content = ["{}\n".format(file),
                       "{}\n".format("=" * len(file))]
        if file != "main":
            # one command(with all its subcommands) per cli module.
            cli_content += ["\n",
                            ".. click:: {}.cli.{}:{}\n".format(
                                lib_name, file, ht_cli_data[file][0]),
                            "   :prog: {} {}\n".format(
                                    tool_name, ht_cli_data[file][1]),
                            "   :show-nested:\n"]
        else:
            # multiple commands in the 'main' group (explicitly named to
            # avoid commands from other modules to be included). Also specify
            # commands as root commands.
            for group in ht_cli_data[file].keys():
                cli_content += ["\n",
                                ".. click:: {}.cli.{}:{}\n".
                                format(lib_name, "__init__", group),
                                "   :prog: {}\n".format(tool_name),
                                "   :show-nested:\n",
                                "   :commands: " + " ,".
                                join(ht_cli_data[file][group]) + "\n"
                                ]

        # Create CLI group reST file.
        with open(os.path.join(doc_folder, file + ".rst"), 'w') as group_file:
            group_file.writelines(cli_content)

    return 1


def update_cli_index(index_path, group_filenames):
    """Create or update the index.rst file inside the docs\\cli folder to include
    links to the click groups found.

    Args:
        index_path: index.rst file path to be updated or created from scratch.
        group_filenames: Name of the click groups to include in the
            index \'Commands\' section.
    """
    # Include exisitng cli/index.rst data if present.
    cli_content = []
    if os.path.isfile(index_path):
        with open(index_path, 'r') as index_file:
            lines = index_file.readlines()
        cli_content = lines[:lines.index("Commands\n")
                            ] if "Commands\n" in lines else lines
        print("[CLI cli\\index]: Updating index.rst file...")
    else:
        # Otherwise create a "CLI" heading.
        cli_content = ["CLI\n", "===\n", "\n"]
        print("[CLI cli\\index]: Creating index.rst file...")

    # Add 'Commands' section with directive and options.
    cli_content += ["\n"
                    "Commands\n",
                    "--------\n",
                    ".. toctree::\n",
                    "   :maxdepth: 1\n",
                    "\n"
                    ]

    # Add sub-command groups to content.
    if "main" in group_filenames:
        group_filenames.remove('main')
        group_filenames.insert(0, 'main')
    for file in group_filenames:
        cli_content.append("   {}\n".format(file))

    # Append section to existing file or create new file.
    with open(index_path, 'w') as index_file:
        index_file.writelines(cli_content)

    return 1


def update_doc_index(proj_folder, lib_name):
    """Update the documenation index.rst file inside the \\docs folder to include
    a CLI Docs section if not present already.

    Args:
        proj_folder: The documentation file path where the package documentation
            index.rst file is located.
        lib_name: The name of the library the click groups belong to. For
            example ``honeybee_energy``, ``dragonfly`` or ``honeybee_radiance``
            are possible library names.
    Returns:
        1 on success.
        -1 on error.
    """
    index_fpath = os.path.join(proj_folder, "index.rst")
    if not os.path.isfile(index_fpath):
        print("[CLI doc\\index]: No index.rst file found.")
        return -1
    with open(index_fpath, 'r') as index_file:
        text = index_file.read()

    # Check if CLI Docs section already present
    if re.search(r'^ *cli\/\/index *\n|^CLI Docs *\n=+\n', text, flags=re.MULTILINE):
        return 1

    print("[CLI doc\\index]: Updating index.rst file...")
    # Add CLi Docs section
    cli_text = "\n" + \
               "CLI Docs\n" + \
               "========\n" + \
               "\n" + \
               "For command line interface documentation and API " + \
               "documentation see the pages below.\n" + \
               "\n" + \
               ".. toctree::\n" + \
               "   :maxdepth: 2\n" + \
               "\n" + \
               "   cli//index\n" + \
               "\n" + \
               "\n"

    # Find insert location, add text and save
    lib_exp = r'^' + lib_name + r' *\n=+\n|^\.\. toctree:: *\n'
    m = re.search(lib_exp, text, flags=re.MULTILINE)
    if m:
        text_updated = text[:m.start()-1] + cli_text + text[m.start():]
        with open(os.path.join(proj_folder, "index.rst"), 'w') as index_file:
            text = index_file.write(text_updated)
    else:
        print("[CLI doc\\index]: index.rst update not possible - content \
              format cannot be recognized.")
        return -1

    return 1


# Custom CLI docs function call.
if custom_cli_docs:
    create_cli_files()

# -----------------------------------------------------------------------------
