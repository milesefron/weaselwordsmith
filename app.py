from flask import Flask, render_template, redirect, url_for, request, flash

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
import json
import secrets
import requests
import utils

app = Flask(__name__)
app.config.from_pyfile("settings.py")

csrf = CSRFProtect(app)

api_endpoint =  app.config['API_ENDPOINT'] 

weasel_words = []
r = requests.get(url=api_endpoint + '/vocab')
weasel_words = r.json()


STORY_MAX_SEGMENT_LENGTH = 5000
STORY_MAX_LENGTH = 30000

class TextForm(FlaskForm):
    text = TextAreaField('paste here', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
   form = TextForm()
   return render_template('index.html', form=form, weasel_words=weasel_words)

@app.route('/about')
def about():
   return render_template('about.html', weasel_words=weasel_words)

@app.route('/stats')
def stats():
   form = TextForm()
   return render_template('stats.html', form=form, weasel_words=weasel_words)

@app.route('/help')
def help():
   return render_template('help.html', weasel_words=weasel_words)

@app.route('/analyze', methods=('GET', 'POST'))
def analyze():
   text = request.form['text']

   if len(text) > STORY_MAX_LENGTH:
      form = TextForm()
      flash('Too long! Try a shorter paste.')
      return render_template('index.html', form=form, weasel_words=weasel_words)
   
   if len(text) > STORY_MAX_SEGMENT_LENGTH:
      analysis = utils.handle_long_text(text, STORY_MAX_SEGMENT_LENGTH, api_endpoint, 'analysis')
   else:
      parameters = {'text': text}
      r = requests.post(url = api_endpoint + '/analysis', params = parameters)
      analysis = r.json()
      
   print(json.dumps(analysis, indent=4))
   message = 'We found ' + str(len(analysis['counts'])) + ' of the ' + str(len(weasel_words)) + ' weasel words in your prose.'         
   return render_template('analyze.html', weasel_words=weasel_words, analysis=analysis, message=message)

@app.route('/stats', methods=('GET', 'POST'))
def analyze_stats():
   text = request.form['text']

   if len(text) > STORY_MAX_LENGTH:
      form = TextForm()
      flash('Too long! Try a shorter paste.')
      return render_template('index.html', form=form, weasel_words=weasel_words)
   
   if len(text) > STORY_MAX_SEGMENT_LENGTH:
      analysis = utils.handle_long_text(text, STORY_MAX_SEGMENT_LENGTH, api_endpoint, 'stats')
   else:
      parameters = {'text': text}
      r = requests.post(url = api_endpoint + '/stats', params = parameters)
      analysis = r.json()
      
   #print(json.dumps(analysis, indent=4))
   message = 'Statistical report for your prose'         
   return render_template('analyze.html', analysis=analysis, message=message)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5001)



