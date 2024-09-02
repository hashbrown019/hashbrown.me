from flask import Flask, render_template, redirect, render_template_string

_INCLUDE_FUNCS = {}
DATA_RETURN_TYPES =["_INT_","_STRING_","_FLOAT_","_OBJECT_","_NONE_"]

class Brorn:
	def __init__(self, arg):
		super(Brorn, self).__init__();
		self.arg = arg;

	def test():
		print(" * Running Brorn Module");

	def include_function(self, name,func):
		_INCLUDE_FUNCS[name] = func
		return _INCLUDE_FUNCS

	'''return _app.render_template(name_of_wsp_file, content="test", contents="test 2")'''
	def render_template(this,view,**vals):
		path = "view" if "brn" in view else 'templates' 

		view_ = open("{}/{}".format(path,view),"r");
		VIEW = view_.read() + "\n";
		view_.close();
		VIEW = render_template_string(VIEW,**vals);
		char_counter = 0; char_finder = ""; code_finder = "";
		codes = []; code_frames = [];
		END_TAG = []; START_TAG_TEMP = []; START_TAG = []
		CHAR_COUNT = 0

		for char in VIEW:
			char_finder += char
			char_counter += 1
			if(char_finder.find("<start$>") !=-1):
				if(CHAR_COUNT not in START_TAG):
					START_TAG_TEMP.append(CHAR_COUNT)
				code_finder +=VIEW[char_counter]
				if(char_finder.find("<end$>") !=-1):
					if(CHAR_COUNT not in END_TAG):
						END_TAG.append(CHAR_COUNT)
					codes.append(code_finder)
					char_finder =""; code_finder = ""
					START_TAG.append(START_TAG_TEMP[0])
					START_TAG_TEMP = []
					code_frames.append(char_counter+1)
			CHAR_COUNT +=1

		TEMP_VIEW = VIEW;
		for indx in range(len(END_TAG)):
			code_block = TEMP_VIEW[START_TAG[indx]-7:END_TAG[indx]+1]
			VIEW = VIEW.replace(code_block,f"__CODE{indx}__")
		code_count = 0
		commands_global = {**_INCLUDE_FUNCS}
		for code in codes:
			LOCAL_OBJECTS = {}
			stringyfy = ""
			for _types in DATA_RETURN_TYPES:
				data_indetifier = _types
				if _types in code :
					if _types =="_STRING_":
						stringyfy = "`";
						break
					break

			tabs = code.split("\n")[1].count("\t")
			lines = code.split("\n")
			new_code = ""
			for line in lines:
				new_code += line.replace("\t","",tabs).replace(data_indetifier,"") + "\n"

			GLOBAL_FUNC_WITH_INC = globals().update(commands_global)
			try:
				exec(new_code.replace("<end$>","").replace("<start$>",""), GLOBAL_FUNC_WITH_INC, LOCAL_OBJECTS)
				commands_global = LOCAL_OBJECTS
			except Exception as e:
				return str(type(e))+" <br> "+str(e)+"<hr>"+code.replace('\n','<br>').replace('<end$>','').replace('\t','&nbsp;'*8)

			try:
				return_workaround = LOCAL_OBJECTS['main']
			except Exception as e:
				return "Some Code blocks are mising the <b><i>main</i></b> function <hr>"+code.replace('\n','<br>').replace('<end$>','').replace('\t','&nbsp;'*8)

			VIEW = VIEW.replace(f"__CODE{code_count}__",f"{stringyfy}{return_workaround()}{stringyfy}")
			code_count +=1

		VIEW = VIEW.replace("<end$>","").replace("<start$>","")

		if("brn" in view):
			HTML_HOLDER = '''<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link class="x-links" rel="stylesheet" href="../static/css/x.css"><link class="x-links" rel="stylesheet" href="../static/css/css"><link class="x-links" rel="stylesheet" href="../static/css/font-awesome.min.css"><script type="text/javascript" src="../static/module/Brorn.min.js"></script><script type="text/javascript" src="../static/module/view.js"></script><title></title></head><body></body><script type="text/javascript">||VIEW||</script></html>'''.replace("||VIEW||",VIEW)
			return render_template_string(HTML_HOLDER)
		else:
			return render_template_string(VIEW)

	def sample(args):
		print(args)

		return args
