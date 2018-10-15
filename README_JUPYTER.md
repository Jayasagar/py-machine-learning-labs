##### DON'T DO THIS
`!pip install numpy`

#### Using LaTeX for forumlas
* https://www.latex-project.org/help/documentation/amsldoc.pdf
When you write LaTeX in a Markdown cell, it will be rendered as a formula using MathJax.



##### Best artcile to refer to understand jupyter internals
Ref: [https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/](Ref: https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)

##### This is Best way ###########
##### Install a pip package in the current Jupyter kernel
`import sys
!{sys.executable} -m pip install numpy`

#### Below is always best practice 
`python -m pip install <package>`
because is more explicit about where the package will be installed

 By default, the first place Python looks for a module is an empty path, meaning the current working directory.
If the module is not found there, it goes down the list of locations until the module is found. 
You can find out which location has been used using the __path__ attribute of an imported module:

`import numpy as np
np.__path__`

###### ?, you can access the Docstring for quick reference on syntax.
`?str.replace()`

###### IPython Magic Commands

# This will list all magic commands
`%lsmagic`

### References
List of all Magic commands for Jupyrer
* https://ipython.readthedocs.io/en/stable/interactive/magics.html

Jupyter Shortcuts and Tips
* https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/