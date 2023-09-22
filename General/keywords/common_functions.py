"""
This file contains all common methods for script
"""

def convert_list_into_db_format_input(lis):
    db_formatted_list = str(lis)
    db_formatted_list = db_formatted_list.strip('[').strip(']')
    return db_formatted_list
