import math
import sys

#The following code builds the naive Bayes model from the training data

def dic_builder(class1,class2,line_words,model,class_count):
     if not(class1 in class_count.keys()):
          class_count[class1]=0 #Initialising class1 count
     if not(class2 in class_count.keys()):
          class_count[class2]=0 #Initialising class2 count
     class_count[class1]+=1
     class_count[class2]+=1
     try:
          class_dic=model[class1]
     except:
          model[class1]={} #initializing the model for class1
     try:
          class_dic=model[class2]
     except:
          model[class2]={} #initializing the model for class2
     for word in line_words:# calculating the count of each word under each class 
          word=''.join(char for char in word if char.isalnum())
          word=word.lower()
          try:
               count=model[class1][word]
               model[class1][word]+=1
          except:
               model[class1][word]=1
          try:
               count=model[class2][word]
               model[class2][word]+=1
          except:
               model[class2][word]=1
          
def smoothing(model,features,model_prob,class_count):
     tot_count={}
     for classes in model.keys():
          tot_count[classes]=0
          for feat in features: #Using Laplace smoothing to smoothen the probabilities
               try:
                    count=model[classes][feat]
                    model[classes][feat]+=1
               except:
                    model[classes][feat]=1
               tot_count[classes]+=model[classes][feat]
     for classes in model.keys():
          model_prob[classes]={}
          for word,count in model[classes].items():
               model_prob[classes][word]=float(count)/tot_count[classes]
     full_count=0
     file_write=open('nbmodel.txt','w')
     for class_items in class_count.keys():
          full_count+=class_count[class_items]
     for class_items in class_count.keys():
          file_write.write(class_items+' '+str(float(class_count[class_items])/full_count)+'\n') #writing the class probabilities
     for classes in model_prob.keys():
          class_dic=model_prob[classes]
          for word in class_dic.keys():
               file_write.write(word+' '+classes+' '+str(class_dic[word])+'\n') #writing the feature the probabilities

#Reading the input file
def read_file(file_name):
     file_content=open(file_name,'r')
     model=dict()
     model_prob=dict()
     class_count=dict()
     c=0
     for line in file_content: #reading every line from the input file and processing the every line
          line_words=line.split()
          dic_builder(line_words[1],line_words[2],line_words[3:],model,class_count)
     features=[]
     for classes in model.keys():
          class_dic=model[classes]
          for words in class_dic.keys():
               features.append(words)
     features=set(features)
     smoothing(model,features,model_prob,class_count)

read_file(sys.argv[1])     

