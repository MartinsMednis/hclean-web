from flask_wtf import FlaskForm, Form
from wtforms.fields import SubmitField, BooleanField, TextAreaField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Optional



class Form1(FlaskForm):
    # attributes
    c_style = BooleanField('style', default="checked")
    c_class = BooleanField('class', default="checked")
    c_width = BooleanField('width', default="checked")
    c_height = BooleanField('height', default="checked")
    c_lang = BooleanField('lang', default="checked")
    c_align = BooleanField('align', default="checked")
    c_face = BooleanField('face', default="checked")
    c_size = BooleanField('size', default="checked")
    c_cellspacing = BooleanField('cell sp.', default="checked")
    c_cellpadding = BooleanField('cell pad.', default="checked")
    # tags
    c_font = BooleanField('font', default="checked")
    c_span = BooleanField('span', default="checked")
    # html input field
    text = TextAreaField('Text', validators=[Optional()])
    submit = SubmitField('Clean html')

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        return True
