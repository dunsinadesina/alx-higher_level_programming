#!/usr/bin/python3
def search_replace(my_list, search, replace):
	res_list = []
	for element in my_list:
		if (element == search):
			res_list.append(replace)
		else:
			res_list.append(element)
	return (res_list)
