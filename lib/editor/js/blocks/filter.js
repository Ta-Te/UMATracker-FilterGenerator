Blockly.Blocks['img_gray_bgrtogray'] = {
    init: function() {
	this.setHelpUrl('http://www.example.com/');
	this.appendValueInput("img")
	    .setCheck("Image_BGR")
	    .setAlign(Blockly.ALIGN_RIGHT)
	    .appendField("BGRToGray");
	this.setOutput(true, "Image_GRAY");
	this.setTooltip('');
    }
};

Blockly.Python['img_gray_bgrtogray'] = function(block) {
    var value_img = Blockly.Python.valueToCode(block, 'img', Blockly.Python.ORDER_ATOMIC);
    // TODO: Assemble Python into code variable.
    var code = 'cv2.cvtColor({0},CV_BGR2GRAY)'.format(value_img);
    var code = 'cv2.cvtColor({0},cv2.COLOR_BGR2GRAY)\n'.format(value_img);

    // TODO: Change ORDER_NONE to the correct strength.
    return [code, Blockly.Python.ORDER_NONE];
};


Blockly.Blocks['im_threshold'] = {
    init: function() {
	this.setHelpUrl('http://www.example.com/');
	this.appendValueInput("im_threshold")
            .appendField("Threshold :")
            .appendField(new Blockly.FieldTextInput("100"), "threshold");
	this.setOutput(true);
	this.setTooltip('');
    }
};

Blockly.Python['im_threshold'] = function(block) {
    var value_im_threshold = Blockly.Python.valueToCode(block, 'im_threshold', Blockly.Python.ORDER_ATOMIC);
    var text_threshold = block.getFieldValue('threshold');
    // TODO: Assemble Python into code variable.
    var code = 'cv2.threshold({0},{1},255,cv2.THRESH_BINARY)[1]'.format('{0}',text_threshold);
    var codeResult = Blockly.Python.joinCodesToOperator(value_im_threshold,'',code)
    // TODO: Change ORDER_NONE to the correct strength.
    return [codeResult, Blockly.Python.ORDER_NONE];
};



Blockly.Blocks['color_filter'] = {
  init: function() {
    this.setHelpUrl('http://www.example.com/');
    this.appendValueInput("inputA")
        .appendField(new Blockly.FieldHSV("#ff0000"), "Color");
    this.setOutput(true);
    this.setTooltip('');
  }
};


Blockly.Python['color_filter'] = function(block) {
  var value_inputA = Blockly.Python.valueToCode(block, 'inputA', Blockly.Python.ORDER_ATOMIC);
  var colour_color = block.getFieldValue('Color');
  var hexToRgb = function (hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? $.map(result,function(v,index){
	if(index == 0)
	    return null;
	return parseInt(v,16)
    }) :null;
  }
  var RGB2HSV = function(rgb){
      return 0;
  }
  var rgb = hexToRgb(colour_color)
  var h = RGB2HSV(rgb)
  // TODO: Assemble Python into code variable.
  var code = 'Filter.hueFilter({0},{1},10)\n'.format('{0}',h);
  var codeResult = Blockly.Python.joinCodesToOperator(value_inputA,'',code)

  // TODO: Change ORDER_NONE to the correct strength.
  return [codeResult, Blockly.Python.ORDER_NONE];
};
