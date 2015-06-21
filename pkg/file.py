import os

can_access = lambda file: True if os.path.isfile(file) and os.access(file, os.R_OK) else False