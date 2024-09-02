const VERSION = "1.0.0";
let _elem_counter_ = 0;


const VIEW = {
	test : function (){
		return "TEST";
	},
	title : function(t){
		document.title = t;
		dom_refresh();
	},
	meta : function (argument) {
		var HEAD = document.querySelector("head");
		let META_ = document.createElement('meta');
		for(attr in res){
			META_[attr] = res[attr];
		}
		HEAD.appendChild(META_);
	},
	include_js :function(res){
		var HEAD = document.querySelector("head");
		let _JS = document.createElement('script');
		for(attr in res){
			_JS[attr] = res[attr];
		}
		HEAD.appendChild(_JS);
	},
	include_css :function(res){
		var HEAD = document.querySelector("head");
		let _CSS = document.createElement('link');
		for(attr in res){
			_CSS[attr] = res[attr];
		}
		HEAD.appendChild(_CSS);
	},
	__init__ : function (elems,ids_){
		var holder = document.createElement("div");
		for (var i = 0; i < elems.length; i++) {
			var template = document.createElement(elems[i]["tag"]);

			if(elems[i]["tag"]==undefined){break}
			if(elems[i]["classn"]!=undefined){
				elems[i]["class"] = elems[i]["classn"];
				delete elems[i]["classn"];
			}

			if(elems[i]["text"]!=undefined){
				template.innerHTML = elems[i]["text"];
			}

   			var sub_elem_ = undefined;
			for(attr in elems[i]){
				if(["tag","contents","text"].includes(attr)){continue}
				else{template.setAttribute(attr,elems[i][attr])}
			};

			if("contents" in elems[i]){
				for (var xxx = 0; xxx < elems[i]["contents"].length; xxx++) {
					sub_elem_ = this.__init__([elems[i]["contents"][xxx]]);
					if(sub_elem_!= undefined){
						template.appendChild(sub_elem_);
					}
				}
			}
			holder.appendChild(template);
		};
		return holder;
	},
	init : function (elems,ids_){
		var elems = this.__init__(elems);
		return {
			elements : elems,
			create : function(id){
				if (id==undefined) {
					document.body.appendChild(elems);
				}else{
					$ID(id).appendChild(elems);
				}
				dom_refresh();
				return this;
			},
			hide : function(){
				elems.style.display = "none";
				return this;
			},
			show : function(){
				elems.style.display = "block";
				return this;
			},
			event : function(event,func){
				elems.addEventListener(event,func);
				return this;
			}
		}
	},
	event : function(id_,event,func){
		$ID(id_).addEventListener(event,func);
	}
}

const CSS = VIEW.include_css;
const JS = VIEW.include_js;
const META = VIEW.meta;