# TaskDispatcher
A tiny code to group students to assignments

Students are able to vote for 10 given tasks. This code takes the voting results and groups students according to their preferences into groups of 3 Students. Bachelor and master students are put into seperate groups. 

# Usage

` python TaskDispatcher.py pathToVotingFile`

# Data structure

Currently only csv-Files with the following structure are supported.

> Name, Type (Bachelor = 0, Master = 1), Voting for Task 1, ...., Voting for Task10
