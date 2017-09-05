# -*- coding: utf-8 -*-
import os

def printtree(list_tree, filename):
	f = open(filename, 'w')
	for elem in list_tree:
		if type(elem) == list:
			ptinttree(elem, f)
		else:
			f.write(elem)
			if elem != list_tree[-1]:
				f.write("\n")
	f.close()
			
def filldirtylist(dirty_list, list_tree):
	for elem in list_tree:
		if type(elem) == list:
			filldirtylist(dirty_list,elem)
		else:
			dirty_list.append(elem)
			
def makeabspath(listofdirs, masterdir):
	abslistof_dirs = []
	for dir in listofdirs:
		abslistof_dirs.append(os.path.join(masterdir, dir))
	return abslistof_dirs
	
def checkforfolder(lst):
	for elem in lst:
		if os.path.isdir(elem) == True:
			finddir = True
			newdir = makeabspath(os.listdir(elem), elem)
			lst.extend(newdir)
			
def filldict(lst, strkey):
	folderdict = {}
	for elem in lst:
		if os.path.isfile(elem) == True:
			str = elem
			str.lower()
			for skey in strkey:
				if str.endswith(skey) == True:
					folderdict[elem] = True
	
	return folderdict
	
def filldictdir(lst):
	folderdict = {}
	for elem in lst:
		if os.path.isdir(elem) == True:
			str = elem
			str.lower()
			folderdict[elem] = True
	
	return folderdict
	
def listmerge(lst, lstlst):
	all=[]
	for el in lstlst:
		all.append(el)
	for el in lst:
		if (el not in lstlst):
			all.append(el)
	return all
	
def getfilteredfilesdirslist(directories, strkey):

	tree = []
	dirlist = []
	subdirlist = []
	finddir = False
	
	if strkey == [""]:
		finddir = True
	
	for _direct in directories:
		subdirlist = makeabspath(os.listdir(_direct), _direct)
		dirlist.extend(subdirlist)

	for dir in dirlist:
		if os.path.isdir(dir) == True:
			tree.append(makeabspath(os.listdir(dir), dir))
			checkforfolder(tree[len(tree) - 1])

	dirtylist = []
		
	filldirtylist(dirtylist, tree)

	folderdict = {}
	
	if finddir == True:
		folderdict = filldictdir(listmerge(dirtylist, subdirlist))
	else:
		folderdict = filldict(listmerge(dirtylist, subdirlist), strkey)

	keys = sorted(folderdict.keys())
	
	return keys
