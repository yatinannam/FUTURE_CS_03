import os
from flask import Flask, request, send_file, render_template, flash, redirect
from werkzeug.utils import secure_filename
from encryption import encrypt_file, decrypt_file

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    files = [f[:-4] for f in files if f.endswith('.enc')]
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect('/')
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect('/')
    
    filename = secure_filename(file.filename)
    data = file.read()
    encrypted_data = encrypt_file(data)
    
    with open(os.path.join(UPLOAD_FOLDER, filename + ".enc"), 'wb') as f:
        f.write(encrypted_data)
    
    flash('File uploaded and encrypted!')
    return redirect('/')

@app.route('/download/<filename>')
def download(filename):
    enc_path = os.path.join(UPLOAD_FOLDER, filename + ".enc")
    if not os.path.exists(enc_path):
        return "File not found", 404
    
    with open(enc_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt_file(encrypted_data)
    
    temp_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(temp_path, 'wb') as f:
        f.write(decrypted_data)
    
    return send_file(temp_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
