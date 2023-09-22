Name :
Sauce Demo Website Test Automation Assignment

Description :
In this project we have automated the Sauce Demo Website.
Test Case contains flow to find the cheapest or most expensive product from the product list.
For creating test suite robot framework has been used.

Flow of the test suite as below:
1. Login into website.
2. Filter the products as low to high.
3. Selecting the first product as it will be the cheapest or most expensive product.
4. Filling the postal details.
5. And Ordering the product


Installation :
1. Install IDE (Pycharm)
2. Install Python (pip install python)
3. Install Selenium (pip install selenium==4.9.1 )
4. Install Robot Framework (pip install robotframework)
5. Install Robot Framework Selenium Library (pip install -U robotframework-seleniumlibrary)
6. Add intelliBot @SeleniumLibrary Patched (Help pycharm to identify .robot files)
7. Download ChromeDriver which is compatible to Chrome Browser and save it in Python > Script Folder

Usage :
To test the Generic flow of ordering the product Sauce Demo Website

Steps to Execute :
1. Provide all the required variables in OrderCheapestProduct.robot or OrderMostExpensiveProduct.robot
2. Navigate to terminal of IDE
3. Use command : robot --variable Password:secret_sauce --outputdir Results TestCases/OrderCheapestProduct.robot
4. Replace secret_sauce according to the password
4. Click Enter
