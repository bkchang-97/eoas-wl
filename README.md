# eoas-wl

This repository contains information about all the various tools and scripts as well as notes documenting their usage.

1. The first item to look through will be `md2canvas` which is a Python script that allows a Canvas quiz designed in a Markdown file to be exported onto Canvas bypassing the need for the instructor to manually set up the questions on Canvas itself. In it you will find some additional notes as well but mainly focus on the `examples` folder which contains sample quizzes that demonstrate how certain types of questions are formatted and how to format an actual Canvas quiz itself. To get started with `md2canvas`, there is a file located in the directory called `How to md2canvas.ipynb` which contains step by step instructions on how to set up a Canvas token and then creating a Canvas Quiz.

2. `e340quizzes` is an application of `md2canvas` in practice. Within the `scripts` directory in `e340quizzes` we have written multiple scripts to be used in multiple scenarios. For example, `image_extract.py` is a script that will extract the figures in a Powerpoint file for later use in creating your Canvas Quiz in Markdown. Or `write_clickers.py` will take a Powerpoint file and filter for only the slides with Clicker questions and formats them in a markdown file that matches the format for a Canvas Quiz. There are already some resources from EOSC 340 that have been processed via these scripts and md2canvas into Canvas quizzes, Days 1 - 4.

3. Finally as many of these scripts and functionality rely and are dependent on Canvas API, the `canvas-api` directory contains some well documented notes and examples on how CanvasAPI works along with some custom functions that have been written to create some useful functionality. The `CanvasAPIGettingStarted.ipynb` file is a Jupyter notebook that walks you through setting up the CanvasAPI as well as some introductory uses of the API. But the `canvas_api_testing.ipynb` notebook file has some custom functions we have written that takes advantage of CanvasAPI in order to achieve some useful functionality (i.e. a function that returns a dictionary of modules with the module items as their values)
