# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 20:09:26 2018

@author: ms395951
"""
line='Sally Spade: 5\'2\" 128 lbs'

list=line.split()

LastName=list[1]
Height=list[2]
Weight=list[3]


def convertHeight(Height):
  splitString=Height.split('\'')
  feet=int(splitString[0])
  inches=splitString[1]
  inches=inches.split('\"')
  inches=inches[0]
  inches=int(inches)
  convertHeight=feet*12+inches
  return convertHeight

InchesHeight=convertHeight('5\'2\"')
Info=str(LastName+' '+str(InchesHeight)+' '+'Inches'+', '+str(Weight)+' '+'lbs')
print(Info)