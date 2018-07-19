# RNEL's DeepLabCut

An adaptation of Mathis et al's [DeepLabCut](https://github.com/AlexEMG/DeepLabCut), a more detailed explanation of which can be found below:

"[Markerless tracking of user-defined features with deep learning](https://arxiv.org/abs/1804.03142v1)" by Alexander Mathis, Pranav Mamidanna, Taiga Abe, Kevin M. Cury, Venkatesh N. Murthy, Mackenzie W. Mathis* and Matthias Bethge*

This package is simply a python GUI wrapper around an earlier version of DeepLabCut, with slightly modified code, that can be run from an Ubuntu terminal, as well as a post-processing analysis tutorial in jupyter notebook. We assume python 3.x and pip3.

# What Can the GUI Handle?:

Generating vs. Training vs. Analysis: 

This GUI simplifies the process of editing the configuration files, for users less familiar with the Python language. Included is a notebook demonstrating a possible post-processing method to generate figures and videos labeled with matplotlib. The recommended general pipeline for first time use, from the developers of DeepLabCut, is:

**Install --> Extract frames -->  Label training data -->  Train DeeperCut feature detectors -->  Apply your trained network to unlabeled data -->  Extract trajectories for analysis.**

The **Generating** mode will extract a user configured number of frames from the training video. Likewise, the **Training** mode will train the feature detectors adapted from DeeperCut, and the **Analysis** mode will both apply the trained network to unlabeled data and extract trajectories for analysis. The GUI does not, however, install the required libraries for you (as listed below), nor does it handle the labeling of data, which may be done using Fiji and shall be detailed later.

# Installation and Library Requirements:

