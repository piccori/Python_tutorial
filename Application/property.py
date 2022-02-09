class PropertyTest(object):

    def __init__(self, url):
        self._url = url

    def get_url(self):
        print('--get_url--')
        return self._url

    def set_url(self, url):
        print('-- set_url --')
        self._url = url

    def del_url(self):
        del self._url

    url = property(get_url, set_url, del_url, 'url Property')


prop = PropertyTest('https://www.python-izm.com')

prop.url = 'python-izm'

print(prop.url)
