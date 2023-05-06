# Git Repository
https://github.com/O-App-Pesi/JT_T1A3

# Styling
Standard Python Styling.

# Features

## Japanese Shrine

This application will simulate what it's like to visit a Japanese Shinto Shrine. There are various activities that a person can partake in at a Japanese Shinto Shrine which are customary to visiting. They are able to purchase fortunes, known as omikuji, pray to the shrine's deities for wellbeing, and even write their wishes on special wooden blocks known as ema.The start of this application puts you at the entrance to the shrine, allowing you to choose which direction you go in. User input is taken and the user is directed to the next step through and if statement depending on what they typed.

## Fortune Pulling

This function of the application simulates an interaction with the fortune pulling system found at Japanese Shinto Shrines. Visitors pull a stick from a hexagonal box and are given a fortune based on the number they pulled. This function loops allowing the user to input the different options multiple times to achieve a random number. Each of the actions creates a random number between two set values and adds to or takes away from the total. Once the user is ready they can pass this total to the final fortune function.
The final fortune function initialises a series of lists, each with 10 numbers between 1 and 50. The function takes an argument, so the total from the previous function is parsed in. Depending on the number that is parsed, the user will recieve a fortune from a selection of six options. If the numbers is above 50 or below 1, there is a final option for that outcome.

## Wishing Blocks

This function of the application simulates how a user might interact with the wooden blocks, on which they can write wishes, at a Japanese Shinto Shrine. If the user accepts to write down a wish, they will presented with two options to interact with this feature and one option to leave. If they choose to "Wish", they will move to the next function. Inside the write on block function, they will be given the opportunity to write down their wish and the date which will be recorded inside a csv file. If the user tries to review before they have written a wish, the function will catch this as an exception and redirect the user to make another choice.
If they choose to "Review" they will move to another function. The review previous wishes function takes the data from the csv file and prints it to a table, using console and table from the rich package. 

## Prayer Box

The final primary function of the application simulates a mystical experience of wishing at a Japanese Shinto Shrine. It is common at Japanese Shrines to drop a donation into a box and in turn ring a bell that hangs above the box, doing this represents paying homage to the deities of the shrine. Since there is not much else to it than the physical act and providing a donation, the function simulates a mystical experience.
Upon choosing to continue with the prayer box function, a random integer is assigned to a variable. This variable is used to determine which sequence plays and in turn which number is given to the user. If the user chooses, they may then use that number that was randomly assigned to run the pull fortune function. This is another way they may achieve a different result to one they have previously recieved.

## Ancillaries

This application uses Prompt and Confirm from the Rich Package. Using Prompt and Confirm, the application will loop on user input until it is given a valid input. For Prompt, the input is already determined and all valid options are listed next to the input statement. For Confirm, the only inputs accepted are a "y" or an "n" which indicate whether the value is "True" or "False".

# Implementation Plan

