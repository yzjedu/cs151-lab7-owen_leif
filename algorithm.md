# ALGORITHM DOC

* Purpose: Calculating the size of the room and adding it to the house
* Name: "room_sizing"
* Parameters: none
* Return: Most recent size of house
* Algorithm:
1. Global import "house size"
2. Assess the counter of the current room (1st, 3rd, etc.)
3. While the input length of the room is not a digit:
   1. Request the length of the room from the user
   2. If the input is not a digit, print an error message
4. While the input width of the room is not a digit:
   1. Request the width of the room from the user
   2. If the input is not a digit, print an error message
4. Calculate the area of the room (L x W)
5. Assign the output of this calculation to "room size"
6. Add "room size" to "house size"

* Purpose: Calculating the various possibilities for the cost of the house
* Name: "cost_calculation"
* Parameters: none
* Return: Various possible prices for the room
* Algorithm:
1. Global import "passthru"
2. Global import "house size"
2. While "passthru" is False:
   1. Request the cost per squared unit of their design
   2. If the input is not a digit:
      1. print an error message
      2. break from code
   3. Calculate the cost of redoing the floor given the design cost (house size * design cost)
   4. while y/n input is not equal to y or n:
      1. Request a y/n input from user whether or not they would like to calculate for a different design
      2. Convert the input to lowercase
      3. if the input is equal to y, break from code
      4. otherwise, if the input is equal to n, set passthru to True
      5. otherwise, print an error message

* Purpose: Executing the regular code
* Name: "main"
* Parameters: none
* Return: Various possible prices for the room
* Algorithm:
1. Set variable "house size" equal to zero
2. Set variable "room counter" equal to 1
3. Set boolean "passthru" to False
4. While the counter of the current room is less than or equal to 5:
    1. Run function "room_sizing"
   2. Add 1 to "room counter"
5. Run function "cost_calculation"
