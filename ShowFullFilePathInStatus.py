import sublime, sublime_plugin, os

class ShowFullFilePathInStatus(sublime_plugin.EventListener):
	def on_activated_async(self, view):
	    path = os.path.abspath(view.file_name())
	    if path is None:
	        view.erase_status('_filename')
	    else:
	        view.set_status('_filename', "Full path: " + path)