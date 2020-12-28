from app import create_app
from app.models import User
from app.extensions import db 

app = create_app()

@app.shell_context_processor
def create_shell_context():
    return {'db': db, 'User':User}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)