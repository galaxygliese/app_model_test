#-*- coding:utf-8 -*-

###API MODEL
###DATA BASE -TAI HOLBONO

def get_history(_id, _start, _end, _type):
    return [{'id':1, 'date':'2018-04-01', 'start':_start, 'end':_end, \
             'hang_out':'hang_out', 'hang_in':'hang_in', \
             'work_content':'work_content', 'report':'report', 'type':_type}]

def post_history(_user_id, _start, _work_content, _report, _type):
    return {'id': _user_id, 'status': 'status'}

def put_history(_user_id, _start, _end, _hang_out, _hang_in, _work_content, _report, _type):
    return {'id': _user_id, 'status': 'status'}

def delete_history(_id):
    return {'id':_id, 'status': 'status'}



def get_users():
    return [{'id': 1, 'name': 'name', 'email': 'email'}]



def get_user(_user_id):
    return { 'user_id': _user_id, 'name': '', 'email': '', 'enter_date': '', 'tags': '', 'role': ''}

def post_user(_name, _password, _email, _enter_date, _tags, _role):
    return {'user_id':'', 'status':''}

def put_user(_name, _password, _email, _enter_date, _tags, _role):
    return {'user_id':'', 'status':''}

def delete_user(_user_id):
    return {'user_id':'', 'status':''}



def post_sign_in(_email, _password):
    return {'token':''}


if __name__ == '__main__':
   pass
