from flask import Flask, render_template,redirect, request, session, flash
import os
from func.py import Download, Change

#change INDEX_NAME and DOC_TYPE_NAME for specific names of your indices and types in your elasticsearch

app = Flask(__name__)


@app.route('/')
def start():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('start.html')

@app.route('/charts/')
def wykresy():
    if session.get('logged_in'):
        return render_template('charts.html')
    else:
        return redirect('/')

@app.route('/results/', methods=['GET', 'POST'])
def wyszukiwarka():
    if session.get('logged_in'):
        result_list, size=Download(INDEX_NAME,DOC_TYPE_NAME)
        return render_template('results.html',result_list=result_list,size=size)
    else:
        return redirect('/')

@app.route('/puls/', methods=['GET','POST'])
def pulsbiznesu():
    if session.get('logged_in'):
        lista, rozmiar=Download(INDEX_NAME,DOC_TYPE_NAME)
        im = request.form.get('im')
        reg = request.form.get('reg')
        ident = request.form.get('ident')
        if ident:
            result_list2, size2=Change(INDEX_NAME,DOC_TYPE_NAME,im, reg, ident)
            return render_template('puls.html',result_list=result_list2,size=size2)
        else:
            return render_template('puls.html',result_list=lista,size=rozmiar)
    else:
        return redirect('/')

@app.route('/link/', methods=['GET','POST'])
def linkedin():
    if session.get('logged_in'):
        result_list, size=Download(INDEX_NAME,DOC_TYPE_NAME)
        return render_template('link.html',result_list=result_list,size=size)
    else:
        return redirect('/')
        
@app.route('/hurt/', methods=['GET','POST'])
def hurtdetal():
    if session.get('logged_in'):
        lista, rozmiar=Download(INDEX_NAME,DOC_TYPE_NAME)
        im = request.form.get('im')
        reg = request.form.get('reg')
        ident = request.form.get('ident')
        if ident:
            result_list2, size2=Change(INDEX_NAME,DOC_TYPE_NAME,im, reg, ident)
            return render_template('hurt.html',result_list=result_list2,size=size2)
        else:
            return render_template('hurt.html',result_list=lista,size=rozmiar)
    else:
        return redirect('/')
        
@app.route('/twitter-akt/', methods=['GET','POST'])
def twittera():
    if session.get('logged_in'):
        lista, rozmiar=Download(INDEX_NAME,DOC_TYPE_NAME)
        im = request.form.get('im')
        reg = request.form.get('reg')
        ident = request.form.get('ident')
        if ident:
            result_list2, size2=Change(INDEX_NAME,DOC_TYPE_NAME,im, reg, ident)
            return render_template('twitter-akt.html',result_list=result_list2,size=size2)
        else:
            return render_template('twitter-akt.html',result_list=lista,size=rozmiar)
    else:
        return redirect('/')

@app.route('/', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Zły login lub hasło')
    return start()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('/')

if __name__ == '__main__':
    app.secret_key = os.urandom(16)
    app.run(host='0.0.0.0', port=8001) 
