import requests
from nose.tools import nottest
from nose.plugins.attrib import attr
from ConfigParser import ConfigParser

class ApiTestCase():
    main_url=''

    def __init__(self):
        test_suite_config = ConfigParser()
        test_suite_config.read('./test_suite.ini')
        self.main_url = test_suite_config.get('api_settings', 'url')

    def get_results(self, url):
        r = requests.get(self.main_url + url)
        return (r.json(), r.status_code)

@attr('smoke')
def test_get_one_post():
    '''
    Get one post successfully.
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/posts/1')
    assert response_code == 200

def test_get_posts():
    '''
    Get /posts without arguments, get default number of posts = 100
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/posts')
    assert len(result) == 100
    assert response_code == 200

def test_get_page_of_posts():
    '''
    Get posts on given page
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/posts?_page=7')
    assert response_code == 200

def test_get_slice_of_posts():
    '''
    Get a slice of posts
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/posts?_start=20&_end=30')
    assert response_code == 200
    assert result[0]['id'] == 21
    assert result[-1]['id'] == 30

def test_get_comments_on_post():
    '''
    Get comments from a post
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/posts/1/comments')
    assert response_code == 200

def test_get_page_of_albums():
    '''
    Get albums on given page
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/albums?_page=7')
    assert response_code == 200

def test_get_page_of_photos():
    '''
    Get photos on given page
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/photos?_page=7')
    assert response_code == 200

def test_get_page_of_users():
    '''
    Get users on given page
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/users?_page=7')
    assert response_code == 200

def test_get_one_todo():
    '''
    Get one todo
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/todos/1')
    assert response_code == 200

def test_get_page_of_todos():
    '''
    Get todos on given page
    :return:
    '''
    test_case = ApiTestCase()
    (result, response_code) = test_case.get_results('/todos?_page=7')
    assert response_code == 200
