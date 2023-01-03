from models.User import User
from src.UserList import UserList


def test_save_user_list():
    file_path = '/home/peter/Desktop/inz/db/test_UserList.json'
    img_path = '../static/def/'
    data = [
        User(id=1, name="Peter", surname="Kub-on", image=img_path + "def_pers_icon.png",
             login="admin", password="admin", role="doctor"),
        User(id=1, name="Piotr", surname="Kub-on", image=img_path + "def_pers_icon.png",
             login="pkubon", password="pkubon", role="doctor"),
        User(id=1, name="Adam", surname="Jak-on", image=img_path + "def_pers_icon.png",
             login="adam", password="adam", role="doctor"),
    ]

    tmp = UserList.save_user_list(data, file_path)
    assert 1 == 1


def test_read_user_list():
    file_path = '/home/peter/Desktop/inz/db/test_UserList.json'
    img_path = '../static/def/'
    read_m = UserList.read_user_list(file_path)
    data = [
        User(id=1, name="Peter", surname="Kub-on", image=img_path + "def_pers_icon.png",
             login="admin", password="admin", role="doctor"),
        User(id=1, name="Piotr", surname="Kub-on", image=img_path + "def_pers_icon.png",
             login="pkubon", password="pkubon", role="doctor"),
        User(id=1, name="Adam", surname="Jak-on", image=img_path + "def_pers_icon.png",
             login="adam", password="adam", role="doctor"),
    ]
    assert data == read_m
