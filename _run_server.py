import start_point as sp
import _config as c
c.CURRENT_SETTING = c.SERVER_SETINGS


app = sp.app
# app.run(host=c.CURRENT_SETTING['HOST'], port=c.CURRENT_SETTING['PORT'], debug=c.CURRENT_SETTING['IS_DEBUG']) 