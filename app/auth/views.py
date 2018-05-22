from flask import render_template
from . import auth


# registration route
@auth.route('templates/auth/reqister',methods=['GET','POST'])
def register():
    '''
    function that registaers the users
    '''
    form =RegistrationForm()
    if form.validate_on_submit():
        user =User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    title="Registration"
    return render_template('auth/register.html',registration_form=form,title=title)


@auth.route('/login')
def login(): #login view function that renders a template a template file
    return render_template('auth/login.html')