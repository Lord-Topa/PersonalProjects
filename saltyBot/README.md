# Salty-Scraper
*Project put on hold for forseable future to focus on school and other projects*

## Description:
This program is meant to go to [saltybet](https://www.saltybet.com), scrape data from the 
homepage and compendium, then display that data in one simple place for the user. 
I made this program because I was finding it annoying to try and find all of the data 
for the fighters before a match to make an informed bet, so I automated it.
	
## Requirments: 
* User has selenium on their system
* User has chrome webdriver on their system
* User has a saltybet illuminati account	

## Limitations:
Currently only works for 1v1 matches. I plan to add an option/way to make
it work with 2v2 and 2v1 matches but as of now that is on the back burner
while I make the program work well with 1v1

## Instructions
1) Run with python3
2) Enter username and password
3) Enter 1 when prompted and saltybet is showing fighter information
4) Enjoy

## Challenges:
*presented in a problem followed by solution format*

How do I get character data for the thousands of characters that saltybet
	  uses on their site?
	  
>Rather than decide to try and download all of the characters from the site
	   I did research and found that most salty bet characters (and a lot of mugen
	   characters in general) use a set of default stats, so my temporary solution
	   was to use these default values and then modify them based on data presented
	   on the homepage of saltybet and the information given in the compendium.
	

Program was having a hard time getting data from a dynamic page using
	   Requests and html dom manipulation.
	   
>Switched the program to using selenium, and just grabbing the dynamic 
 	   elements directly from the html presented in the browser.

How do I get information from the compendium and how do I get to the 
	   page for the specific character I am looking for?
	   
>Firstly I created a custom url by combinging the search URL + the 
	   character name. Then I navigate to the part of the dom holding the 
	   compendium information, if there is none i leave, if there is some
	   I take in all of it as a string (it wasn't seperated in dom so I must
	   seperate myself) and then split the String. After splitting the strig
	   by line I go through each line and if it is data for either the life or 
	   exhib meters I add that data to an array for addition later.

While I have no proof that my original assumption that saltybet uses
	   default values for damage is true upon watching clips and comparing 
	   a few of their characters I downloaded I found that the downloaded 
	   version often had non-standard stats. This would explain a lot of 
	   things I saw in clips. So What if some characters are not using 
	   default stats for themselves how do I find out that information 
	   and display it?
	   
>My current approach is likely going to be to use another site that 
	   has many of the same characters as saltybet at seemingly similar power
	   I will use information that I grab from there as well as the info
	   from saltybet in order to paint a more clear picture. The other option
	   would be to download all 9000+ saltybet characters and have the program
	   simply compare their data, however i do not have the storage for that.
	   ***this solution was never implemented as personal issues kept me busy until school started again***
## Ideas:
* Create a way for the program to auto detect when new fighters are on the
	  screen and have then automatically fill out the information on its own.
* Maybe switch the project to focus on spriteclub due to its more transparent
	  design
