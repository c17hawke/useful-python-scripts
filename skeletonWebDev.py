#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 02:49:57 2018

@author: c17hawke
"""

import os
import sys

def createProject(projectName):
	os.system("mkdir "+projectName)
	os.system("mkdir {0}/css {0}/images".format(projectName))
	os.system("touch {0}/css/styles.css {0}/index.html {0}/index.js".format(projectName))
	os.system("clear")

def createThings():
	projectName = input("enter the project Name you want to create: \n>>>")
	createProject(projectName)
	openIn_atom = input("Would you like to open project '{}' in atom \
		and in chrome as well ?\nenter 'y'\nelse press any key to exit\n>>>".format(projectName))
	if openIn_atom == 'y':
		os.system("atom {0}".format(projectName))
		os.system("google-chrome {0}/index.html".format(projectName))
		print("opening the project in atom")
	else:
		print("Project '{}' created\nExiting program!!".format(projectName))

def deleteProject(projectName):
	while True:
		print("\n\nWarning !! this will delete everything, still want to continue ?")
		Flag = input("if yes press 'y'\n>>>")
		if Flag == "y":
			os.system("rm -r {0}".format(projectName))
			print("project '{}' deleted".format(projectName))
			sys.exit()
		else:
			print("Exiting program!!")
			sys.exit()

def destroyThings():
	for i in range(2):
		projectName = input("enter the project Name you want to delete: \n>>>")
		testExistence = os.path.isdir(projectName)
		if testExistence:
			deleteProject(projectName) 
		elif i == 0:
			print("there is no such project named '{}' exists\nplease try again once more".format(projectName))
	print("\nyou have entered wrong project name twice\nHence Terminating the program!!")

def main():
	choice = input("Choose \n(1) to create press 'c' \n(2) to delete an existing project press 'd'\n>>>")
	if choice == 'c':
		createThings()
	elif choice == 'd':
		destroyThings()
	else:
		print("Wrong choice, please try again !")
		print("Exiting program!!")
		sys.exit()

if __name__ == '__main__':
	main()