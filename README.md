# COMMAND-LINE-PATTERN-MATCHING-PROGRAM
It is a Project which deals with making of a customised "UBUNTU TERMINAL COMMAND", changing the "PATH VARIABLE" by making changes to .bashrc, involves the use of ReGex (re module of Python) and os related modules of python

## RUN the Following Commands And You Are Ready For New Customized Command On Ubuntu:-

`python3 installing.py`
`gedit ~/.bashrc`

PASTE THE FOLLOWING LINE AT THE END OF THE FILE(.bashrc) In a new line.
`export PATH=~/Pattern_Matching:$PATH`

# Commands Are :-
pamatch
work

*****************************************************************************************************************************

# Guide for pattern matching

*****************************************************************************************************************************
## Metacharacters:

### Character                                     Description                                     Example

    []                                    A set of characters                                 "[a-m]"

    \                                 Signals a special sequence                               "\d"
                             (can also be used to escape special characters)

   .                                          Any character                                   "he..o"
                                      (except newline character)    

   |                                           Either or                                    "falls|stays" 


*****************************************************************************************************************************
## Special Sequences:

#### A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

### Character                                     Description                                 Example

\b                                Returns a match where the specified 
                                  characters are at the beginning or at the       	   "\bain
                                               end of a word                               "ain\b"

\d                                  Returns a match where the string 
                                      contains digits (numbers from 0-9)	            "\d"

\D                                Returns a match where the string 
                                          DOES NOT contain digits                           "\D"

\s                                Returns a match where the string
                                    contains a white space character                        "\s"

\S                                Returns a match where the string DOES
                                   NOT contain a white space character 		            "\S"


*****************************************************************************************************************************
## Sets:

#### A set is a set of characters inside a pair of square brackets [] with a special meaning:

### Set                                                  Description

[arn]               Returns a match where one of the specified characters (a, r, or n) are present

[a-n]              Returns a match for any lower case character, alphabetically between a and n

[^arn]            Returns a match for any character EXCEPT a, r, and n

[0123]           Returns a match where any of the specified digits (0, 1, 2, or 3) are present

[0-9]              Returns a match for any digit between 0 and 9

[0-5][0-9]      Returns a match for any two-digit numbers from 00 and 59 

[a-zA-Z]        Returns a match for any character alphabetically between a and z, lower case OR upper case
*****************************************************************************************************************************
## Contributers

- Archit Sangal
- Raghava S N

## NOTE:

Codes are in different files

# All pull requests are welcomed and appreciated.....
