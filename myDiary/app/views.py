from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app,db
from forms import LoginForm,WriteForm
from models import Diary
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
     diary = Diary.query.all()
     return render_template('index.html',
        title = 'Home',
        diary = diary
        )

@app.route('/diary_content/<titlename>')
def diary_content(titlename):
     diary = Diary.query.filter_by(titlename = titlename).first()
     return render_template('diary_content.html',
        title = 'Home',
        diary = diary 
        )

@app.route('/edit_content/<titlename>', methods = ['GET', 'POST'])
def edit_content(titlename):
    form = WriteForm()
    diary = Diary.query.filter_by(titlename = titlename).first()
    if form.validate_on_submit():
        diary.titlename = form.titlename.data
        diary.content = form.content.data
        diary.update_time = datetime.utcnow()
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('diary_content',titlename = form.titlename.data))
    else:
       form.titlename.data = diary.titlename
       form.content.data = diary.content
    return render_template('edit.html',
        title = 'Home',
        diary = diary,
        form = form
        )

@app.route('/write', methods = ['GET', 'POST'])
def write():
    form = WriteForm()
    if form.validate_on_submit():
        diary = Diary(titlename=form.titlename.data,content=form.content.data,update_time = datetime.utcnow())
        db.session.add(diary)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('index'))
    else:
        form.titlename.data = Diary.titlename
        form.content.data = Diary.content
    return render_template('write.html',
        form = form)

@app.route('/delete/<titlename>', methods = ['GET', 'POST'])
def delete(titlename):
     diary = Diary.query.filter_by(titlename=titlename).first()
     db.session.delete(diary)
     db.session.commit()
     flash('Your changes have been saved.')
     return redirect(url_for('index'))
