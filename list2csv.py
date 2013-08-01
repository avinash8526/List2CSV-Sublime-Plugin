#------------------------------------List to CSV----------------------------
# Author: Avinash Agrawal 
# Email : avinash8526@gmail.com
# Version : 2.0
#----------------------------------------------------------------------------

import sublime, sublime_plugin,ast,json,os,webbrowser

pdict = {}
dir_name = None
with open('Pattern') as patfile:
	pdict = json.load(patfile)
	dir_name = os.getcwd()


def fileHandler(filename,mode=None):
	global pdict,dir_name
	os.chdir(dir_name)
	if mode =='w':
		jsonFormat =  json.dumps(pdict, sort_keys = True, indent = 4)
		l = open(filename, mode)
		l.write(jsonFormat)
		l.close()
	else:
		with open(filename) as patfile:
	    		if filename == "Pattern":
	    			pdict = json.load(patfile)
	    		return patfile	

def on_loadP():
	global fileHandler,pdict
	if pdict["ShowPop"] == "Yes":
		#sublime.message_dialog("Plugin Notification :\n\nList2CSv Sublime PLugin is updated,\nImplemented Row length enhancement View Read Me File for detailed info.\n\n\t\t\t\t\t \n\n\nThis popup will not open again.")	
		try:
			webbrowser.open("https://github.com/avinash8526/List2CSV-Sublime-Plugin/blob/master/README.md")
		except:
			print "Not able to open file"
			pdict["ShowPop"] = "No"
		finally:
			f.close()				
		pdict["ShowPop"] = "No"
		fileHandler("Pattern",'w')

on_loadP()
class list2csvCommand(sublime_plugin.TextCommand):
	global fileHandler

	def run(self, edit):		
		sels = self.view.sel()		
		if self.isRegionEmpty(sels[0]):
			sublime.message_dialog("Please select list by pressing ctrl+A")
		else:
			if self.convertListTocsv(sels,edit) =="true":
				sublime.status_message("Conversion Done")

			
	def isRegionEmpty(self,region):
		return region.empty()

	def convertListTocsv(self,selection,edt):	
		global pdict
		rowlen = pdict['rowlen']
		print rowlen
		ed = 0
		t = 0		
		positions =  self.view.lines(selection[0])
		for times,pos in enumerate(positions):
			ed = times+ed
			self.view.insert(edt, pos.begin()+ed, pdict['FirstDel'])
			self.view.insert(edt, pos.end()+ed+1, pdict['SecondDel'])	
			ed = times+1
		sels = self.view.sel()
		positions =  self.view.lines(sels[0])	
		for pos in positions:
			if rowlen != "NULL" :
				t = t+1	
				if self.view.find('\n',pos.end()):
					nwlnreg = self.view.find('\n',pos.end())
					print "t is",t,"and rowlen is",rowlen
					if t==int(rowlen):
						t = 0
						continue
					else:
						self.view.replace(edt, nwlnreg, pdict['Separator'])
			else:
				if self.view.find('\n',pos.end()):
					nwlnreg = self.view.find('\n',pos.end())
					self.view.replace(edt, nwlnreg, pdict['Separator'])
							
		return "true"
							 
		
class l_settingsCommand(sublime_plugin.WindowCommand):
	global fileHandler
	
	def run(self):
		global pdict
		if pdict["Memory"] == "No" or pdict["Memory"] == "NO" :
			fileHandler("Pattern")
		patString = (str(pdict).replace("u",'')).replace(" ",'')
		self.window.show_input_panel("Please enter a pattern:", patString, self.on_done, None, None)
		

	def on_done(self,user_input):
		global pdict
		lpdict = pdict
		pdict = ast.literal_eval(user_input.replace(' ',''))
		for key in lpdict.keys():
			if key not in pdict.keys():
				self.panelO("Key is not found, refreshing pattern \nPlease put backslash followed by delimitter \\'")
				fileHandler("Pattern")

	def panelO(self,msg = None):
		panel_name = 'test'
		ref = self.window.get_output_panel(panel_name)
		self.window.run_command("show_panel",{"panel": "output." + panel_name})
		ref.set_read_only(False)
		edit = ref.begin_edit()
		ref.insert(edit,ref.size(),"\nError AVI0003\n")
		ref.insert(edit,ref.size(),msg)		
		ref.end_edit(edit)
		ref.set_read_only(True)
		
	@classmethod	
	def getClassHandler(cls):
		return l_settingsCommand(cls)
	

		