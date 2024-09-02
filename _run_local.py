import _config as c

def _init_config_():
	c.CURRENT_SETTING = c.LOCAL_SETINGS

_init_config_()
import start_point as sp
_init_config_()

app = sp.app
app.run(host=c.CURRENT_SETTING['HOST'], port=c.CURRENT_SETTING['PORT'], debug=c.CURRENT_SETTING['IS_DEBUG']) 