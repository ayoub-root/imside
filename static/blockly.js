class Component {
constructor(name){
    this.name=name;
}}
////////////////////////
class Device {
constructor(name){
    this.name=name;
}}
var i =0;
 //alert("ffff  ")
            function device(name,bg,description) {

  Blockly.Blocks[name] = {
  init: function() {

    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField(new Blockly.FieldImage(bg, 115, 115, { alt: "*", flipRtl: "FALSE" }));
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip(description);
 this.setHelpUrl("");
  }
};
Blockly.JavaScript[name] = function(block) {
 return 'var d'+(i++)+' = devices("'+name+'");'+'\n';
};
Blockly.Python[name] = function(block) {
  return 'device_("'+name+'")\n';
};
}
        function component(name,bg,description) {

  Blockly.Blocks[name] = {

  init: function() {
    this.appendDummyInput()
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField(new Blockly.FieldImage(bg, 115, 115, { alt: "*", flipRtl: "TRUE"}));
    this.appendStatementInput("NAME")
        .setCheck(null);
    this.setPreviousStatement(false, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip(description);
 this.setHelpUrl("");
  }
};
Blockly.JavaScript[name] = function(block) {
     var text = Blockly.JavaScript.statementToCode(block, 'NAME',
      Blockly.JavaScript.ORDER_MEMBER) || '\'\'';
 return 'function components("'+name+'")'+'\n'+'{\n '+text+'}';
};
Blockly.Python[name] = function(block) {
  return 'def component_("'+name+'"):\n';
};
}          //    alert("{{ post.name }}");
  function microservice(name,id) {

Blockly.Blocks[name] = {
  init: function() {
    this.appendValueInput("NAME")
        .setAlign(Blockly.ALIGN_CENTRE)
        .appendField(name);
    this.setInputsInline(false);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};
Blockly.JavaScript[name] = function(block) {
     var text = Blockly.JavaScript.valueToCode(block, 'NAME',
      Blockly.JavaScript.ORDER_MEMBER) || '\'\'';
 return ' ms_('+name+' , '+id+' , '+text+');\n';
};
Blockly.Python[name] = function(block) {
 return ' ms_('+name+')\n';
};



} var d=0;

function microservices(names,id,type, argss, description) {
	let name=names;
	d=(d+1);
 var args= [];
 var msg="";
 var t=argss.split(" ");//
 for (var i in t){
    // alert('"'+t[i]+'"');
    args.push({"type":"input_value","name":'"'+t[i]+'"',"align": "RIGHT"});
     msg+= t[i]+"%"+(+i+1)+" ";
 }
//alert(type);
//alert(args[2].name);
    var data = {
        "message0": name+"   "+d+' '+msg,
        "args0":args
    }
	//alert(name)
    Blockly.Blocks[name] = {
        init: function () {

            this.jsonInit(data);
          this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
   this.setColour(id);
 this.setTooltip(description);
 this.setHelpUrl("lk,kl,lk");
        }
    };
 if (type==="standard") {
    // alert(type+type.length)
     Blockly.JavaScript[name] = function (block) {
         var val = [];
         for (i in t) {
             //   alert('"'+t[i]+'"');
             val[i] = Blockly.JavaScript.valueToCode(block, '"' + t[i] + '"', Blockly.JavaScript.ORDER_ATOMIC);
         }
//alert(val)
         return name + '(' + val + ');\n';
     };
     Blockly.Python[name]= function (block) {return "";};
 }
 if(type==="standard"){
   Blockly.Python[name] = function(block) {
    var val=[];
    var kwargs=[];
    for (i in t){
     //   alert('"'+t[i]+'"');
        kwargs[i]="'"+t[i]+"'"+':'+Blockly.Python.valueToCode(block, '"'+t[i]+'"', Blockly.Python.ORDER_ATOMIC)
         val[i] = Blockly.Python.valueToCode(block, '"'+t[i]+'"', Blockly.Python.ORDER_ATOMIC);
    }

  return 'pymicroservice("'+name+'","'+id+'"'+',args={'+kwargs+'})\n';
};
   Blockly.JavaScript[name]=function (block) { return "$('#ssss').append('<div id=\"sss\">"+name+"</div>')";

};}

}
  function data(name) {

  Blockly.Blocks[name] = {
  init: function() {
    this.appendStatementInput("NAME")
        .setCheck(null);

    this.setPreviousStatement(false, null);
    this.setNextStatement(false, null);
    this.setColour((d%400));
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

}