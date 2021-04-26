---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
<<<<<<< HEAD
<<<<<<< HEAD
    jupytext_version: 1.7.1
=======
    jupytext_version: 1.6.0
>>>>>>> jupytext
=======
    jupytext_version: 1.7.1
>>>>>>> update
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell}
:ctype: question
:quesnum: 0

import markdown
from bs4 import BeautifulSoup
html = markdown.markdown(open("Day02_Systems_2019t2_allslides.md").read())
text = ("".join(BeautifulSoup(html).findAll(text=True)))
```

+++ {"quesnum": 0, "ctype": "answer"}

q0 answer here

```{code-cell}
:ctype: question
:quesnum: 1

type(text)
```

+++ {"quesnum": 1, "ctype": "answer"}

q1 answer here

```{code-cell}
:ctype: question
:quesnum: 2

slides = text.split("Slide ")
```

+++ {"quesnum": 2, "ctype": "answer"}

q2 answer here

```{code-cell}
:ctype: question
:quesnum: 3

slides[1:]
```

+++ {"quesnum": 3, "ctype": "answer"}

q3 answer here

```{code-cell}
:ctype: question
:quesnum: 4

clickers = [x for x in slides if "Clicker" in x]
```

+++ {"quesnum": 4, "ctype": "answer"}

q4 answer here

```{code-cell}
:ctype: question
:quesnum: 5

clickers
```

+++ {"quesnum": 5, "ctype": "answer"}

q5 answer here

```{code-cell}
:ctype: question
:quesnum: 6


```

+++ {"quesnum": 6, "ctype": "answer"}

q6 answer here
