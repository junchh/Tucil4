from flask import Flask, render_template, url_for
import re 


def matchKeyword(text, keyword, choice):
    if(choice == 3):

        keyword = keyword.lower()
        p = re.compile(keyword)
        it = p.finditer(text)
        rem = []
        for m in it:
            rang = m.span()
            res = keyword
            for j in range(rang[1], len(text)):
                if(text[j] == '.'):
                    if(text[j - 1].isdigit() == False or text[j + 1].isdigit() == False):
                        break
                    else:
                        res += text[j]
                else:
                    res += text[j]
            for j in range(rang[0] - 1, -1, -1):
                if(text[j] == '.'):
                    if(text[j - 1].isdigit() == False or text[j + 1].isdigit() == False):
                        break
                    else:
                        res = text[j] + res
                else:
                    res = text[j] + res
            rem.append([res, rang[0], rang[1]])
        elif(choice == 1):
            
        return rem

def processKalimat(s, start, finish):
    match_tanggal1 = "(senin|selasa|rabu|kamis|jumat|sabtu|minggu), [0-9]+ (jan|feb|mar|apr|mei|jun|jul|agu|sep|okt|nov|des) [0-9]+ [0-9][0-9]:[0-9][0-9] wi(b|t|at)"
    match_tanggal2 = "(senin|selasa|rabu|kamis|jumat|sabtu|minggu) \([0-9]+\/[0-9]+\/[0-9]+\) pukul [0-9][0-9]\.[0-9][0-9] wi(b|t|at)"
    match_bilangan = "[0-9]*\.?[0-9]+"

    p = re.compile(match_bilangan)
    terdekat = 100000
    hasil = ""
    it = p.finditer(s)
    for m in it:
        rang = m.span()
        if(s[rang[0] - 1] == "-"):
            continue
        g = min(abs(rang[1] - start), abs(rang[1] - finish), abs(rang[0] - start), abs(rang[0] - finish))
        if(g < terdekat):
            hasil = s[rang[0]:rang[1]]
            terdekat = g 
    gaga = "-1"
    he = re.search(match_tanggal1, s)
    if(he):
        gaga = s[he.span()[0]:he.span()[1]]
    else:
        he = re.search(match_tanggal2, s)
        if(he):
            gaga = s[he.span()[0]:he.span()[1]]
    
    print(gaga)

    return [hasil, gaga]

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getResult/<int:choice>/<string:keyword>/<text>')
def getres(choice, keyword, text):
    text = text.replace(";", "/")
    text = text.replace("$", " ")
    text = text.lower()
    match_tanggal1 = "(senin|selasa|rabu|kamis|jumat|sabtu|minggu), [0-9]+ (jan|feb|mar|apr|mei|jun|jul|agu|sep|okt|nov|des) [0-9]+ [0-9][0-9]:[0-9][0-9] wi(b|t|at)"

    range_tanggal = re.search(match_tanggal1, text)
    if(range_tanggal):
        tanggal_artikel = text[range_tanggal.span()[0]:range_tanggal.span()[1]]
    else:
        tanggal_artikel = ""
        
    result = tanggal_artikel + '<br>'
    listmatches = matchKeyword(text, keyword, choice)

    for a in listmatches:
        hey = processKalimat(a[0], a[1], a[2])
        if(hey[1] == "-1"):
            hey[1] = tanggal_artikel
        result += "Keyword : " + keyword + "<br>"
        result += "Jumlah : " + hey[0] + "<br>"
        #print(hey[1])
        result += "Waktu : " + hey[1] + "<br>"
        result += a[0] + "<br>"

    return result


if(__name__ == "__main__"):
    app.run(debug=True)