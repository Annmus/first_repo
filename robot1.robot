*** Settings ***
Library  SeleniumLibrary

*** Variables ***


*** Keywords ***


*** Test Cases ***
Test 1
    Open Browser    https://pl.wikipedia.org    chrome
    wait until element is visible  pt-login     3   mamy blad
    Click Element   pt-login
    ${my_value}     get text    wpName1
    should be empty     ${my_value}
    input text  wpName1     RobotTests
    input text  wpPassword1     RobotFramework
    checkbox should not be selected  wpRemember
    select checkbox  wpRemember
    click element  wpLoginAttempt
    capture page screenshot  screen.png
    Sleep  5
