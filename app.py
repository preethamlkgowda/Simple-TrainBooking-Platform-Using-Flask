
from email import message
from optparse import Option
from turtle import position
from flask import Flask, render_template,request
from regex import F

from train import Train

app=Flask(__name__)
a=Train()
dropdown_options = [
        {'value': 'W', 'text': 'Window'},
        {'value': 'M', 'text': 'Middle'}
        
    ]
dropdown_options2 = [
        {'value': 0, 'text': '0'},
        {'value': 1, 'text': '1'},
        {'value': 2, 'text': '2'},
        {'value': 3, 'text': '3'}
    ]
dropdown_options3 = [
        {'value': 0, 'text': '0'},
        {'value': 1, 'text': '1'},
        {'value': 2, 'text': '2'},
        {'value': 3, 'text': '3'},
        {'value': 4, 'text': '4'}
    ]
@app.route('/')#base url
def index():
    
    return render_template('index.html', Options=dropdown_options,Pos1=dropdown_options2,Pos2=dropdown_options3)



@app.route('/Awailable',methods=['POST'])#url from base to catch 
def AwailableSeateCount():
    
  
    return render_template('index.html',seates=a.SeatsAwailable())

@app.route('/Awailable/position',methods=['POST'])#url from base to catch 
def AwailableSeatePos():
    
    
    return render_template('index.html',position=a.SeatPositions(),Options=dropdown_options,Pos1=dropdown_options2,Pos2=dropdown_options3)

@app.route('/BookSeat',methods=['POST'])#url from base to catch 
def Bookseat():
    text=request.form.get('BookSeat')
    
    return render_template('index.html',message1=a.BookSeat(text),Options=dropdown_options,Pos1=dropdown_options2,Pos2=dropdown_options3)
@app.route('/CancelSeat',methods=['POST'])#url from base to catch 
def Cancelseat():
    text1=request.form.get('CancelSeatRow')
    text2=request.form.get('CancelSeatCol')
    m=[int(text1),int(text2)]
    
    return render_template('index.html',message2=a.CancelSeat(m),Options=dropdown_options,Pos1=dropdown_options2,Pos2=dropdown_options3)

if __name__ =='__main__':
    app.run()