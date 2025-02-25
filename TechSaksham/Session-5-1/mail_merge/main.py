# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:51:07 2025

@author: doshi
"""

PLACEHOLDER="[name]"

with open("names.txt",'r') as names_list:
    names=names_list.readlines()
    
with open("samplemail.docx") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        
        with open(f"letter_for_{stripped_name}.docx",'w+') as completed_letter:
            completed_letter.write(new_letter)
