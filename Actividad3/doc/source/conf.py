# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os      #realizamos las importaciones necesarias
sys.path.append(os.path.abspath('../../'))      #configuramos la ruta a los archivos a apartir de los cuales crearemos la documentacion
extensions = ['sphinx.ext.autodoc','sphinx.ext.napoleon']       #añadimos las extensiones que utilizaremos


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tkinter'
copyright = '2022, Juan Carlos Tibocha Espinosa'
author = 'Juan Carlos Tibocha Espinosa'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'spanish'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'     #cambiamos el tema visual
html_static_path = ['_static']
