from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm

api = Redprint('client')


@api.route('/register',methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL:__register_user_by_email,
            ClientTypeEnum.USER_MINA:__register_user_by_mina
        }


def __register_user_by_email(form):
    User.register_by_email(form.account.data,form.secret.data)

def __register_user_by_mina():
    pass