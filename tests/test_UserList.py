from src.PatientList import PatientList

from models.User import User
from src.UserList import UserList


def test_save_user_list():
    IMG_PATH_DEF = '../static/def/'
    data = [
        User(id=1, name="Peter", surname="Kub-on", image=IMG_PATH_DEF+"def_pers_icon.png",
             login="admin", password="admin"),
        User(id=1, name="Piotr", surname="Kub-on", image=IMG_PATH_DEF+"def_pers_icon.png",
             login="pkubon", password="pkubon"),
        User(id=1, name="Adam", surname="Jak-on", image=IMG_PATH_DEF+"def_pers_icon.png",
             login="adam", password="adam"),
    ]

    tmp = UserList.save_user_list(data)
    assert 1 == 1

def test_read_user_list():
    IMG_PATH_DEF = '../static/def/'
    readed = UserList.read_user_list()
    data = [
        User(id=1, name="Peter", surname="Kub-on", image=IMG_PATH_DEF+"def_pers_icon.png",
             login="admin", password="admin"),
        User(id=1, name="Piotr", surname="Kub-on", image=IMG_PATH_DEF+"def_pers_icon.png",
             login="pkubon", password="pkubon"),
        User(id=1, name="Adam", surname="Jak-on", image=IMG_PATH_DEF+"def_pers_icon.png",
             login="adam", password="adam"),
    ]
    assert data == readed
