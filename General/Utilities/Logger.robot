*** Settings ***
Resource    loader.robot

*** Keywords ***
info
   [Arguments]   ${message}         ${logLevel}=INFO
   log      ${\n}Info Log-->: ${message} :${\n}         level=${logLevel}
   log to console      ${\n}Info Log-->: ${message} :${\n}


debug
         [Arguments]  ${message}
         log      ${\n}Debug Log-->:${message}:${\n}        DEBUG
         log to console      ${\n}Debug Log-->:${message}:${\n}




steplog
        [Arguments]  ${message}
        log             ${\n}==================== ${message} ======================${\n}
        log to console  ${\n}==================== ${message} ======================${\n}



Take Screenshot
    capture page screenshot
#    reload current page