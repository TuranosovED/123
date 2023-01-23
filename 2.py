from flask import Flask, render_template, request

app = Flask(__name__)
crypt = None
a = 0
@app.route('/', methods=['GET', 'POST'])
def test():
    global a
    number = request.form.get("Number")
    string = request.form.get("String")
    if number is not None:
        a = int(number)
    if string is not None:
        i = 0
        crypt = ""
        while i < len(string):
            if string[i] == " ":
                    crypt +=" "
            if( (ord(string[i]) in range(55,91)) or (ord(string[i]) in range(97,123)) ):
                if(ord(string[i]) in range(55,91) and ord(string[i])+a > 90):
                    crypt+=chr(ord(string[i])-91+55+a)
                elif(ord(string[i]) in range(97,123) and ord(string[i])+a > 122):
                    crypt+=chr(ord(string[i])-123+97+a)
                elif(ord(string[i])+a in range(55,91) or ord(string[i])+a in range(97,123)):
                    crypt+=chr(ord(string[i])+a)
                else:
                    crypt+=string[i]
            i+=1
                
    
            
    else:
        crypt = None
    return render_template("index.html", password=crypt)

if __name__ == '__main__':
    app.debug = True
    app.run()
    