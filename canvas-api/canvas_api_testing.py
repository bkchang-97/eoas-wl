# ---
# jupyter:
#   jupytext:
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.10.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from canvasapi import Canvas

# %%
API_URL = "https://canvas.ubc.ca/"
API_KEY = "11224~mWKHmcIXWnookfU8kLo0xEV0iRuNFfDGvTWHJnRTuLWVkAK9tC7LA4NngKW2kEQU"

canvas = Canvas(API_URL, API_KEY)

# %%
ahl = canvas.get_course(51824)

# %%
ahl.name

# %%
ahl.upload("chain.h")

# %%
ahl.get_folders

# %%
