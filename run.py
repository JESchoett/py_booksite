from booksite.app import create_app

from flask import Flask, send_from_directory
flask_app = create_app("development")

#allow the handeling of static files in the /booksite/static folder
@flask_app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)


if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', debug=True, port=5003)