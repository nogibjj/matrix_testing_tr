# Mini-Project 4  Tianji Rao

[![CI](https://github.com/nogibjj/matrix_testing_tr/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/matrix_testing_tr/actions/workflows/ci.yml)

## Overview
This repo contains:

- .devcontainer 
- .github   
- .gitignore    
- Makefile  
- README.md 
- requirements.txt  
- main.py   
- test_main.py  
- some .sh files    


## Objective
The objective of this project is creat a action matrix for multiple python versions and os systems. Here we modified the `ci.yml` file and created two matrixs corresponding to python version and os. 

## Matrix
1. Python versions:    
`3.7`, `3.8`, `3.9`, `3.10`, `3.11`

2. OS:  
Latest `Windows` and latest `ubuntu`

## Test
Here we create a function `add_func` based on the `add` in mylib/calculator. In the test_main.py file, we use `test_add_func` which contains three examples for testing.

## Preparation
1. Open a new codespace 
2. Waiting for the codespace to be built with required packages installed   
3. Apply make actions


## Actions
1. Format: `make format`    

2. Lint: `make lint`    
![Screenshot 2023-09-22 at 9 52 58 PM](https://github.com/nogibjj/TianjiRao_Mini_Project_3/assets/104114843/957b6156-1a10-46e0-aa8b-e29a975c1334)

    Here we use ruff to lint all codes in .py files and mylib/.py files.


3. Test: `make test`    
![Screenshot 2023-09-22 at 9 53 35 PM](https://github.com/nogibjj/TianjiRao_Mini_Project_3/assets/104114843/e5a84fe7-65e1-40a8-9647-cdac356dea2e)


