import numpy as np
import tensorflow as tf
from keras.layers import Dense
from keras import Sequential
from tensorflow.python.keras.losses import BinaryCrossentropy
import csv  

x = np.zeros((0,2))
y = np.zeros((0,1))

cards = {'jack':11,'queen':12, 'king':13, 'ace': 14}
suits = {'hearts': 0, 'dimonds': 1, 'clubs':2,'spades':3}

trainOrAdd = input("would you like to train the AI or add data (t/a): ")



if(trainOrAdd == 't'):
    with open('cardData.csv','r') as f:
        reader = csv.reader(f)
        for read in reader:
            x = np.append(x,[[float(read[0]),float(read[1])]],axis=0)
            y = np.append(y,[[float(read[2])]])

    layer1 = Dense(units=2,activation='relu')
    layer2 = Dense(units=1, activation='sigmoid')

    model = Sequential([layer1,layer2]) #builid model
    model.compile(loss=BinaryCrossentropy()) # compile useing loss that you would like


    model.fit(x,y,epochs=1000) # train it with dater

    inX = int(input("how many games do you want to predict: "))

    for i in range(inX):
        card1 = input('What is the first card do you have: ')
        suit1 = input('What is the suit of the first card: ')
        suit1 = suits[suit1]
        card2 = input('What is the second card do you have: ')
        suit2 = input('What is the suit of the second card: ')
        suit2 = suits[suit2]
        try:
            card1 = int(card1)
        except:
            card1 = cards[card1]
        try:
            card2 = int(card2)
        except:
            card2 = cards[card2]
        card1 = card1 * 4 - suit1
        card2 = card2 * 4 - suit2
        print(card1,card2)
        predict1 = model.predict([[card1,card2]])
        print(predict1)

else:
    inX2 = int(input('how many games would you like to play: '))

    with open('cardData.csv','a',newline='') as f:
        writer = csv.writer(f)
        
        for i in range(inX2):
            card1 = input('What is the first card do you have: ')
            suit1 = input('What is the suit of the first card: ')
            suit1 = suits[suit1]
            card2 = input('What is the second card do you have: ')
            suit2 = input('What is the suit of the second card: ')
            suit2 = suits[suit2]
            try:
                card1 = int(card1)
            except:
                card1 = cards[card1]
            try:
                card2 = int(card2)
            except:
                card2 = cards[card2]
            card1 = card1 * 4 - suit1
            card2 = card2 * 4 - suit2
            win = input('did you win y/n: ')
            if win == 'y':
                win = 1
            else: 
                win = 0
            print(card1,card2,win)
            writer.writerow([card1,card2,win])
            
