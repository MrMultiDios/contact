import transaction
from .models import DBSession, Subject, Contact
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

@view_config(route_name='home', request_method='GET',
    renderer='templates/mytemplate.pt')
def display_the_contact_form(request):
    infos = request.session.pop_flash('infos')
    subjects = DBSession.query(Subject).all()
    return {'subjects': subjects, 'project': 'contact', 'infos': infos}

@view_config(route_name='home', request_method='POST',
    renderer='templates/mytemplate.pt')
def contact_post(request):
    'Process contact datas'
    with transaction.manager:
        email, subject_id, text = map(request.POST.get,
            ('email', 'subject_id', 'text'))
        DBSession.add(Contact(email=email,
            subject_id=subject_id, text=text))
    request.session.flash('Your submission has been registered', 'infos')
    return HTTPFound(location=request.route_url('home'))