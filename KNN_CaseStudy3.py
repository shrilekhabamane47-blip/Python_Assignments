# X[2,5,6,1] -->hours of study
# Y[60,80,85,50]-->Attendance
#  [F,P,P,F]

from math import sqrt
import numpy as np

def Euclidean(P1,P2):
    Ans= sqrt((P1['X']-P2['X'])**2+(P1['Y']-P2['Y'])**2)
    return Ans

def Predictor():
    border = "-"*50
    Data = [
                {'X': 2 ,'Y' : 60, 'label':'Fail'} ,
                {'X': 5 ,'Y' : 80, 'label':'Pass'} ,
                {'X': 6 ,'Y' : 85, 'label':'Pass'},
                {'X': 1 ,'Y' : 50, 'label':'Fail'} 
            ]   
    new_point ={'X' :4 , 'Y' :70}

    print(border)
    print("Dataset given for Training")
    print(border)

    for i in Data:
        print(i)
    print(border)

    for d in Data:
        d['distance'] = Euclidean(d,new_point)

    print(border)
    print("Traning dataset according to euclidean distance")
    print(border)

    for d in Data:
        print(d)
    sorted_data = sorted(Data,key =lambda item : item['distance'] )
    
    print(border)
    print("Sorted Traning dataset according to euclidean distance")
    print(border)

    for d in sorted_data:
        print(d)
    

    k=5
    nearest = sorted_data[:k]

    print(border)
    print("Nearest elements ")
    print(border)

    for d in nearest:
        print(d)
    print(border)

    vote={}
    for neighbour in nearest:
        label=neighbour['label']
        vote[label]=vote.get(label,0)+1

    print(border)
    for d in vote:
        print("Result:",d,"count of grade :",vote[d])
    print(border)

    predicted_class = max(vote,key=vote.get)
    print(border)
    print("Predicted result for (4,70) is",predicted_class)
    print(border)

def main():
    Predictor()
if __name__ =="__main__":
    main()