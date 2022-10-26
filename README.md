# TaskDispatcher
A tiny code to group students to assignments

Students are able to vote for given tasks. This code takes the voting results and groups students according to their preferences into groups of 3 Students. Students of different types (e.g. Bachelor, Master) are put into seperate groups. 

# Usage

`TaskDispatcher.py [-h] [--sortAscending] [--sortDescending] path`

positional arguments:
  path              Path to file containing the votings

options:
  -h, --help        show this help message and exit
  --sortAscending   If the lowest voting stands for the highest approval.
  --sortDescending  If the highest voting stands for the highest approval. This is the default.

# Data structure

Currently only csv-Files with the following structure are supported. The Type can be any String, e.g. BA, MA.

> Name, Type, Voting for Task 1, Voting for Task 2, ....
