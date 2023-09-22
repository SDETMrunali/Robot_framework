*** Settings ***
Documentation    login testcase

Suite Setup         Run Keywords   Login
Suite Teardown      Run Keywords   Logout

Resource            ../../General/Utilities/loader.robot
Resource            ../keyword/keyword_login.robot
Variables           ../keyword/variables.py


*** Test Cases ***
Test Case 01: Navigate to PC
    [Tags]  PC  PC_Regression    PC_Scan   PC_OndemandScan   test
    info    test

*** Keywords ***
Login
    Login to FO  ${username}    ${password}    ${url}

Logout
    Logout from FO