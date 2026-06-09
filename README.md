# Welcome to Microblog!

This is an example application featured in Miguel Grinberg's [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). It is a full-featured social microblogging web application built with Python and Flask.

## Features
* User registration, login, password reset, and profile customization
* Follower system with a personalized home timeline and global explore feed
* Full-text post search and live language translation
* Asynchronous background tasks and private user messaging

## Virtual Environment & Dependencies

Create and activate a `venv` virtual environment:

```bash
$ python3 -m venv venv
```

Simply activate your brand new environment by running the following command:
```bash
$ source venv/bin/activate
(venv) $ _
```

*If you're using a Microsoft Windows command prompt window, use this command:*
```bash
$ venv\Scripts\activate
(venv) $ _
```

*Or if you prefer PowerShell instead, use this other activation command:*
```bash
$ venv\Scripts\Activate.ps1
(venv) $ _
```

Install the required Python packages:

```bash
(venv) $ pip install -r requirements.txt
```

## Configuration & Database Setup

1. Create a `.env` file in the root directory to store your local secrets and service keys:
   ```env
   SECRET_KEY=your-secret-key
   DATABASE_URL=sqlite:///app.db
   MAIL_SERVER=localhost
   MAIL_PORT=8025
   MS_TRANSLATOR_KEY=your-azure-key
   ELASTICSEARCH_URL=http://localhost:9200
   ```
2. Initialize the database migrations:
   ```bash
   (venv) $ flask db upgrade
   ```

## Running the Code

Because `.flaskenv` sets `FLASK_APP=microblog.py` automatically, start the development server with:

```bash
(venv) $ flask run
```

Open your web browser and navigate to `http://localhost:5000/`.

## Translations

Because compiled `.mo` translation files are excluded from Git, compile the language catalogs before running the application:

```bash
flask translate compile
```

To initialize a new language translation catalog:

```bash
flask translate init <language-code>
```

To update existing translation catalogs after modifying text strings in the codebase:

```bash
flask translate update
flask translate compile
```

## Production Deployment (Vagrant, Nginx & Supervisor)

To deploy using the included ARM64 Ubuntu Vagrant VM (`192.168.56.10`):

1. **Start VM & Generate SSL Certs**
   ```bash
   vagrant up --provider=virtualbox && vagrant ssh
   cd /home/vagrant/microblog && mkdir -p certs
   openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 -keyout certs/key.pem -out certs/cert.pem
   ```

2. **Configure Supervisor (Gunicorn Process Manager)**
   ```bash
   sudo cp deployment/supervisor/microblog.conf /etc/supervisor/conf.d/microblog.conf
   sudo supervisorctl reload && sudo supervisorctl status
   ```

3. **Configure Nginx (Reverse Proxy & HTTPS)**
   ```bash
   sudo cp deployment/nginx/microblog /etc/nginx/sites-available/microblog
   sudo rm -f /etc/nginx/sites-enabled/default
   sudo ln -s /etc/nginx/sites-available/microblog /etc/nginx/sites-enabled/microblog
   sudo nginx -t && sudo systemctl reload nginx
   ```
   
* **Access:** Open `https://192.168.56.10` on your host machine.
* **Management:** Use `sudo supervisorctl restart microblog` inside the VM to restart after updates, or `vagrant halt` from your host to stop the VM.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
