import os
import sys
from main import app


sys.path.insert(0, os.path.dirname(__file__))

if __name__ == '__main__':
    app.run(host='127.0.0.1')
