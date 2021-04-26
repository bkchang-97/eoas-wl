---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
import markdown
from bs4 import BeautifulSoup
html = markdown.markdown(open("Day02_Systems_2019t2_allslides.md").read())
text = ("".join(BeautifulSoup(html).findAll(text=True)))
```

```{code-cell} ipython3
type(text)
```

```{code-cell} ipython3
slides = text.split("Slide ")
```

```{code-cell} ipython3
slides[1:]
```

```{code-cell} ipython3
clickers = [x for x in slides if "Clicker" in x]
```

```{code-cell} ipython3
clickers
```

```{code-cell} ipython3

```
