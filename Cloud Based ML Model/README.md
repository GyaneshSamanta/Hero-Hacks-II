# Stray Animal Detection Model

## Setup

    1. Open the `TFOD API for Stray Detection.ipynb` file in Google Colab. 
    2. Ensure you have a GCP account and create a project named "fast-ai-exploration". 
    3. In the section titled, "Set up GCP Utilities" add in your GCP account details.
    4. Switch over to your Colab Notebook and click on the "Connect" button to allocate resources to your notebook.
    5. By default you should be allocated around 14 GB of RAM and 107GB of disk space. 
    6. Wait for the installation of required packages in the initial cells. 
    Now you're all setup to test the model on your own

## Understanding the Model

In the first section titled "TFOD API", we use a Tensorflow object detection model API.
The following section "Gather Pets dataset and prepare it" we download the dataset from ``www.robots.ox.ac.uk``.
"Set up GCP Utilities is where we initialize a GCP project, titled "fast-ai-exploration" in this case and create a storage bucket to store our data. 
Once we have created the bucket we set the compute zone location (preferably to the same location as where our storage bucket is created, it allows for faster access).
The following directory structure is recommended for training and evaluation of our model by TFOD API. 
[Directory Structure](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_training_and_evaluation.md#recommended-directory-structure-for-training-and-evaluation)  

Once we have the directory in order, we can now move to kickstart the model training. 
First thing we do is to set our Model directory. Once that is setup, you can navigate to the logs viewer in GCP to ensure that the model directory was set correctly.
You can monitor the same on TensorBoard within your colab notebook. 
Once you are happy with the results of our model you can export the model to "SavedModel" Format. This exports the checkpoints as a SavedModel locally.