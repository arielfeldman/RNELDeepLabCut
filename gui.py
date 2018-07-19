# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'track.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Ui_MainWindow(object):
    __attributes__ = ['_scorername', '_date', '_task', '_vidtype', '_bodyparts',\
                        '_cropping', '_dataset', '_trainingvid', '_analysisvid',\
                        '_mode']

    def __init__(self):
        for attr in self.__attributes__:
                exec("self." + attr + " = None")
        self._mode = "Generating"

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 429)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gscorer = QtWidgets.QLineEdit(self.centralwidget)
        self.gscorer.setText("Rel")
        self.gscorer.setObjectName("gscorer")
        self.verticalLayout_2.addWidget(self.gscorer)
        
        spacerItem5 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.gdate = QtWidgets.QLineEdit(self.centralwidget)
        self.gdate.setText("Jul16")
        self.gdate.setObjectName("gdate")
        self.verticalLayout_2.addWidget(self.gdate)
        
        spacerItem6 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.gtask = QtWidgets.QLineEdit(self.centralwidget)
        self.gtask.setText("programming")
        self.gtask.setObjectName("gtask")
        self.verticalLayout_2.addWidget(self.gtask)
        
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.gvid_type = QtWidgets.QLineEdit(self.centralwidget)
        self.gvid_type.setObjectName("gvid_type")
        self.gvid_type.setText("mp4")
        self.verticalLayout_2.addWidget(self.gvid_type)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.gbodyparts = QtWidgets.QLineEdit(self.centralwidget)
        self.gbodyparts.setText('\"'+"Right Ear"+'\", \"'+"Left Ear"+'\"')
        self.gbodyparts.setObjectName("gbodyparts")
        self.verticalLayout_3.addWidget(self.gbodyparts)
        
        spacerItem9 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.gcrop = QtWidgets.QLineEdit(self.centralwidget)
        self.gcrop.setText("0, 0, 0, 0")
        self.gcrop.setObjectName("gcrop")
        self.verticalLayout_3.addWidget(self.gcrop)
        
        spacerItem10 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.gdataset = QtWidgets.QPushButton(self.centralwidget)
        self.gdataset.setObjectName("gdataset")
        self.verticalLayout_3.addWidget(self.gdataset)
        
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.gtrain_vid_file = QtWidgets.QPushButton(self.centralwidget)
        self.gtrain_vid_file.setObjectName("gtrain_vid_file")
        self.verticalLayout_3.addWidget(self.gtrain_vid_file)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.ganalysis_vid_file = QtWidgets.QPushButton(self.centralwidget)
        self.ganalysis_vid_file.setObjectName("ganalysis_vid_file")
        self.verticalLayout.addWidget(self.ganalysis_vid_file)
        
        spacerItem13 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.gtraining_iter = QtWidgets.QLineEdit(self.centralwidget)
        self.gtraining_iter.setObjectName("gtraining_iter")
        self.gtraining_iter.setText("5000")
        self.verticalLayout.addWidget(self.gtraining_iter)
        
        spacerItem14 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem14)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gmode_select = QtWidgets.QComboBox(self.centralwidget)
        self.gmode_select.setObjectName("gmode_select")
        self.gmode_select.addItem("")
        self.gmode_select.addItem("")
        self.gmode_select.addItem("")
        self.verticalLayout.addWidget(self.gmode_select)
        
        spacerItem15 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.gleggo = QtWidgets.QPushButton(self.centralwidget)
        self.gleggo.setObjectName("gleggo")
        self.verticalLayout.addWidget(self.gleggo)
        self.horizontalLayout.addLayout(self.verticalLayout)
        
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem16)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_4)
        
        self.connect4()
        self.gleggo.clicked.connect(self.run)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def connect4(self):

        self.gdataset.clicked.connect(self.datasetSlot)
        self.gtrain_vid_file.clicked.connect(self.trainingVidSlot)
        self.ganalysis_vid_file.clicked.connect(self.analysisVidSlot)
        self.gmode_select.currentIndexChanged.connect(self.modeSlot)

    def run(self):
        """
        Upon hitting "Let's Go!", the user configurations are passed to the configuration
        file, and the selected mode is run.
        """
        # print(self._mode)
        
        # Setting the attributes of the session in the MainWindow() class
        if (self._mode == "Training") or (self._mode == "Generating"):
            
            self._scorername = str(self.gscorer.text())
            print("Scorer:",self._scorername)

            self._date = str(self.gdate.text())
            print("Label Date:", self._date)
            
            self._task = str(self.gtask.text())
            print("Task:", self._task)

            self._bodyparts = str(self.gbodyparts.text())
            print("Items to Track:", self._bodyparts)

            self._cropping = str(self.gcrop.text())
            if self._cropping == "0, 0, 0, 0":
                print("No cropping")
            else:
                print("Cropping Coordinates:", self._cropping)
            
            self._trainingsiters = str(self.gtraining_iter.text())
            print("Save Iterations:", self._trainingsiters)

            if (self._mode == "Training"):
                print("Dataset Location:", str(self._dataset))
            
            print("Training Video File:", str(self._trainingvid))

            # Rewriting the lines in the training configuration file in place
            with open('myconfig.py', 'r') as f:
                instr = f.readlines()
            
            instr[42] = "Scorers = ['" + str(self._scorername) + "']\n"
            instr[62] = "scorer = '" + str(self._scorername) + "'\n"
            
            instr[61] = "date = '" + str(self._date) + "'\n"
            
            instr[13] = "Task = '" + str(self._task) +"'\n"

            instr[39] = "bodyparts = [" + str(self._bodyparts) + "]\n"

            if self._cropping == "0, 0, 0, 0":
                instr[20] = "cropping = False"+ "\n"
            else:
                instr[20] = "cropping = True"+"\n"
            instr[26] = "x1 = " + self._cropping.split(",")[0] +"\n"
            instr[27] = "x2 = " + self._cropping.split(",")[2] +"\n"
            instr[28] = "y1 = " + self._cropping.split(",")[1] +"\n"
            instr[29] = "y2 = " + self._cropping.split(",")[3] +"\n"

            if (self._mode == "Training"):
                instr[48] = "multibodypartsfilename = '" + str(self._dataset.split("/")[-1])+"'\n"

            instr[18] = "filename = '" + str(self._trainingvid) + "'\n"

            instr[77] = "trainingsiterations = " + str(self._trainingsiters) + "\n"
            
            with open('myconfig.py', 'w') as f:
                f.writelines(instr)
            print("User configurations set!")

            os.chdir("Generating_a_Training_Set")

            if self._mode == "Generating":
                os.system("python Step1_SelectRandomFrames_fromVideos.py")

            elif self._mode == "Training":
                os.system("python Step2_ConvertingLabels2DataFrame.py")
                os.system("python Step3_CheckLabels.py")
                os.system("python Step4_GenerateTrainingFileFromLabelledData.py")
                os.system("cp -R "+ str(self._task)+ str(self._date)+"-trainset95shuffle1 ../pose-tensorflow/models/")
                os.system("cp -R UnaugmentedDataSet_"+ str(self._task) + str(self._date)+"/ ../pose-tensorflow/models/")
                os.chdir("../pose-tensorflow/models/pretrained/")
                os.system("./download.sh")
                os.chdir("../"+str(self._task) + str(self._date)+"-trainset95shuffle1/train")
                os.system("TF_CUDNN_USE_AUTOTUNE=0 CUDA_VISIBLE_DEVICES=0 python ../../../train.py")

        elif self._mode == "Analysis":
            
            print("entered analysis")
            a_folder = ""
            
            self._vidtype = str(self.gvid_type.text())
            print("Type of Videos to Analyze:", self._vidtype)

            self._scorername = str(self.gscorer.text())
            print("Scorer:",self._scorername)

            self._date = str(self.gdate.text())
            print("Label Date:", self._date)
            
            self._task = str(self.gtask.text())
            print("Task:", self._task)

            self._cropping = str(self.gcrop.text())
            if self._cropping == "0, 0, 0, 0":
                print("No cropping")
            else:
                print("Cropping Coordinates:", self._cropping)

            print("Dataset Location:", str(self._dataset))

            self._trainingsiters = str(self.gtraining_iter.text())
            print("Save Iterations:", self._trainingsiters)
            
            for directory in self._analysisvid.split("/")[0:-1]:
                a_folder += str(directory)+"/"
            print("Analysis Video Folder:", str(a_folder))

            # Rewriting the lines in the analysis configuration file in place
            with open('myconfig_analysis.py', 'r') as f:
                instr = f.readlines()
            
            instr[8] = "videofolder = '" + a_folder + "'\n"

            instr[12] = "videotype = '." + str(self._vidtype) + "'\n"
            
            instr[30] = "scorer = '" + str(self._scorername) + "'\n"
            
            instr[31] = "Task = '" + str(self._task) +"'\n"

            instr[32] = "date = '" + str(self._date) + "'\n"

            if self._cropping == "0, 0, 0, 0":
                instr[9] = "cropping = False"+ "\n"
            else:
                instr[9] = "cropping = True"+"\n"
            instr[23] = "x1 = " + self._cropping.split(", ")[0] +"\n"
            instr[24] = "x2 = " + self._cropping.split(", ")[2] +"\n"
            instr[25] = "y1 = " + self._cropping.split(", ")[1] +"\n"
            instr[26] = "y2 = " + self._cropping.split(", ")[3] +"\n"

            instr[43] = "trainingsiterations = '" + str(self._trainingsiters) + "'\n"
            
            with open('myconfig_analysis.py', 'w') as f:
                f.writelines(instr)
            print("User configurations set!")

            os.chdir("Evaluation-Tools/")
            print(os.getcwd())
            os.system("python Step1_EvaluateModelonDataset.py")
            os.system("python Step2_AnalysisofResults.py")
            os.system("CUDA_VISIBLE_DEVICES=0 python AnalyzeVideos.py")
            os.system("python MakingLabeledVideo.py")            

    def datasetSlot(self):

        self._dataset = QtWidgets.QFileDialog.getOpenFileName()[0]

    def trainingVidSlot(self):

        self._trainingvid = QtWidgets.QFileDialog.getOpenFileName()[0]

    def analysisVidSlot(self):
        
        self._analysisvid = QtWidgets.QFileDialog.getOpenFileName()[0]

    def modeSlot(self):

        self._mode = str(self.gmode_select.currentText())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RNEL's DeepLabCut"))
        self.label_8.setText(_translate("MainWindow", "Note: Scorer, Label Date and Task Name must match the inputs written prior to training of the network!"))
        self.label_3.setText(_translate("MainWindow", "Scorer:"))
        self.label_4.setText(_translate("MainWindow", "Label Date:"))
        self.label_5.setText(_translate("MainWindow", "Task Name:"))
        self.label_10.setText(_translate("MainWindow", "Video Type:"))
        self.label_6.setText(_translate("MainWindow", "Items to Track:"))
        self.label_7.setText(_translate("MainWindow", "Cropping Coordinates:"))
        self.label_9.setText(_translate("MainWindow", "Labeled Dataset:"))
        self.label_2.setText(_translate("MainWindow", "Training Video File:"))
        self.label_11.setText(_translate("MainWindow", "Analysis Video Folder:"))
        self.label_12.setText(_translate("MainWindow", "Training Iterations:"))
        self.label.setText(_translate("MainWindow", "Training or Analysis?"))
        self.gmode_select.setItemText(0, "Generating")
        self.gmode_select.setItemText(1, _translate("MainWindow", "Training"))
        self.gmode_select.setItemText(2, _translate("MainWindow", "Analysis"))
        self.gleggo.setText(_translate("MainWindow", "Let\'s Go!"))
        self.gtrain_vid_file.setText("Click Me!")
        self.gdataset.setText("Click Me!")
        self.ganalysis_vid_file.setText("Click Me!")
        MainWindow.setWindowIcon(QtGui.QIcon('rnel.png'))

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)    
MainWindow.show()
sys.exit(app.exec_())

