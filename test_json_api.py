import requests
from nose.tools import nottest
from ConfigParser import ConfigParser

test_suite_config = ConfigParser()
test_suite_config.read('./test_suite.ini')

main_url = test_suite_config.get('api_settings', 'url')
post_url = main_url + '/posts'

def test_get_one_post():
    '''
    Get one post successfully.
    :return:
    '''
    post_url = main_url + '/posts/1'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_posts():
    '''
    Get /posts without arguments, get default number of posts = 100
    :return:
    '''
    post_url = main_url + '/posts'
    r = requests.get(post_url)
    data = r.json()
    assert len(data) == 100
    assert r.status_code == 200

def test_get_page_of_posts():
    '''
    Get posts on given page
    :return:
    '''
    post_url = main_url + '/posts?_page=7'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_slice_of_posts():
    '''
    Get a slice of posts
    :return:
    '''
    post_url = main_url + '/posts?_start=20&_end=30'
    r = requests.get(post_url)
    data = r.json()
    assert data[0]['id'] == 21
    assert data[-1]['id'] == 30
    assert r.status_code == 200

def test_get_comments_on_post():
    '''
    Get comments from a post
    :return:
    '''
    post_url = main_url + '/posts/1/comments'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_page_of_albums():
    '''
    Get albums on given page
    :return:
    '''
    post_url = main_url + '/albums?_page=7'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_page_of_photos():
    '''
    Get photos on given page
    :return:
    '''
    post_url = main_url + '/photos?_page=7'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_page_of_users():
    '''
    Get users on given page
    :return:
    '''
    post_url = main_url + '/users?_page=7'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_one_todo():
    '''
    Get one todo
    :return:
    '''
    post_url = main_url + '/todos/1'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_page_of_todos():
    '''
    Get todos on given page
    :return:
    '''
    post_url = main_url + '/todos?_page=7'
    r = requests.get(post_url)
    assert r.status_code == 200
