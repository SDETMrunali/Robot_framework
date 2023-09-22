*** Settings ***

Library         SeleniumLibrary
Library         String
Library         UtilsAuto.py
Library         APIUtils.py
Library         autoUtil.py
Library         DateTime
Library         OperatingSystem
Library         DatabaseLibrary
Library         Collections
Library         RequestsLibrary
Library         JSONLibrary
Library         SSHLibrary
Library         XML     use_lxml=True


#### General
Variables           ../../config/common/common_props.py
Variables           ../../config/environment/url_configurations.py
Variables           ../Locators/locator.py
Library             ../Locators/locator.py

Resource            ../Keywords/keyword_commonAction.robot
Library             ../Keywords/common_functions.py

Resource            Logger.robot



*** Variables ***
# this can be done as pod wise configuration file and add all variable there.
# pod4 username hwdy_rm

#robot --listener General/Utilities/ReportListener.py -d Results -A Environment/SmokeSuite.txt

####Improvements####
#api-client - contains api function for add ip, add ags etc by calling apis - done
#configuration file as variable to be included in execution - done but lets keep hardcoded for now.
#keep listener but we will use run.py for execution. report directory will take care of creating date wise resut directory. - jenkins
#email notification - done
#run from cucumber pod - done


