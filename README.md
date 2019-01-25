# Naive-Bayes-Classifier
Naive Bayes classifier to identify hotel reviews as either true or fake, and either positive or negative
There are two programs which needs to be run sequentially
Step 1
nblearn.py 
This will learn a naive Bayes model from the training data
Training data format
The first 3 tokens in each line are:
- a unique 7-character alphanumeric identifier
- a label True or Fake
- a label Pos or Neg
- These are followed by the text of the review.
- example: "064BmtQ Fake Neg I was very disappointed with this hotel"
Command to run the file
> python nblearn.py /path/to/input

Step 2
nbclassify.py 
This will use the model to classify new data
The classification program will be invoked in the following way:
> python nbclassify.py /path/to/input

The argument is a single file containing the test data file; the program will read the parameters of a naive Bayes model from the file nbmodel.txt, classify each entry in the test data, and write the results to a text file called nboutput.txt
