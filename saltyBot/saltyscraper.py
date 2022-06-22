from bs4 import BeautifulSoup as soup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
#CHANGE THESE TO CHANGE THE ACCOUNT THAT IS USED FOR THE LOGIN

CHROMEWEBDRIVERPATH = './chromedriver' #can be changed if user is using a different driver for different system

loginPageURL = 'https://www.saltybet.com/authenticate?signin=1'
compendiumURL = 'https://www.saltybet.com/compendium?search='
homeURL = 'https://www.saltybet.com'

class player():
    name = ''
    matches = 0
    winRate = ''
    tier = ''
    life = 1000
    meter = -1
    attack = 100
    defense = 100
    exhibMeter = 0

################################################################
# Name:        createDriver()
#
# description: creates and returns a webdriver object driving 
#              Chrome. The options that it uses are to avoid a bunch
#              log output that was getting annoying
#  
# pre-conditions: function is used to generate a driver
#
# post-conditions: returns a chrome webdriver set up to avoid annoying logs
#################################################################
def createDriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path=CHROMEWEBDRIVERPATH)
    driver = webdriver.Chrome(options=options)
    return driver


################################################################
# Name:         fillOutPlayer
#
# description:  Uses the webdriver, and the playerNum to fill out 
#               the data for a player object with the information 
#               presented on the home page
# 
# pre-conditions: player is a player object, playerNum is a int, driver 
#                 is a working webdriver for selenium
#
# post-conditions: player object should be filled out with all data 
#                  from the home page
#################################################################
def fillOutPlayer(player, playerNum):
    if playerNum == 1:
        playerShell = browser.find_element(By.ID, "sbettors1")
    else:
        playerShell = browser.find_element(By.ID, "sbettors2")

    #name
    playerShell = playerShell.find_element(By.TAG_NAME, "strong")
    player.name = playerShell.text

    if playerNum == 1:
        playerShell = browser.find_element(By.ID, "sbettors1")
    else:
        playerShell = browser.find_element(By.ID, "sbettors2")

    #get all of the bettor-line elements into an array that I can go through
    playerShell = playerShell.find_elements(By.CLASS_NAME, "bettor-line")

    #Total Matches
    tm = playerShell[0]
    totalM = tm.text
    selections = totalM.split('s')
    player.matches = int(selections[1])

    #winRate
    wr = playerShell[1]
    winR = wr.text
    selections = winR.split('e')
    player.winRate = selections[1]

    #tier
    tr = playerShell[2]
    tier = tr.text
    selections = tier.split('r')
    player.tier = selections[1]

    #life
    lf = playerShell[3]
    life = lf.text
    selections = life.split('e')
    player.life = int(selections[1])

    #meter
    mr = playerShell[4]
    meter = mr.text
    selections = meter.split('r')
    player.meter = int(selections[1])

################################################################
# Name:        login
#
# description: uses the email and password to login into saltybet
#              after it has been pulled up in the webdriver
#  
# pre-conditions: driver is a valid chrome webdriver, email is a 
#                 valid string and pword is a valid string
#
# post-conditions: driver should be returned in a state where the 
#                  the website has been logged into
#################################################################
def login():

    email = input("please input your saltybet email: ")
    pword = input("please input your saltybet password: ")

    browser.get(loginPageURL)
    userInput = browser.find_element(By.ID, "email")
    userInput.send_keys(email)
    userPass = browser.find_element(By.ID, "pword")
    userPass.send_keys(pword)
    userPass.send_keys(Keys.ENTER)
    return browser

################################################################
# Name:        displayPlayers
#
# description: displays the information of the two players input as redPlayer and bluePlayer
#  
# pre-conditions: redPlayer is a player object, bluePlayer is a playerObject
#
# post-conditions: the data for both player objects is output into the console
#################################################################
def displayPlayers(redPlayer, bluePlayer):
    print("redPlayer name: " + redPlayer.name + " VS bluePlayer name: " + bluePlayer.name)
    print("redPlayer total matches: " + str(redPlayer.matches) + " | bluePlayer total matches: " + str(bluePlayer.matches))
    print("redPlayer win rate: " + redPlayer.winRate + " | bluePlayer win rate: " + bluePlayer.winRate)
    print("redPlayer tier: " + redPlayer.tier + " | bluePlayer tier: " + bluePlayer.tier)
    print("redPlayer life: " + str(redPlayer.life) + " | bluePlayer life: " + str(bluePlayer.life))
    print("redPlayer meter: " + str(redPlayer.meter) + " | bluePlayer meter: " + str(bluePlayer.meter))
    print("redPlayer exhibMeter: " + str(redPlayer.exhibMeter) + " | bluePlayer exhibMeter: " + str(bluePlayer.exhibMeter))

################################################################
# Name:        getCompendiumData
#
# description: grabs data from the compendium on the current character
#  
# pre-conditions: player is a player object with its name filled out
#
# post-conditions: player will have compendium data added to it
#################################################################
def getCompendiumData(player):

    exhibArr = []

    searchTerm = player.name
    searchTerm = searchTerm.replace(" ", "+")
    searchTerm = compendiumURL + searchTerm

    browser.get(searchTerm)
    
    playerShell = browser.find_element(By.ID, 'tierlist')
    results = playerShell.find_elements(By.TAG_NAME, 'li')
    for x in results: #O(n)
        if x.text == player.name:
            playerShell = x
            playerShell.click()
            break
    
    playerShell = browser.find_element(By.ID, 'compendiumright')

    # see if this character has any changes listed in the compendium
    # if they dont then set lifeArr and exhibArr to both just contain 0
    # otherwise fill out the arr's with their proper values

    try: 
        playerShell = playerShell.find_element(By.TAG_NAME, 'div')
        statBlock = playerShell.text
        if statBlock.__contains__('\n'):

            resultArr = statBlock.split("\n")
            for x in resultArr: #O(n)
                if x.__contains__('exhib meter'):
                    tempArr = x.split('exhib meter ')
                    exhibArr.append(int(tempArr[1]))   
    except:
        exhibArr = [0]

    for x in exhibArr:
        player.exhibMeter += x

    print(exhibArr)
    
def main():

    global browser
    browser = createDriver()
    browser = login()

    again = 1
    while again == 1:
        redPlayer = player()
        bluePlayer = player()

        #get player info and display
        fillOutPlayer(redPlayer, 1)
        fillOutPlayer(bluePlayer, 0)

        getCompendiumData(redPlayer)
        getCompendiumData(bluePlayer)

        displayPlayers(redPlayer, bluePlayer)
        browser.get(homeURL)
        again = input("Enter 1 when the next set of fighter information apears on the screen. Enter anything else to exit.")
        try:
            again = int(again)
        except:
            print("goodbye")
            break

    print("goodbye")
    
main()