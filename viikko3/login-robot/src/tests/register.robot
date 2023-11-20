*** Settings ***
Resource  resource.robot
Test Setup  Input New Command Setup

*** Test Cases ***
Register With Valid Username And Password
    Input Registeration Credentials  random  kalle123  kalle123
    Output Should Contain  New user registered
 
Register With Already Taken Username
    Create User  testi  salis123
    Input Registeration Credentials  testi  salis123  salis123
    Output Should Contain  Username already taken

Register With Too Short Username
    Input Registeration Credentials  ra  kalle123  kalle123
    Output Should Contain  Username too short

Register With Invalid Username
    Input Registeration Credentials  yah1a  kalle123  kalle123
    Output Should Contain  Invalid username

Register With Too Short Password
    Input Registeration Credentials  yahia  salis  salis
    Output Should Contain  Password too short

Register With Password Containing Only Letters
    Input Registeration Credentials  yahia  salissss  salissss
    Output Should Contain  Password should contain letters and numbers

*** Keywords ***
Input New Command Setup
    Input New Command

Registration Should Succeed
    Main Page Should Be Open
