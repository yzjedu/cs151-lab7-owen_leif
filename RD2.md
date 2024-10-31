# Reflection Document

* Drive Full Name  : Leif LaBianca
* Partner Full Name: Owen Sanchez
* Student ID: 1928607

In this lab, the objective was to build a program that would calculate the estimated cost of flooring given the dimensions and types of flooring given by a user.
The lab required us to separate the functions of the code into different explicitly defined functions.
I wrote out an algorithm first, as is expected. I then worked out test cases to map out how we anticipated the most typical interactions with the program to go.
With these steps completed, I set out to write the code itself. I ran into some issues in regards to the looping of the code several times, but solved this with "passthru" variables.
Despite this, I sorted out the code relatively quickly and without tremendous turmoil.
The test cases were fairly straightforward, and not too complex. I essentially mapped out a typical interaction between the user and machine, not using many extreme variables.
The main issue I encountered, as previously mentioned, was related to looping not working due to them being set to variables that constantly changed, leaving the program confused, softlocking the code.
To fix the issue, I defined a boolean variable "passthru" that defaulted to false to the while loop condition. While this variable was false, it would ocntinue to run
It would only become true in the case of a full cycle being completed, which usually just meant error checking being passed.
Other than that, I did not have any outstanding problems concerning the code that needed addressing.
The most important takeaway I had in this lab was primarily to be careful with how you orient your loops.
The minor kerfuffle I encountered with the while loops being set to operate on the condition of constantly changing variables used in the code emphasized this point to me.
Regardless, I found that I learned what I was supposed to, because I managed to write a functioning set of while loop based functions that calculated as they were expected.


