import sys

#The following function predicts the classes of the sentence using the naive bayes model
def calc_class(line_words,class_prob,model):
    final_val={}
    for class_ in class_prob.keys():
        val=class_prob[class_]
        for word in line_words: #Calculates the total probablity of each line under both the classes
            word=''.join(char for char in word if char.isalnum())
            word=word.lower()
            try:
                val+=model[class_][word]
            except:
                continue
        final_val[class_]=val
    my_list=[]
    #predicting the classes based on the total probability
    if final_val["Fake"]>final_val["True"]:
        my_list.append("Fake")
    else:
        my_list.append("True")
    if final_val["Pos"]>final_val["Neg"]:
        my_list.append("Pos")
    else:
        my_list.append("Neg")
    return my_list

def read_file(file_name):
    file_name_model='nbmodel.txt'
    file_content=open(file_name_model,'r')
    class_prob=dict()
    model=dict()
    for line in file_content: #the probabilities from the model file
        data=line.split()
        if len(data)<3:
            class_prob[data[0]]=float(data[1])
        else:
            if not(data[1] in model.keys()):
                model[data[1]]={}
            model[data[1]][data[0]]=float(data[2])
    file_write=open('nboutput.txt','w')
    file_content=open(file_name,'r')
    for line in file_content: #reading and processing every line from the test file
          line_words=line.split()
          my_list=calc_class(line_words[1:],class_prob,model)
          file_write.write(line_words[0]+' '+my_list[0]+' '+my_list[1]+'\n') #writing the predicted classes in the output file
#read_file("dev-text.txt")
read_file(sys.argv[1])
