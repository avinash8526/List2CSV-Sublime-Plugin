#------------------------------------List to CSV----------------------------
# Author: Avinash Agrawal 
# Email : avinash8526@gmail.com
# Version : 1.0
#----------------------------------------------------------------------------

import sublime, sublime_plugin

class list2csvCommand(sublime_plugin.TextCommand):
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
		for se in selection:			
			positions =  self.view.lines(se)
			for pos in positions:
				if self.view.find('\n',pos.end()):
					nwlnreg = self.view.find('\n',pos.end())
					self.view.replace(edt, nwlnreg, ',\r')
		return "true"			 
		
