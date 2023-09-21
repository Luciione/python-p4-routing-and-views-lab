import io
import sys
from bs4 import BeautifulSoup
from app import app  

class TestApp:
    '''Flask application in app.py'''

    def test_index_route(self):
        '''has a resource available at "/".'''
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_index_text(self):
        '''displays "Python Operations with Flask Routing and Views" in h1 in the browser.'''
        response = app.test_client().get('/')
        assert response.data.decode() == '<h1>Python Operations with Flask Routing and Views</h1>'

    def test_print_route(self):
        '''has a resource available at "/print/<parameter>".'''
        response = app.test_client().get('/print/hello')
        assert response.status_code == 200

    def test_print_text(self):
       '''displays text of the route in the browser.'''
       response = app.test_client().get('/print/hello')
       assert '<h1>Printed String: hello</h1>' in response.data.decode()

    def test_print_text_in_console(self):
        '''displays text of the route in the console.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        app.test_client().get('/print/hello')
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == 'hello\n'

    def test_count_route(self):
        '''has a resource available at "/count/<parameter>".'''
        response = app.test_client().get('/count/5')
        assert response.status_code == 200

    def test_count_range_10(self):
        '''counts through the range of parameter in "/count/<parameter>" on separate lines.'''
        response = app.test_client().get('/count/10')
        count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'

        # Extract plain text content without HTML tags from response
        response_text = ''.join(BeautifulSoup(response.data.decode(), 'html.parser').findAll(text=True))

        assert response_text.strip() == count.strip()

    def test_math_route(self):
        '''has a resource available at "/math/<parameters>".'''
        response = app.test_client().get('/math/5/+/5')
        assert response.status_code == 200

    def test_math_add(self):
        '''adds parameters in "/math/" resource when the operation is "+".'''
        response = app.test_client().get('/math/5/+/5')
        assert response.data.decode() == '<h1>Result: 10.0</h1>'

    def test_math_subtract(self):
        '''subtracts parameters in "/math/" resource when the operation is "-".'''
        response = app.test_client().get('/math/5/-/5')
        assert response.data.decode() == '<h1>Result: 0.0</h1>'

    def test_math_multiply(self):
        '''multiplies parameters in "/math/" resource when the operation is "*".'''
        response = app.test_client().get('/math/5/*/5')
        assert response.data.decode() == '<h1>Result: 25.0</h1>'

    def test_math_divide(self):
        '''divides parameters in "/math/" resource when the operation is "div".'''
        response = app.test_client().get('/math/5/div/5')
        assert response.data.decode() == '<h1>Result: 1.0</h1>'

    def test_math_modulo(self):
        '''finds the remainder of parameters in "/math/" resource when the operation is "%".'''
        response = app.test_client().get('/math/5/%/5')
        assert response.data.decode() == '<h1>Result: 0.0</h1>'
