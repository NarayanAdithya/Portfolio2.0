from app import app, db, socketio
from app.auth.models import User
from app.models import TechStack, Project
@app.shell_context_processor
def make_shell_context():
    return {'db':db,'user':User,'tech':TechStack,'project':Project}


if __name__=='__main__':
    socketio.run(app)