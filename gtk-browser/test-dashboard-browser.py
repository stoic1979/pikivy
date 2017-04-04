#!/usr/bin/env python
 
import gtk
import webkit
import gobject
import sys, warnings

url = "https://freeboard.io/board/G6qZxn"
 
width=800
height=480
 
def go_back(widget, data=None):
    webview.go_back()
 
def go_forward(widget, data=None):
    webview.go_forward()
 
def refresh(widget, data=None):
    webview.reload()
    
def homepage(widget, data=None):
    webview.load_uri(url)
 
def update_buttons(widget, data=None):
    back_button.set_sensitive(webview.can_go_back())
    #forward_button.set_sensitive(webview.can_go_forward())
 
 
win = gtk.Window()
webview = webkit.WebView()
sw = gtk.ScrolledWindow()
 
win.set_size_request(width,height)
win.set_decorated(False)
win.connect("destroy", lambda q: gtk.main_quit())
 
webview.load_uri(url)
 
toolbar = gtk.Toolbar()
 
back_button = gtk.ToolButton(gtk.STOCK_GO_BACK)
back_button.connect("clicked", go_back)
 
#forward_button = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
#forward_button.connect("clicked", go_forward)
 
refresh_button = gtk.ToolButton(gtk.STOCK_REFRESH)
refresh_button.connect("clicked", refresh)
 
home_button = gtk.ToolButton(gtk.STOCK_HOME)
home_button.connect("clicked", homepage)
 
webview.connect("load_committed", update_buttons)
 
toolbar.add(back_button)
#toolbar.add(forward_button)
toolbar.add(refresh_button)
toolbar.add(home_button)
 
vbox = gtk.VBox(False, 0)
vbox.pack_start(toolbar, False, True, 0)
 
vbox.add(sw)
win.add(vbox)
sw.add(webview)
 
win.show_all()
gtk.main()
