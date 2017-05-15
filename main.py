import re
from flask import *
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html',
                           form=request.form,
                           flash_msgs=get_flashed_messages(),
                           errors={}
                           )


@app.route('/submit', methods=['POST'])
def submit():
    validation = Validator(request.form, {
        'email': ['not_blank', 'email'],
        'password': ['min_length:9'],
        'colour': ['not_blank'],
        'animal': ['min_count:2'],
        'tiger_type': ['tiger_type'],
    })

    if validation.is_valid():
        flash('Thanks. We have received your submission')
        return redirect(url_for('index'))

    flash('Sorry. There have been some errors. Please fix them')

    return render_template('index.html',
                           form=request.form,
                           flash_msgs=get_flashed_messages(),
                           errors=validation.errors
                           )


class Validator:
    form = None
    metadata = {}
    errors = {}

    def __init__(self, form: ImmutableMultiDict, metadata):
        self.form = form.to_dict(False)
        self.metadata = metadata

    def is_valid(self):
        for field, values in self.metadata.items():
            field_result = []
            for constraint in values:
                param = None

                if ':' in constraint:
                    constraint, param = constraint.split(':')

                if constraint == 'not_blank':
                    field_result.append(self.not_blank(self.form[field]))

                if constraint == 'email':
                    field_result.append(self.email(self.form[field]))

                if constraint == 'min_length':
                    field_result.append(self.min_length(self.form[field], int(param)))

                if constraint == 'min_count':
                    field_result.append(self.min_count(self.form[field], int(param)))

                if constraint == 'tiger_type':
                    field_result.append(self.tiger_type(self.form))

            self.errors[field] = True if False in field_result else False

        return False if True in self.errors.values() else True

    @staticmethod
    def not_blank(value: list):
        return len(value[0]) > 0

    @staticmethod
    def email(value: list):
        m = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)").match(value[0])

        return False if m is None else True

    @staticmethod
    def min_length(value: list, min_length: int):
        v = value[0]
        if v is None and min_length > 0:
            return False

        return len(v) >= min_length

    @staticmethod
    def min_count(value: list, min_count: int):
        if value is None and min_count > 0:
            return False

        return len(value) >= min_count

    @staticmethod
    def tiger_type(obj: dict):
        if 'animal' in obj and 'tiger' in obj['animal'] and not Validator.not_blank(obj['tiger_type']):
            return False

        return True
