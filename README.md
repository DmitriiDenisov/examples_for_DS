# Exaples for DS

This repository provides a few examples about some useful packages and methods

#### `example_proxy_python.py` 
Illustrates some usages of proxy http/https/socks5 for requests library

### `Examples_Stacking.ipynb`
Illustrates examples of StackingClassifier from mlxtend library

Source:
http://rasbt.github.io/mlxtend/user_guide/classifier/StackingClassifier/

### `exp_gridsearch.ipynb`
Illustrates small example how to use GridSearchCV with params

### `example_logging.py`
Illustrates small example how to make a simple logger using ligging library

Source:
https://python-scripts.com/logging-python

### `example_batch_generator.py`
Illustrates example of function which provides a generator for batches of size n

### `ex_generator_and_augm_keras.py`
Illustrates example of how you can use a generator as a wrapper over another generator.
In this case augmentation generator was used as a wrapper over read files generator

### `example_left_join_perfomance.py`
Illustrates performance of left join. Change N to see time performance of pd.merge function

### `get_size_variables.py`
Allows to get information about size of all variables

### `Decorators`
This folder contains several examples how to use decorators

Something more about decorators:
https://realpython.com/primer-on-python-decorators/

### `Example add to path`
Add these row to file ```~/.bash_profile```:
```export PATH=/usr/local/Cellar/rabbitmq/<version>/sbin:$PATH```



### `Create alias`
In folder: (usually in folder with binaries: /usr/bin/), ```sudo ln -s {path_to_executable} {name_of_alias}```
for example ```sudo ln -s /home/dmitryhse/.local/bin/pip3.7 pip3.7```


### `Virtualenv`
1. ```pip3 install virtualenv```
2. In your project folder: ```virtualenv -p {path_to_python} {name_of_virtualenv}``` for example:  ```virtualenv -p /usr/bin/python3.7 .venv```


### `Virtual environment for Jupyter Notebooks`
Create:
https://anbasile.github.io/programming/2017/06/25/jupyter-venv/

Remove: ```jupyter kernelspec uninstall unwanted-kernel```

Rename Kernel: https://stackoverflow.com/questions/45085233/jupyter-kernel-is-there-a-way-to-rename-them

`jupyter kernelspec list` - list of available kernels
