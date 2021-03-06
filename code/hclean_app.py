import re
from flask import Flask, session, render_template, request, jsonify, flash, redirect, make_response
from flask_wtf import FlaskForm, Form
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import json
import datetime

from pygments import highlight
from pygments.lexers import HtmlLexer
from pygments.formatters import HtmlFormatter

from forms import Form1

# Initialize the Flask application
application = Flask(__name__)
application.config['SECRET_KEY'] = 'hohohoo'

@application.route('/', methods=['GET', 'POST'])
def consolidation_page():
    form = Form1()
    pygmented_text = ''
    the_css= ''

    if request.method == 'POST' and form.validate():
        ATTR = [
            'style', 'class', 'width', 'height', 'lang', 'align', 'face',
            'size', 'cellspacing', 'cellpadding']
        TAGS = ['font', 'span', 'u']

        attr = [
            "c_{}".format(x) in request.form \
            for x in ATTR]
        tags = [
            "c_{}".format(x) in request.form \
            for x in TAGS]

        htmlcode = clean_html(
                request.form['text'],
                attr=[x[1] for x in zip(attr, ATTR) if x[0]],
                tags=[x[1] for x in zip(tags, TAGS) if x[0]])
        form.text.data = htmlcode
        pygmented_text = highlight(htmlcode, HtmlLexer(), HtmlFormatter(style='colorful'))
        the_css = HtmlFormatter(style='colorful').get_style_defs()

        return render_template('myform.html', form=form, pygmented_text=pygmented_text, the_css=the_css)
    else:
        return render_template('myform.html', form=form, pygmented_text=pygmented_text, the_css=the_css)


def attr_filter(name):
    return [r' {}=".*?"'.format(name), r' {}=\d+'.format(name)]


def tag_filter(name):
    return [r'<{}.*?>'.format(name), r'</{}>'.format(name)]


def clean_html(data, **kwargs):
    if 'attr' in kwargs:
        for f in kwargs['attr']:
            for r in attr_filter(f):
                data = re.sub(r, '', data)
    if 'tags' in kwargs:
        for f in kwargs['tags']:
            for r in tag_filter(f):
                data = re.sub(r, '', data)
    return data
