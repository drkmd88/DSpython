# Test Example

This repo shows a easy example about Python unit test. It mainly helps understand:
  - The structure of a project
  - What command to use at each step
  - Basic design and syntax to follow at feature functions and testing functions

## Structure
Notice that in each sub-directory, __init__.py is required, indicating it's a package. Refer to the following:

MyProject
 	src
		__init__.py
		process.py
	test
		__init__.py
		test_process.py

## How to run test
Under MyProject, run the following:
```python -m unittest test/test_process.py```



