import sys

from main.login import login_event
from main import app

if __name__ == "__main__":
    dlg = login_event()
    dlg.show()
    sys.exit(app.exec_())

