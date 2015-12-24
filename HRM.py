import sys

from main.create import create_event
from main import app

if __name__ == "__main__":    
    dlg = create_event()
    dlg.show()
    sys.exit(app.exec_())


