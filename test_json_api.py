import requests
from nose.tools import nottest
main_url = 'http://localhost:3000'

def test_get_one_post():
    post_url = main_url + '/posts/1'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_posts():
    post_url = main_url + '/posts'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_page_of_posts():
    post_url = main_url + '/posts?_page=7'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_slice_of_posts():
    post_url = main_url + '/posts?_start=20&_end=30'
    r = requests.get(post_url)
    assert r.status_code == 200

def test_get_comments_on_post():
    post_url = main_url + '/posts/1/comments'
    r = requests.get(post_url)
    assert r.status_code == 200
