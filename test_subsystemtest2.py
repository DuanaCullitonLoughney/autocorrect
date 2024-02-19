import pytest
import tempfile
import os
from SpellCheckApp import SpellCheckApp
from SpellChecker import SpellCHecker




@pytest.fixture(scope='module')
def app():
   app = SpellCheckApp.create_app()
   app.testing = True
   with app.test_client() as client:
       yield client




def test_home_page(app):
   response = app.get('/')
   assert response.status_code == 200
  




def test_upload_file(app):
   with tempfile.NamedTemporaryFile(delete=False) as test_file:
       test_file.write(b'binte')
   test_file_path = test_file.name


   response = app.post('/upload', data={
       'file': (open(test_file_path, 'rb'), test_file_path)
   }, follow_redirects=True)


   assert response.status_code == 200
   assert b'bainte' in response.data