- Hardware:
     - Computer: For reference, we use Ubuntu 16.04 LTS and run a docker container that has TensorFlow, etc. installed (*available in a future release). One should also be able to run the code in Windows or MacOS (but we never tried). You will need a strong GPU such as the [NVIDIA GeForce 1080 Ti](https://www.nvidia.com/en-us/geforce/products/10series/geforce-gtx-1080/).
     
- Software: 
     - You will need [TensorFlow](https://www.tensorflow.org/) (we used 1.0 for figures in papers, later versions also work with the provided code (we tested **TensorFlow versions 1.0 to 1.4**, but recommend **1.0**, ses below) for Python 3 with GPU support (otherwise training and running is extremely slow). Please check your CUDA and [TensorFlow installation](https://www.tensorflow.org/install/) with this line (below), and you can test that your GPU is being properly engaged with these additional [tips](https://www.tensorflow.org/programmers_guide/using_gpu).

      $ sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

Please also install:

     - Install Sypder (or equivalent IDE) and/or Jupyter Notebook
     - Clone (or download) the code we provide
     - You will also need to install the following Python packages (in the terminal type):

      $ pip install scipy scikit-image matplotlib pyyaml easydict 
      $ pip install moviepy imageio tqdm tables
      $ pip install pyqt5
      $ git clone https://github.com/arielfeldman/RNELDeepLabCut

# Instructions on Training a Network and Analyzing Videos:

**(0) Configuration of your project:**
Run the GUI from the Ubuntu terminal and set the global variables for your dataset. The variables that must be configured differ based on the mode the GUI is being run in (Generating, Training or Analysis), and thus will be detailed in those sections of this guide. Below is an example of how RNEL's DeepLabCut interface should appear.

<p align="center">
<img src="/gui_RNELlabel.png" width="60%">
</p>

- Scorer specifies the name of whomever has labeled the data to be used in training. This is helpful to specify networks after multiple have been stored. The same scorer must be specified when referencing an earlier network as was used when creating the network.

- Label Date specifies the day the data was generated. This must also be maintained, both in content and in format (i.e. Jul16 vs. 07-16) when referencing an earlier network, but upon initiation (generating a dataset) can be input as any form the user would prefer.

- Task specifies the activity the animal in the video is engaging in that is being analyzed, such as rotating or foraging. Once again, this must be preserved to access an earlier network, but may always be configured to the user's liking to build a new network.

- Video Type specifies the type of videos in the Video Analysis folder the user wants to analyze (mp4, avi, etc.). This input is only required for the **Analysis** mode.

- Items to Track specifies the body parts or items the user would like to train the network to recognize, in the format of body parts/items each in quotes, separated by comas. The order in which they are listed must be preserved in labeling (i.e. if there are 7 body parts, every click *x* in which *x*%7=1 should be the first body part in the list, and so on) as well as when using the **Training** mode on a generated dataset.

- Cropping Coordinates specifies a region of interest of the frames which captures all of the activity the user would like to train on and analyze. This defaults to no cropping. However, if cropping is required, enter the coordinates in the following format: 
>*x<sub>1</sub>*, *y<sub>1</sub>*, *x<sub>2</sub>*, *y<sub>2</sub>*

- Labeled Dataset specifies where the .csv file generated after labeling (explained in Step 2) is located. This is required for the **Training** mode only.

- Training Video File specifies where the video from which the dataset is made is located. This is required for both the **Generating** and **Training** modes.

- Analysis Video Folder specifies the folder in which all the videos the user wants to analyze are located. Be warned, all videos with a give codec (as specified with the Video Type input) in the chosen folder shall be analyzed and labeled. Click any arbitrary file within the analysis folder to specify - all videos shall still be analyzed, given their codec. This is required only for the **Analysis** mode.

- Training Iterations specifies several different things, depending on mode.

>First, in the **Generating** mode, training iterations specifies how many frames from the training video to select while building a dataset. 

>In the **Training** mode, training iterations will determine how often to update the progress of the network as it is training. By default, this is configured to every 5000 steps, which was useful in our experience. This would lead to a span of 20000 steps being save at any given time (since only about 4 networks are saved at any given time - newer ones are rewriting over ones 5 saves before). 

>In the **Analysis** mode, training iterations specifies the network to use during analysis - i.e., if one had stopped training at 165,000 steps and wanted to use the most trained of the networks used, they would input 165000 in this area. However, if one felt the network was overtrained and wanted to compare performance to an earlier version, one may set this number to 145000 (assuming the training iterations was set to 5000 during training, this would be the least trained network saved on the task).

**(1) Selecting data to label:** 
In efforts to create a diverse and representative training set in all aspects, selecting the Generating mode will randomly select a user configured number of frames from across the entire training video(s) in a uniform manner. The number of frames (and thus the size of the dataset to label) should be configured in the input line entitled: "Training Iterations".
            
**(2) Label the frames:**

   - You should label a sufficient number of frames with the anatomical locations of your choice. Depending on your required accuracy and the nature of the scene statistics more training data might be necessary. Try to label consistently similar spots (e.g. on wrist that is very large, try to label the same location).
     
   - Labeling can be done in any program, but we recommend using [Fiji](https://fiji.sc/). In Fiji one can simply open the images, create a (virtual) stack* (in brief, in fiji: File > Import > Image Sequence, then use the "Multi-point Tool" to label frames. You scroll through the frames and click on as many points as you wish in the same order on each frame. Then simply measure and save the resulting .csv file (Analyze>Measure (or simple Ctrl+M)). 

   - Our GUI assumes you store one .csv file per folder that contains all body parts in a cyclical way (same, repeating order). If a particular body part is not visible in a frame, then click close to (0,0) to later exclude those labels. Furthermore, make sure that the sequence of body parts entered in the GUI has exactly the same order as the cyclically labeled body parts.

**(3) Using the Training Mode:**

 By running the **Training** mode, and having specified the inputs detailed above, a data structure in [pandas](https://pandas.pydata.org/) (stored as .h5 and .csv) combining the various labels together with the (local) file path of the images is created. Keep in mind that ".csv" files input to the GUI should exist in a folder alongside the individual images.
     
 Next, labels are generated for the input dataset, based off of the .csv file. This allows the user to check and ensure that they have labeled correctly, or make corrections as needed.

 The labeled data is then split into test and train sets for benchmarking. This step will create a ".mat" file, which is used by DeeperCut as well as a ".yaml" file containing meta information with regard to the parameters of the DeeperCut. A folder with the training data as well as a folder for training the corresponding model in DeeperCut will both be created here. 

An earlier, minimal yet sufficient for our purposes variant of [DeeperCut](https://github.com/eldar/pose-tensorflow) is implemented for the training portion, which has been tested for **TensorFlow 1.0** (recommended). All features other than simultaneous evaluation for multiple snapshots (`Step1_EvaluateModelonDataset.py`) work for **TensorFlow** versions up to **1.4**. 

Then, training begins!

Tip from the developers of DeepLabCut: You can also stop during a training, and restart from a snapshot (aka checkpoint):
Just change the init_weights term, i.e. instead of "init_weights: ../../pretrained/resnet_v1_50.ckpt"  put "init_weights: ./snapshot-insertthe#ofstepshere" (i.e. 10,000). Train for several thousands of iterations until the loss plateaus.

>This, however, requires modifying the code, but is not too difficult for those inexperienced with python. Within the pose_cfg.yaml (located from GUI location at "pose-tensorflow/models/TaskDate-trainset95shuffle1/train/pose\_cfg.yaml"), find the line that says "init\_weights: ../../pretrained/resnet\_v1\_50.ckpt", and change this to reflect the number of iterations when you stopped training, rounded down to the nearest multiple of training iterations you set. For example, if one had set training iterations equal to 5000 and had stopped training at 169000, they would set the number of steps for the snapshot to 165000.

**(4) Analysis Mode:**
     
The performance of the trained network on the whole data set (train and test images) will be quantified when using **Analysis** mode.
 
After successfully training and finding low generalization error for the network, one may extract labeled points and poses from all videos in the user specified Analysis Videos Folder and plot them above frames. Of course one can use the extracted poses in many other ways.

# Support:

If you are having issues regarding the user interface, please let us know by contacting [Ariel.K.Feldman@rice.edu] for help. For questions on DeepLabCut's development, feel free to reach out to: [alexander.mathis@bethgelab.org] or [mackenzie@post.harvard.edu]