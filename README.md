# EEG-Emotion-classification

# PROBLEM S TATEMENT
It is difficult to look at the EEG signal and identify the state of Human mind. In this assign-
ment, the SVM classifier is trained with Deap dataset to predict the state of mind. the state of
mind is predicted in terms of valence, arousal. which can further be used to predict the state
of mind in terms of expression.
# PROCEDURE TO SOLVE THE ABOVE PROBLEM
In this assignment, the preprocessed data is used for training the classifier.
Steps involve in training the dataset:-
1. Extracting the dataset
2. Finding the features
3. Reducing the dimension
4. traning the vector
5. checking the classifier efficiency
## EXTRACTING THE DATASET
The DEAP dataset consists of two parts:
1. The ratings from an online self-assessment where 120 one-minute extracts of music
videos were each rated by 14-16 volunteers based on arousal, valence and dominance.
2. The participant ratings, physiological recordings and face video of an experiment where
32 volunteers watched a subset of 40 of the above music videos. EEG and physiological
signals were recorded and each participant also rated the videos as above.
In this assignment, labels are extracted into separate file and data of each channel is extracted
into separate file. data from each channel is stored in row wise versus time in column for each
trail,per person
## FINDING THE FEATURES
In this assignment, Wavelet transform is used to decompose the each channel data into the
five feature i.e
• Delta (< 4 Hz)
• Theta (4-7 Hz)
• Alpha (8-15 Hz)
• Beta (16-31 Hz)
• Gamma (> 32 Hz)
In this assignment, obtained the 7 decomposed values but we negalted the frequency whose
range is in 0-0.5 Hz so that the artifcats are removed. The frequency whose range is near 50
Hz are removed to reduce the effect of power line on signals. finally, EEG band are obtained
for each channel.
## REDUCING THE DIMENSION
The dimension can be reduced using one of the below mention method:-
1. Standard Deviation
2. Mean
3. Variance
4. Median
But in this assignment Standard Deviation is used because it describe the devaition of each
EEG Band power density properly given by the equation below.
## TRANING THE VECTOR
In this assignment, the classifier used is Support vector machine (SVM). we can also use other
classifier or neural network to predict the values but the training efficiency is found to be
nearly 98 percentage with SVM.
