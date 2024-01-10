#!/usr/bin/python3
"""Defines a text-reading function"""

def write_file(filename="", text=""):
	"""Write a string to UTF8 text file

	Args:
		filename(str): name of file to write
		text(str): the text to write in the file

	Returns:
		number of characters written
	"""
	
	with open(filename, "w", encoding="utf-8") as f:
		return f.write(text)
