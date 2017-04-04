#
# Docs:
# http://www.pygtk.org/pygtk2reference/class-gtkwindow.html
#
import gtk 
import webkit 

url = "https://freeboard.io/board/G6qZxn"

view = webkit.WebView() 


sw = gtk.ScrolledWindow() 
sw.add(view) 

# btn
button = gtk.Button()
sw.add(button) 

win = gtk.Window(gtk.WINDOW_TOPLEVEL) 
win.resize(800, 480)
win.set_title("Web Browser Test!")
win.add(sw) 


win.show_all() 

view.open(url)
gtk.main()
