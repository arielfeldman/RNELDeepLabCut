# coding: utf-8

############################
# This configuration file sets various parameters for running a trained model,
# that performed well on train/test set on videos
############################

# Filename and path to behavioral video (for labeling)
videofolder = '/home/kemerelab/DeepLabCut/videos/'
cropping = False

#type of videos to analyze
videotype = '.mp4'

#Note: under the hood there is moviepy, which can handle many types of videos:
#https://zulko.github.io/moviepy/_modules/moviepy/video/io/VideoFileClip.html

# If you have stacks of tiffs (instead of videos) you can use "AnalyzeABunchofPictures.py"

# ROI dimensions / bounding box (only used if cropping == True)
# x1,y1 indicates the top left corner and
# x2,y2 is the lower right corner of the cropped region.

x1 = 0
x2 = 0
y1 = 0
y2 = 0

# Analysis Network parameters:

scorer = 'Rel'
Task = 'programming'
date = 'Jul16'

# Fraction of labeled images used for training
trainingsFraction = 0.95

resnet = 50
snapshotindex = -1
shuffle = 1

# For plotting:
# type the number listed in .pickle file
trainingsiterations = '5000'

# likelihood cutoff for body part in image
pcutoff = 0.1

# delete individual (labeled) frames after making video?
deleteindividualframes = True
dotsize = 5
colormap = 'cool'

# "strength/transparency level of makers" in individual frames (Vary from 0 to 1. )
alphavalue=.5 
