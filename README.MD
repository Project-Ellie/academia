# Exploring academic subjects

You'll need python 3.6 available on your machine. I guess any
other version will do but I can only support 3.6.

## Setup
My recommended setup is as follows

1) Install virtualenv by following these instructions
[Instructions](https://virtualenv.pypa.io/en/stable/installation/)

2) Create a virtual environment in your project directory
```shell
    $ virtualenv --python=python3 venv
    $ . ./venv/bin/activate # or use 'source'
```

3) Install dependencies and start jupyter notebook
```shell
    $ pip install tensorflow matplotlib jupyter
    $ virtualenv --python=python3 venv
```

4) Choose the notebook of your choice and have fun
```shell
    $ cd ./src
    $ jupyter notebook
```
