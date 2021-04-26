The write_meta.py script reads the input notebook, adds metadata items to every cell, then
adds a new cell to every question cell with the answer metadata and a short text string.
It then write out a markdown and ipynb version of the notebook.  To try it do:

python write_meta.py in_notebook.md out_notebook.md
