from flask import Flask


FAI=Flask(__name__)

@FAI.route('/stringResponse')
def stringResponse():
    return 'THIS IS THE FIRST STRING VIEW RESPONSE IN FLASK'

if __name__==('__main__'):
    FAI.run(debug=True)