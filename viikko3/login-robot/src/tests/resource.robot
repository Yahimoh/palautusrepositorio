*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input New Command
    Input  new

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Input Registeration Credentials
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Input  ${username}
    Input  ${password}
    Input  ${password_confirmation}
    Run Application

