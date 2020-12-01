#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import QT_VERSION_STR
import json
from scene import Scene

#delete items                   fait
#move group                     a faire = non
#barre d'etat                   fait 
#polygon                        fait
#text finir                     fait
#menusurgissant                 fait
#ajouter dans barre d'outils    fait
#save voir si fichier existe    fait     coords text incorrectes
#new file                       fait
 
#color,                         fait
#font,                          fait
#width                          fait

########       README         ######### !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.file=None
        self.resize(500, 300)
        self.setWindowTitle("Paint")
        self.create_scene()
        self.create_actions()
        # self.create_ContextMenu()
        self.create_menus()
        self.connect_actions()
        self.create_status_bar()
        #to check default tools and styles
        self.action_line.setChecked(True)
        self.action_brush_solid.setChecked(True)
        self.action_solid.setChecked(True)
        self.action_pen_width_3.setChecked(True)
##        textEdit = QtGui.QTextEdit()
##        self.setCentralWidget(textEdit)
    def create_scene(self) :
        view=QtWidgets.QGraphicsView()
        self.scene=Scene(self)
        view.setScene(self.scene)
        self.setCentralWidget(view)

    def create_actions(self) :
        #File
        self.action_new = QtWidgets.QAction(QtGui.QIcon('icons/new.png'), 'New', self)
        self.action_new.setShortcut('Ctrl+N')
        self.action_new.setStatusTip('Open a New File')
        self.action_save = QtWidgets.QAction(QtGui.QIcon('icons/save.png'), 'Save', self)
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.setStatusTip('Save to file')
        self.action_save_as = QtWidgets.QAction(QtGui.QIcon('icons/save_as.png'), 'Save as', self)
        self.action_save_as.setShortcut('Ctrl+Shift+S')
        self.action_save_as.setStatusTip('Save to file as')
        self.action_open = QtWidgets.QAction(QtGui.QIcon('icons/open.png'), 'Open', self)
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.setStatusTip('Open file')
        self.action_exit = QtWidgets.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.setStatusTip('Exit application')
        self.group_action_tools = QtWidgets.QActionGroup(self)
        #Tools
        self.action_line = QtWidgets.QAction(QtGui.QIcon('icons/tool_line.png'),self.tr("&Line"), self)
        self.action_line.setCheckable(True)
        self.action_line.setChecked(False)


        self.action_rectangle = QtWidgets.QAction(QtGui.QIcon('icons/tool_rectangle.png'),self.tr("&Rectangle"), self)
        self.action_rectangle.setCheckable(True)
        self.action_rectangle.setChecked(False)

        self.action_ellipse = QtWidgets.QAction(QtGui.QIcon('icons/tool_ellipse.png'),self.tr("&Ellipse"), self)
        self.action_ellipse.setCheckable(True)
        self.action_ellipse.setChecked(False)

        self.action_polygon = QtWidgets.QAction(QtGui.QIcon('icons/tool_polygon.png'),self.tr("&Polygon"), self)
        self.action_polygon.setCheckable(True)
        self.action_polygon.setChecked(False)

        self.action_text = QtWidgets.QAction(QtGui.QIcon('icons/tool_text.png'),self.tr("&Text"), self)
        self.action_text.setCheckable(True)
        self.action_text.setChecked(False)
        
        self.group_action_tools.addAction(self.action_line)
        self.group_action_tools.addAction(self.action_rectangle)
        self.group_action_tools.addAction(self.action_ellipse)
        self.group_action_tools.addAction(self.action_polygon)
        self.group_action_tools.addAction(self.action_text)
        #Style
        self.action_pen_color = QtWidgets.QAction(self.tr("Color"), self)
        self.action_pen_line = QtWidgets.QAction(self.tr("Line"), self)
        self.action_pen_width = QtWidgets.QAction(self.tr("Width"), self)
        self.action_brush_color = QtWidgets.QAction(self.tr("Color"), self)
        self.action_brush_fill = QtWidgets.QAction(self.tr("Fill"), self)
        self.action_font = QtWidgets.QAction(self.tr("Font"),self)

        self.action_solid = QtWidgets.QAction(QtGui.QIcon('icons/qpen-solid1.png'),self.tr("&SolidLine"), self)
        self.action_solid.setCheckable(True)
        self.action_solid.setChecked(False)
        self.group_action_tools.addAction(self.action_solid)
        self.action_dot = QtWidgets.QAction(QtGui.QIcon('icons/qpen-dot1.png'),self.tr("&DotLine"), self)
        self.action_dot.setCheckable(True)
        self.action_dot.setChecked(False)
        self.group_action_tools.addAction(self.action_dot)
        self.action_dash = QtWidgets.QAction(QtGui.QIcon('icons/qpen-dash1.png'),self.tr("&DashLine"), self)
        self.action_dash.setCheckable(True)
        self.action_dash.setChecked(False)
        self.group_action_tools.addAction(self.action_dash)
        self.action_dashdot = QtWidgets.QAction(QtGui.QIcon('icons/qpen-dashdot1.png'),self.tr("&DashDotLine"), self)
        self.action_dashdot.setCheckable(True)
        self.action_dashdot.setChecked(False)
        self.group_action_tools.addAction(self.action_dashdot)
        self.action_dashdotdot = QtWidgets.QAction(QtGui.QIcon('icons/qpen-dashdotdot1.png'),self.tr("&DashDotDotLine"), self)
        self.action_dashdotdot.setCheckable(True)
        self.action_dashdotdot.setChecked(False)
        self.group_action_tools.addAction(self.action_dashdotdot)


        self.action_pen_width_1 = QtWidgets.QAction(self.tr("&1"), self)
        self.action_pen_width_1.setCheckable(True)
        self.action_pen_width_1.setChecked(False)
        self.group_action_tools.addAction(self.action_pen_width_1)
        self.action_pen_width_2 = QtWidgets.QAction(self.tr("&2"), self)
        self.action_pen_width_2.setCheckable(True)
        self.action_pen_width_2.setChecked(False)
        self.group_action_tools.addAction(self.action_pen_width_2)
        self.action_pen_width_3 = QtWidgets.QAction(self.tr("&3"), self)
        self.action_pen_width_3.setCheckable(True)
        self.action_pen_width_3.setChecked(False)
        self.group_action_tools.addAction(self.action_pen_width_3)
        self.action_pen_width_4 = QtWidgets.QAction(self.tr("&4"), self)
        self.action_pen_width_4.setCheckable(True)
        self.action_pen_width_4.setChecked(False)
        self.group_action_tools.addAction(self.action_pen_width_4)
        self.action_pen_width_5 = QtWidgets.QAction(self.tr("&5"), self)
        self.action_pen_width_5.setCheckable(True)
        self.action_pen_width_5.setChecked(False)
        self.group_action_tools.addAction(self.action_pen_width_5)
        self.action_pen_width_6 = QtWidgets.QAction(self.tr("&6"), self)
        self.action_pen_width_6.setCheckable(True)
        self.action_pen_width_6.setChecked(False)
        self.group_action_tools.addAction(self.action_pen_width_6)
 
        self.action_brush_no = QtWidgets.QAction(QtGui.QIcon('icons/nobrush.png'),self.tr("&No"), self)
        self.action_brush_no.setCheckable(True)
        self.action_brush_no.setChecked(False)
        self.group_action_tools.addAction(self.action_brush_no)
        self.action_brush_solid = QtWidgets.QAction(QtGui.QIcon('icons/brush_solid.png'),self.tr("&Solid"), self)
        self.action_brush_solid.setCheckable(True)
        self.action_brush_solid.setChecked(False)
        self.group_action_tools.addAction(self.action_brush_solid)
        self.action_brush_dense3 = QtWidgets.QAction(QtGui.QIcon('icons/brush_dense3.png'),self.tr("&Dense3"), self)
        self.action_brush_dense3.setCheckable(True)
        self.action_brush_dense3.setChecked(False)
        self.group_action_tools.addAction(self.action_brush_dense3)
        self.action_brush_dense5 = QtWidgets.QAction(QtGui.QIcon('icons/brush_dense5.png'),self.tr("&Dense5"), self)
        self.action_brush_dense5.setCheckable(True)
        self.action_brush_dense5.setChecked(False)
        self.group_action_tools.addAction(self.action_brush_dense5)
        self.action_brush_dense7 = QtWidgets.QAction(QtGui.QIcon('icons/brush_dense7.png'),self.tr("&Dense7"), self)
        self.action_brush_dense7.setCheckable(True)
        self.action_brush_dense7.setChecked(False)
        self.group_action_tools.addAction(self.action_brush_dense7)
        self.action_brush_cross = QtWidgets.QAction(QtGui.QIcon('icons/brush_cross.png'),self.tr("&Cross"), self)
        self.action_brush_cross.setCheckable(True)
        self.action_brush_cross.setChecked(False)
        self.group_action_tools.addAction(self.action_brush_cross)
        self.action_brush_diag = QtWidgets.QAction(QtGui.QIcon('icons/brush_diag.png'),self.tr("&Diag"), self)
        self.action_brush_diag.setCheckable(True)
        self.action_brush_diag.setChecked(False)
        self.group_action_tools.addAction(self.action_brush_diag)
        self.action_brush_diag_cross = QtWidgets.QAction(QtGui.QIcon('icons/brush_diag_cross.png'),self.tr("&Diag Cross"), self)
        self.action_brush_diag_cross.setCheckable(True)
        self.action_brush_diag_cross.setChecked(False)
        self.group_action_tools.addAction(self.action_brush_diag_cross)
        # self.action_brush_gradient = QtWidgets.QAction(QtGui.QIcon('icons/brush_gradient.png'),self.tr("&Gradient"), self)
        # self.action_brush_gradient.setCheckable(True)
        # self.action_brush_gradient.setChecked(False)
        # self.group_action_tools.addAction(self.action_brush_gradient)


    def create_menus(self) :
 #       statusbar=self.statusBar()
        menubar = self.menuBar()

        #File
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(self.action_new)
        menu_file.addAction(self.action_open)
        menu_file.addAction(self.action_save)
        menu_file.addAction(self.action_save_as)
        menu_file.addSeparator()
        menu_file.addAction(self.action_exit)

        #Tools
        self.menu_tools = menubar.addMenu('&Tools')
        self.menu_tools.addAction(self.action_line)
        self.menu_tools.addAction(self.action_rectangle)
        self.menu_tools.addAction(self.action_ellipse)
        self.menu_tools.addAction(self.action_polygon)
        self.menu_tools.addSeparator()
        self.menu_tools.addAction(self.action_text)

        #Style
        self.menu_style=menubar.addMenu('&Style')
        self.menu_style_pen=self.menu_style.addMenu('Pen')
        self.menu_style_pen.addAction(self.action_pen_color)
        self.menu_style_pen_line=self.menu_style_pen.addMenu('Line')
        self.menu_style_pen_line.addAction(self.action_solid)
        self.menu_style_pen_line.addAction(self.action_dot)
        self.menu_style_pen_line.addAction(self.action_dash)
        self.menu_style_pen_line.addAction(self.action_dashdot)
        self.menu_style_pen_line.addAction(self.action_dashdotdot)

        menu_style_pen_width=self.menu_style_pen.addMenu('Width (px)')
        menu_style_pen_width.addAction(self.action_pen_width_1)
        menu_style_pen_width.addAction(self.action_pen_width_2)
        menu_style_pen_width.addAction(self.action_pen_width_3)
        menu_style_pen_width.addAction(self.action_pen_width_4)
        menu_style_pen_width.addAction(self.action_pen_width_5)
        menu_style_pen_width.addAction(self.action_pen_width_6)

        self.menu_style_brush=self.menu_style.addMenu('Brush')
        self.menu_style_brush.addAction(self.action_brush_color)
        self.menu_style_brush_fill=self.menu_style_brush.addMenu('Fill')
        self.menu_style_brush_fill.addAction(self.action_brush_no)
        self.menu_style_brush_fill.addAction(self.action_brush_solid)
        self.menu_style_brush_fill.addAction(self.action_brush_dense3)
        self.menu_style_brush_fill.addAction(self.action_brush_dense5)
        self.menu_style_brush_fill.addAction(self.action_brush_dense7)
        self.menu_style_brush_fill.addAction(self.action_brush_cross)
        self.menu_style_brush_fill.addAction(self.action_brush_diag)
        self.menu_style_brush_fill.addAction(self.action_brush_diag_cross)
        # self.menu_style_brush_fill.addAction(self.action_brush_gradient)

        self.menu_style.addAction(self.action_font)

        #Help
        menu_help=self.menuBar().addMenu(self.tr("&Help"))
        self.action_about_us = menu_help.addAction(self.tr("&Abut Us"))
        self.action_about_qt = menu_help.addAction(self.tr("&About Qt"))
        self.action_about_app = menu_help.addAction(self.tr("&About the Application"))

        toolbarExit = self.addToolBar('Exit')
        toolbarExit.addAction(self.action_open)
        toolbarExit.addAction(self.action_save)
        toolbarExit.addAction(self.action_exit)
        toolbarTools = self.addToolBar('Tools')
        toolbarTools.addAction(self.action_line)
        toolbarTools.addAction(self.action_rectangle)
        toolbarTools.addAction(self.action_polygon)
        toolbarTools.addAction(self.action_ellipse)
        toolbarTools.addAction(self.action_text)


    def create_status_bar(self):

        # setting status bar message 
        self.statusBar().showMessage("Status Bar")
  
        # creating a label widget 
        self.label_1 = QtWidgets.QLabel("Label 1") 

        # adding label to status bar 
        self.statusBar().addPermanentWidget(self.label_1) 


    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseMove :
            pos = event.pos()
            self.label_1.setText("x :%d, y :%d" % (pos.x(), pos.y()))
        return super(MainWindow, self).eventFilter(source, event)

    def connect_actions(self) :
        self.action_new.triggered.connect(self.file_new)
        self.action_open.triggered.connect(self.file_open)
        self.action_save.triggered.connect(self.file_save)
        self.action_save_as.triggered.connect(self.file_save_as)
        self.action_exit.triggered.connect(self.file_exit)
        self.action_about_us.triggered.connect(self.help_about_us)
        self.action_about_qt.triggered.connect(self.help_about_qt)
        self.action_about_app.triggered.connect(self.help_about_app)
        self.action_pen_color.triggered.connect(self.pen_color_selection)
        self.action_brush_color.triggered.connect(self.brush_color_selection)
        self.action_font.triggered.connect(self.font_selection)

        self.action_line.triggered.connect(lambda checked, tool="line": self.set_action_tool(checked,tool))
        self.action_rectangle.triggered.connect(lambda checked, tool="rectangle": self.set_action_tool(checked,tool))
        self.action_ellipse.triggered.connect(lambda checked, tool="ellipse": self.set_action_tool(checked,tool))
        self.action_polygon.triggered.connect(lambda checked, tool="polygon": self.set_action_tool(checked,tool))
        self.action_text.triggered.connect(lambda checked, tool="text": self.set_action_tool(checked,tool))

        self.action_pen_width_1.triggered.connect(lambda checked, width="1": self.set_action_width(checked,width))
        self.action_pen_width_2.triggered.connect(lambda checked, width="2": self.set_action_width(checked,width))
        self.action_pen_width_3.triggered.connect(lambda checked, width="3": self.set_action_width(checked,width))
        self.action_pen_width_4.triggered.connect(lambda checked, width="4": self.set_action_width(checked,width))
        self.action_pen_width_5.triggered.connect(lambda checked, width="5": self.set_action_width(checked,width))
        self.action_pen_width_6.triggered.connect(lambda checked, width="6": self.set_action_width(checked,width))

        self.action_solid.triggered.connect(lambda checked, pen="SolidLine": self.set_action_pen(checked,pen))
        self.action_dot.triggered.connect(lambda checked, pen="DotLine": self.set_action_pen(checked,pen))
        self.action_dash.triggered.connect(lambda checked, pen="DashLine": self.set_action_pen(checked,pen))
        self.action_dashdot.triggered.connect(lambda checked, pen="DashDotLine": self.set_action_pen(checked,pen))
        self.action_dashdotdot.triggered.connect(lambda checked, pen="DashDotDotLine": self.set_action_pen(checked,pen))

        self.action_brush_no.triggered.connect(lambda checked, brush="No": self.set_action_brush(checked,brush))
        self.action_brush_solid.triggered.connect(lambda checked, brush="Solid": self.set_action_brush(checked,brush))
        self.action_brush_dense3.triggered.connect(lambda checked, brush="Dense3": self.set_action_brush(checked,brush))
        self.action_brush_dense5.triggered.connect(lambda checked, brush="Dense5": self.set_action_brush(checked,brush))
        self.action_brush_dense7.triggered.connect(lambda checked, brush="Dense7": self.set_action_brush(checked,brush))
        self.action_brush_cross.triggered.connect(lambda checked, brush="Cross": self.set_action_brush(checked,brush))
        self.action_brush_diag.triggered.connect(lambda checked, brush="Diag": self.set_action_brush(checked,brush))
        self.action_brush_diag_cross.triggered.connect(lambda checked, brush="Diag Cross": self.set_action_brush(checked,brush))
        # self.action_brush_gradient.triggered.connect(lambda checked, brush="Gradient": self.set_action_brush(checked,brush))


    def set_action_tool(self,checked, tool) :
        print("lamda checked, tool : ",checked, tool)
        self.scene.set_tool(tool)
        self.statusBar().showMessage("Tool used : "+tool)


    def set_action_pen(self,checked, pen) :
        print("lamda checked, pen : ",checked, pen)
        self.scene.set_pen(pen)
        self.statusBar().showMessage("Pen used : "+pen)

    def set_action_width(self,checked,width):
        print("lamda checked, width : ",checked, width)
        self.scene.set_width(width)
        self.statusBar().showMessage("Width of the pen used : "+width)

    def set_action_brush(self,checked, brush) :
        print("lamda checked, brush : ",checked, brush)
        self.scene.set_brush(brush)
        self.statusBar().showMessage("Brush used : "+brush)
    
    def file_exit(self):
        msgBox=QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle("Exit")
        msgBox.setText("Are you sure you want to exit?")
        msgBox.setInformativeText("Your file will may be not save !")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ignore | QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        msgBox.exec_()
        buttonI=msgBox.button(QtWidgets.QMessageBox.Ignore)
        buttonS=msgBox.button(QtWidgets.QMessageBox.Save)
        buttonC=msgBox.button(QtWidgets.QMessageBox.Cancel)
        if msgBox.clickedButton()==msgBox.button(QtWidgets.QMessageBox.Ignore):
            #Ignore was clicked
            exit(0)
        elif msgBox.clickedButton()==msgBox.button(QtWidgets.QMessageBox.Cancel):
            #Cancel was clicked
            msgBox.close()
        elif msgBox.clickedButton()==msgBox.button(QtWidgets.QMessageBox.Save):
            #Save was clicked
            self.file_save()
            exit(0)
            
    def file_new(self):
        msgBox=QtWidgets.QMessageBox(self)
        msgBox.setWindowTitle("New File")
        msgBox.setText("Are you sure you want create a new file ?")
        msgBox.setInformativeText("This action will may not save your current file!")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel)
        msgBox.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        msgBox.button(QtWidgets.QMessageBox.Yes).setText("New Without Saving")
        msgBox.button(QtWidgets.QMessageBox.Save).setText("Save and New")
        msgBox.exec_()
        if msgBox.clickedButton()==msgBox.button(QtWidgets.QMessageBox.Yes):
            #Ignore was clicked
            self.scene.clear()
            self.statusBar().showMessage("Scene cleared")
        elif msgBox.clickedButton()==msgBox.button(QtWidgets.QMessageBox.Cancel):
            #Cancel was clicked
            msgBox.close()
        elif msgBox.clickedButton()==msgBox.button(QtWidgets.QMessageBox.Save):
            #Save was clicked
            self.file_save()
            self.scene.clear()
            self.statusBar().showMessage("Scene cleared")
            self.file=None
       
    def file_open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.getcwd())
        # print(filename[0])
        if len(filename[0])>0:
            fileopen=QtCore.QFile(filename[0])
            if fileopen.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
                data = json.loads(fileopen.readAll().data().decode('utf-8'))
                print(data)
                self.scene.clear()
                self.scene.data_to_items(data)
                self.file=fileopen
                print("File opened !")
                self.statusBar().showMessage("File Opened")
            else :
                print("Can't open this file !")
                self.statusBar().showMessage("Can't open this file !")

            fileopen.close()
        

    def file_save(self):
        if(self.file):
            if self.file.open(QtCore.QIODevice.WriteOnly):
                data=self.scene.items_to_data()
                print(data)
                self.file.write(json.dumps(data).encode("utf-8"))
                self.file.close()
                print("File saved !")
                self.statusBar().showMessage("File Saved")
            else :
                print("Can't save this file !")
                self.statusBar().showMessage("Can't save this file !")
        else:
            filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', os.getcwd())
            if len(filename[0])>0:
                if(filename[0][len(filename[0])-5:]==".json"):
                    file=filename[0]
                else:
                    file=filename[0]+".json"
                filesave=QtCore.QFile(file)
                if filesave.open(QtCore.QIODevice.WriteOnly):
                    data=self.scene.items_to_data()
                    print(data)
                    filesave.write(json.dumps(data).encode("utf-8"))
                    filesave.close()
                    self.file=filesave
                    print("File saved !")
                    self.statusBar().showMessage("File Saved")
                else :
                    print("Can't save this file !")
                    self.statusBar().showMessage("Can't save this file !")


    def file_save_as(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File As', os.getcwd())
        # print(filename[0][len(filename[0])-5:])
        if len(filename[0])>0:
            if(filename[0][len(filename[0])-5:]==".json"):
                file=filename[0]
            else:
                file=filename[0]+".json"
            filesave=QtCore.QFile(file)
            if filesave.open(QtCore.QIODevice.WriteOnly):
                data=self.scene.items_to_data()
                print(data)
                filesave.write(json.dumps(data).encode("utf-8"))
                filesave.close() 
                self.file=filesave
                print("File saved !")
                self.statusBar().showMessage("File Saved")
            else :
                print("Can't save this file !")
                self.statusBar().showMessage("Can't save this file !")

    def pen_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self )
        if color.isValid() :
            print("Color Chosen : ",color.name())
            self.scene.set_pen_color(color)
        else :
            print("color is not a valid one !")

    def brush_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self )
        if color.isValid() :
            self.scene.set_brush_color(color)
            print("Color Chosen : ",color.name())
        else :
            print("color is not a valid one !")

    def font_selection(self):
        (font, ok) = QtWidgets.QFontDialog.getFont(QtGui.QFont("serif", 11), self )
        print(ok)
        if ok:
            print("Font Chosen : ")
            self.scene.set_font(font)
        else:
            print("Serif 11 is chosen by default")


    def help_about_us(self):
        QtWidgets.QMessageBox.information(self, self.tr("About Us"),
                                self.tr("Corentin Régné et Lénaël Jagline\n copyright ENIB 2020"))
    def help_about_qt(self):
        QtWidgets.QMessageBox.information(self, self.tr("About Qt"),
                                self.tr("Qt is a visual module for C++ and Python"))
    def help_about_app(self):
        text=open('README.txt').read()
        QtWidgets.QMessageBox.information(self, self.tr("About the Application"),
                            self.tr(text))



    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

if __name__ == "__main__" :  
    print(QT_VERSION_STR)
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.installEventFilter(main)
    sys.exit(app.exec_())
