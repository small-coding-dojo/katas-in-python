# Katas in Python

Description.

## Acknowledgements

Many thanks ❤️ go to

- [JetBrains](https://www.jetbrains.com/?from=PROJECT-NAME) who provide an [Open Source License](https://www.jetbrains.com/community/opensource/) for this project

## Developer Guide

### Prerequisites

It is recommended to use a python virtual environment. Create and activate it:

```shell
python3 -m venv venvsource venv/bin/activate
```

Install the required python packages:

```shell
pip install -r requirements.txt
```

Then install this package in development mode:

```shell
pip install --editable .
```

### Run the Application

```shell
python src/dall_e/count_bits.py
```

### Execute the Tests Once

```shell
python -m pytest
```

### Launch the Test Runner in the Interactive Watch Mode

```shell
ptw . --now --last-failed --new-first
```
