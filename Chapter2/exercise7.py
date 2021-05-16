import numpy as np

# intermediate level exercise
def count11(seq):
    occurence=0
    for i in range(len(seq)-1):
       if seq[i]==1:
           if seq[i+1]==1:
               occurence+=1
    return occurence

print(count11([0, 0, 1, 1, 1, 0])) 

# advance level exercise
def generate(p1):
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    occurence=0
    for i in range(len(seq)-4):
        test=True
        for j in range(i,i+5): 
            if seq[j]!=1:
                test=False        
        if test:
            occurence+=1
    return occurence 

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
