---
jupytext:
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
from canvasapi import Canvas
```

```{code-cell} ipython3
API_URL = "https://canvas.ubc.ca/"
API_KEY = "11224~mWKHmcIXWnookfU8kLo0xEV0iRuNFfDGvTWHJnRTuLWVkAK9tC7LA4NngKW2kEQU"

canvas = Canvas(API_URL, API_KEY)
```

```{code-cell} ipython3
ahl = canvas.get_course(51824)
```

```{code-cell} ipython3
ahl.name
```

```{code-cell} ipython3
ahl.upload("chain.h")
```

```{code-cell} ipython3
ahl.get_folders
```

```{code-cell} ipython3

```
