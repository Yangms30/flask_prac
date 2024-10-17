from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xdeO\x19\x8ao\xa7\xc3\xf0\xfeA\xf7\x84\x17eo\xe9'