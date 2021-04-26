"""
This script goes through all the cells in a notebook
and sets the ctype metadata to 'question' and adds
a question number.  Then it makes a second pass through 
each cell and adds a new cell with the same question number
and the metadata answer, with the text 'qxx answer here'

To run:

python write_meta.py in_notebook.md out_notebook.md

"""
import jupytext as jp
from jupytext.cli import jupytext
from pathlib import Path
from nbformat.v4.nbbase import new_code_cell, new_markdown_cell
import click


@click.command()
@click.argument("jupyin", type=str, nargs=1)
@click.argument("jupyout", type=str, nargs=1)
def main(jupyin,jupyout):
    in_file = Path(jupyin).resolve()
    out_file = Path(jupyout).resolve()
    print(in_file,out_file)
<<<<<<< HEAD
<<<<<<< HEAD
    nb = jp.read(in_file)
=======
    nb = jp.readf(in_file)
>>>>>>> jupytext
=======
    nb = jp.read(in_file)
>>>>>>> update
    print(f"{(len(nb),type(nb))=}")
    print(f"keys {list(nb.keys())}")
    for item in ['nbformat', 'nbformat_minor', 'metadata']:
        print(f"{item}:{nb[item]=}")
    for count,the_cell in enumerate(nb['cells']):
        the_cell['metadata']['ctype']='question'
        the_cell['metadata']['quesnum']=count
    new_cells = []
    for a_cell in nb['cells']:
        new_cells.append(a_cell)
        num = a_cell['metadata']['quesnum']
        source = f"q{num} answer here"
        answer = new_markdown_cell(source=source)
        answer['metadata']['quesnum']=a_cell['metadata']['quesnum']
        answer['metadata']['ctype']='answer'
        new_cells.append(answer)
    nb['cells'] = new_cells
    #
    # write two versions of the notebook -- md and ipynb
    #
<<<<<<< HEAD
<<<<<<< HEAD
    jp.write(nb,out_file)
    out_file = out_file.with_suffix('.ipynb')
    jp.write(nb,out_file)
=======
    jp.writef(nb,out_file)
    out_file = out_file.with_suffix('.ipynb')
    jp.writef(nb,out_file)
>>>>>>> jupytext
=======
    jp.write(nb,out_file)
    out_file = out_file.with_suffix('.ipynb')
    jp.write(nb,out_file)
>>>>>>> update

if __name__ == "__main__":
    main()
