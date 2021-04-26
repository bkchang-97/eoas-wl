{
 "cells": [
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "\\pagestyle{headers}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "toc": true
   },
   "source": [
    "<h1>Table of Contents<span class=\"tocSkip\"></span></h1>\n",
    "<div class=\"toc\"><ul class=\"toc-item\"><li><span><a href=\"#Worksheet---EOSC-340---Day-3\" data-toc-modified-id=\"Worksheet---EOSC-340---Day-3-1\"><span class=\"toc-item-num\">1&nbsp;&nbsp;</span>Worksheet - EOSC 340 - Day 3</a></span><ul class=\"toc-item\"><li><span><a href=\"#Prove:-Good-absorbers-are-good-emitters\" data-toc-modified-id=\"Prove:-Good-absorbers-are-good-emitters-1.1\"><span class=\"toc-item-num\">1.1&nbsp;&nbsp;</span>Prove: Good absorbers are good emitters</a></span></li><li><span><a href=\"#The-proof\" data-toc-modified-id=\"The-proof-1.2\"><span class=\"toc-item-num\">1.2&nbsp;&nbsp;</span>The proof</a></span></li></ul></li></ul></div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Worksheet - EOSC 340 - Day 3\n",
    "\n",
    "## Prove: Good absorbers are good emitters\n",
    "\n",
    "The two walls shown below are initially at the same temperature, though they have different emissivities as shown. Assume the transmissivity is 0 for both walls. The space between the walls is a vacuum. Recall that $\\sigma$=5.67x10<sup>-8</sup>$W/m^2$/K<sup>4</sup>. Note that the right all absorbs everything that hits it (it’s a blackbody), while the left wall partially absorbs some radiation and reflects the rest.\n",
    "\n",
    "![fig1](media/two_walls.png)\n",
    "<img src=\"media/two_walls.png\" width=\"60%\">\n",
    "\n",
    "On average, is there a net heat transfer between the two walls? If so, which way does it go? Provide reasoning, but **do not** do any math at this point.\n",
    "\n",
    "**The 2nd law of thermodynamics says that the temperature can’t change without some process doing work, so the net transfer has to be zero at both walls.**\n",
    "\n",
    "Do either or both of the walls change their temperature with time? If so, which becomes warmer with time, and which cools down with time?  Again, don’t do any math at this point.\n",
    "\n",
    "**No temperature change for either wall.**\n",
    "\n",
    "What is the radiative flux (in$W/m^2$) emitted by the  \n",
    "a) the right wall, and  \n",
    "b) the left wall?\n",
    "\n",
    "**Right wall: $I_{right} = \\sigma T^4 =348.5 W/m^2$**\n",
    "\n",
    "**Left wall: $I_{left}=\\epsilon \\sigma T^4 = 0.6x348.5=209\\ W/m^2$**\n",
    "\n",
    "How much flux is absorbed at the left wall, assuming Kirchoff’s law is\n",
    "true?\n",
    "\n",
    "If $abs=\\epsilon$ then $abs I_{right} = \\epsilon I_{right} = 209 W/m^2$\n",
    "\n",
    "## The proof\n",
    "\n",
    "**Kirchhoff’s Law** states that *abs* = $\\epsilon$. Show algebraically that this must be true at the left wall. Do not use numeric values\\! Assume that the left wall can’t change temperature, so that all the arrows at the wall have to cancel out. Remember that the wall is absorbing and reflecting, but not transmitting.\n",
    "\n",
    "Since the 2nd law says temperature can’t change, that means the fluxes in and out have to balance. If we use a minus sign for outbound fluxes and plus sign for inbound fluxes, then the balance at the left wall is:\n",
    "\n",
    "\\begin{equation}\n",
    "I_{emit_{R}} – I_{emit_{L}} – I_{refl_{L}}=0\n",
    "\\end{equation}\n",
    "\n",
    "Also, we can use conservation of energy to write the reflectivity in terms of the absorptivity,\n",
    "since:\n",
    "\n",
    "since the wall is absorbing and reflecting, but not transmitting, we have:\n",
    "\n",
    "\\begin{equation}\n",
    "I_{refl_{L}} = (1 – abs)I_{emit_{R}}\n",
    "\\end{equation}\n",
    "\n",
    "Filling in the rest of the values we can rewrite the equation (1) and divide out $\\sigma T^4$:\n",
    "\n",
    "\\begin{align}\n",
    "0 = & I_{emit_{R}}-\\epsilon \\sigma T^{4}-(1-{abs}) I_{emit_{R}}\\\\\n",
    "0=&\\sigma T^{4}-\\epsilon \\sigma T^{4}-(1-abs) \\sigma T^{4}\\\\\n",
    "0=& 1-\\epsilon-(1-abs)\\\\\n",
    " \\epsilon =& abs\\\\\n",
    "\\end{align}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Where we’ve used the fact that both walls have to be at temperature T and the right wall is black, so that $I_{emit_{R}} = \\sigma T^4$.  Making that subsitution we can make this tranformation:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "jupytext": {
   "cell_metadata_filter": "-all",
   "encoding": "# -*- coding: utf-8 -*-",
   "formats": "ipynb,py:percent",
   "main_language": "python",
   "notebook_metadata_filter": "all,-language_info,-toc,-latex_envs"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "latex_metadata": {
   "chead": "Day 3 worksheet solution",
   "lhead": "E340 2019t2"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": true,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
