
*** Settings ***
Resource            ../Utilities/loader.robot

###################################################################
###################### Setup/Tear Down ############################
###################################################################
*** Keywords ***

Login to FO
    [Arguments]      ${user}    ${password}     ${url}
    info    user: ${user} password: ${password} url: ${url}
    Get Chrome
    set browser implicit wait      10s
    set selenium implicit wait     10s
    Input Text    ${fo_userlogin_username_Inputbox}     ${user}
    Input Text  ${fo_userlogin_password_Inputbox}   ${password}
    Click Button     ${fo_userlogin_login_button}
    Run Keyword And Ignore Error     Call QWEB version API    ${user}    ${password}
    Wait Until Page Does Not Contain Element    ${wait_Refreshing_Data}     ${configurable_wait_time}
    Wait Until Page Does Not Contain Element    ${wait_Loading_VM}
#    Wait Until Page Contains     ${user}    ${configurable_wait_time}


Get Chrome
    [Arguments]     ${Arg_url}=${url}
    open browser    ${Arg_url}/qglogin/index.html?status=timeout    ${browser}

Logout from FO
    switch window   main        timeout=5s
    go To   ${url}/fo/login.php?logout=1
    Close All Browsers

Check FO Login Title
    Steplog  Checking Title Before FO Login
    ${log_in_page_status}=          Run Keyword And Return Status    Title Should Be     ${before_login_title}
    IF  ${log_in_page_status}!=True
        reload page
        FAIL
    END