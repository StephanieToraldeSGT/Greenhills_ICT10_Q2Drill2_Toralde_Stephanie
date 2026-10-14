# seatwork bleghhh
from pyscript import display, document

def student_club(e):
        document.getElementById('checking').innerHTML = ''
        student_givenname = document.getElementById('first_name').value
        student_surname = document.getElementById('last_name').value
        danceclub_firstnames = ('Isabelle', 'Leane', 'Jade', 'Sky', 'Chalanie', 'Devon', 'Jennifer')
        danceclub_lastnames = ('Cabatu', 'Gabia', 'Cabatingan', 'Campo', 'Lumbang', 'Villostas', 'Uy')
        danceclub_members = danceclub_firstnames + danceclub_lastnames
        name_checker = student_givenname, student_surname in danceclub_members
        
        display_message = (f'Sorry {student_givenname} {student_surname}, you are not apart or are not a part of OBMC ', f'Congratulations {student_givenname} {student_surname}! You are successfully apart of the dance troupe Monarch, whose club coordinator (and sometimes chereographer) is Sir Akihiro Marutani!!')
        
        display(display_message[name_checker], target='checking')
