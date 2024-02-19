import os
from flask import Flask, request, render_template
from SpellChecker import SpellCHecker
from werkzeug.utils import secure_filename
import time

class SpellCheckApp(Flask):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.checker = SpellCHecker("./irish.txt")


   @classmethod
   def create_app(cls):
       app = cls(__name__)
       app.add_routes()
       return app


   def add_routes(self):
       self.add_url_rule('/', view_func=self.home)
       self.add_url_rule('/upload', view_func=self.upload, methods=['POST'])


   @staticmethod
   def home():
       return render_template('upload.html')


   def upload(self):
       start_time = time.time()
       file = request.files['file']
       #save the file it so it can be sent to correct_text() 
       file_path = os.path.join(os.getcwd(), 'tmp', file.filename)
       file.save(file_path)
       #run checker on uploaded file
       corrected_text= self.checker.correct_text(input_file =file_path)
        
       end_time = time.time()
       elapsed_time = end_time - start_time
       print(f"Elapsed time: {elapsed_time} seconds")
        
 #output file- made in the spell checker class 
       with open("./output.txt", mode='r', encoding='utf-8-sig') as output_file:
         corrected_text = output_file.read()

       
       

#retrun corrected text
       return corrected_text


if __name__ == '__main__':
   app = SpellCheckApp.create_app()
   app.run(debug=True)