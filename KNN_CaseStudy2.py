#  [A,B,C,D]
# X[1,2,3,6]
# Y[2,3,1,5]
#  [R,R,B,B]

from math import sqrt
import numpy as np

def Euclidean(P1,P2):
    Ans= sqrt((P1['X']-P2['X'])**2+(P1['Y']-P2['Y'])**2)
    return Ans

def Predictor():
    border = "-"*50
    Data = [
                {'Point' : 'A', 'X': 1 ,'Y' : 2, 'label':'Red'} ,
                {'Point' : 'B', 'X': 2 ,'Y' : 3, 'label':'Red'} ,
                {'Point' : 'C', 'X': 3 ,'Y' : 1, 'label':'Blue'},
                {'Point' : 'D', 'X': 6 ,'Y' : 5, 'label':'Blue'} 
            ]   
    new_point ={'X' :2 , 'Y' :2}

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
    

    k=1 #5
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
        print("Name:",d,"No. of votes :",vote[d])
    print(border)

    predicted_class = max(vote,key=vote.get)
    print(border)
    print("Predicted class for (2,2) is",predicted_class)
    print(border)

def main():
    Predictor()
if __name__ =="__main__":
    main()