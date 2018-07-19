# coding: utf-8

############################
# This configuration file sets various parameters for generation of training
# set file & evalutation of results
############################
# from gui1 import scorernameq
# myconfig.py:

########################################
# Step 1:
########################################

Task = 'programming'

# Filename and path to behavioral video:
vidpath = '.'

filename = 'None'

cropping = False

# ROI dimensions / bounding box (only used if cropping == True)
# x1,y1 indicates the top left corner and
# x2,y2 is the lower right corner of the croped region.

x1 = 0
x2 =  0
y1 =  0
y2 =  0

# Portion of the video to sample from in step 1. Set to 1 by default.
portion = 1

########################################
# Step 2:
########################################

# Exact sequence of labels as were put by annotator in *.csv file
bodyparts = ["Right Ear", "Left Ear"]

# who is labeling?
Scorers = ['Rel']

# Set this true if the data was sequentially labeled and if there is one file per folder (you can set the name of this file below, i.e. multibodypartsfilename)
# Otherwise there should be individual files per bodypart, i.e. in our demo case hand.csv, Finger1.csv etc.
# If true then those files will be generated from Results.txt
multibodypartsfile = True 
multibodypartsfilename = 'CollectedData_Mackenzie.csv'

# When importing the images and the labels in the csv/xls files should be in the same order!
# During labeling in Fiji one can thus (for occluded body parts) click in the origin of the image 
#(i.e. top left corner (close to 0,0)), these "false" labels will then be removed. To do so set the following variable:
#set this to 0 if no labels should be removed!If labels are closer to origin than this number they are set to NaN (not 
# a number). Please adjust to your situation. Units in pixel. 
invisibleboundary=10 

########################################
# Step 3:
########################################

date = 'Jul16'
scorer = 'Rel'

# Userparameters for training set. Other parameters can be set in pose_cfg.yaml

# Ids for shuffles, i.e. range(5) for 5 shuffles
Shuffles = [1] 

# Fraction of labeled images used for training
TrainingFraction = [0.95]  

# Which resnet to use
# (these are parameters reflected in the pose_cfg.yaml file)
resnet = 50

# How often to save the trained network's progress
trainingsiterations = '5000'

# For Evaluation/ Analyzing videos
# To evaluate the last model that was trained most set this to: -1 
# To evaluate all models (training stages) set this to: "all"  (as string!)

snapshotindex = -1 #"all"
shuffleindex = 0

# likelihood. RMSE will be reported for all pairs and pairs with larger likelihood than pcutoff (see paper). This cutoff will also be used in plots.
pcutoff=.1

#If true will plot train & test images including DeepLabCut labels next to human labels. Note that this will be plotted for all snapshots as indicated by snapshotindex
plotting=True 
