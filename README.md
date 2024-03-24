# AirBnB Clone - Command Interpreter

## Description

This project is part of the larger AirBnB clone project, focusing on developing a command-line interpreter to manage AirBnB objects. The command interpreter allows users to create, retrieve, update, and delete objects related to AirBnB, such as users, states, cities, and places.

## Command Interpreter

The command interpreter provides a shell-like interface to interact with the AirBnB objects. It supports various commands to perform CRUD (Create, Read, Update, Delete) operations on the objects. Below are the details on how to start and use the command interpreter:

### How to Start

To start the command interpreter, execute the `console.py` script:

```
$ ./console.py
```

### How to Use

Once the command interpreter is running, you can enter various commands to manage AirBnB objects. The prompt `(hbnb)` indicates that the interpreter is ready to accept commands. Type `help` to see the list of available commands and their usage.

### Examples

Here are some examples of commands you can use within the command interpreter:

1. Creating a new user:

```
(hbnb) create User
```

2. Showing all available objects:

```
(hbnb) all
```

3. Updating an object attribute:

```
(hbnb) update User 1234-1234-1234 email "example@example.com"
```

## Project Details

- **Project Name:** AirBnB clone - The console
- **Start Date:** Mar 18, 2024 6:00 AM
- **End Date:** Mar 25, 2024 6:00 AM
- **Weight:** 5
- **Language:** Python
- **Concepts:** OOP

## Background Context

The command interpreter is the first step in building the AirBnB clone project. It helps in managing AirBnB objects efficiently by providing a shell-like interface.

## Resources

- [cmd module](https://docs.python.org/3/library/cmd.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives

- Creating a Python package
- Implementing a command interpreter in Python using the cmd module
- Unit testing in a large project
- Serialization and deserialization of classes
- Handling JSON files
- Managing datetime
- Understanding UUIDs
- Utilizing *args and **kwargs in functions

---

**Bugs - Disclaimer:** Not all solutions meet the stated requirements.
