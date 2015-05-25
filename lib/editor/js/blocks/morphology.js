Blockly.Blocks['cv_erosion'] = {
    init: function() {
        this.setHelpUrl('http://www.example.com/');
        this.appendValueInput("NAME")
            .appendField("Erosion: Kernel =")
            .appendField(new Blockly.FieldTextInput("5"), "SIZE");
        this.setOutput(true);
        this.setTooltip('');
    }
};

Blockly.Python['cv_erosion'] = function(block) {
    var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_NONE);
    var text_size = block.getFieldValue('SIZE');
    // TODO: Assemble Python into code variable.
    var code = [];
    var kernel_name = "kernel_{0}".format(orgFunc.randStr())
        code.push('{1} = np.ones(({0},{0}),np.uint8)\n'.format(text_size,kernel_name))
        code.push( Blockly.Python.joinCodesToOperator(value_name,'','cv2.erode({0},{1},iterations = 1)\n'.format('{0}',kernel_name)))
        //code.push('cv2.erode({0},{1},iterations = 1)\n'.format(value_name,kernel_name))
        var str_code =code.join("\n");
    // TODO: Change ORDER_NONE to the correct strength.
    return [str_code, Blockly.Python.ORDER_MEMBER];
};

Blockly.Blocks['cv_dilation'] = {
    init: function() {
        this.setHelpUrl('http://www.example.com/');
        this.appendValueInput("NAME")
            .appendField("Dilation: Kernel =")
            .appendField(new Blockly.FieldTextInput("5"), "SIZE");
        this.setOutput(true);
        this.setTooltip('');
    }
};

Blockly.Python['cv_dilation'] = function(block) {
    var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_NONE);
    var text_size = block.getFieldValue('SIZE');
    // TODO: Assemble Python into code variable.
    var code = [];
    var kernel_name = "kernel_{0}".format(orgFunc.randStr())
        code.push('{1} = np.ones(({0},{0}),np.uint8)\n'.format(text_size,kernel_name))
        code.push('cv2.dilate({0},{1},iterations = 1)\n'.format(value_name,kernel_name))
        var str_code =code.join("\n");
    // TODO: Change ORDER_NONE to the correct strength.
    return [str_code, Blockly.Python.ORDER_MEMBER];
};


Blockly.Blocks['cv_opening'] = {
    init: function() {
        this.setHelpUrl('http://www.example.com/');
        this.appendValueInput("NAME")
            .appendField("Opening: Kernel =")
            .appendField(new Blockly.FieldTextInput("5"), "SIZE");
        this.setOutput(true);
        this.setTooltip('');
    }
};

Blockly.Python['cv_opening'] = function(block) {
    var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_NONE);
    var text_size = block.getFieldValue('SIZE');
    // TODO: Assemble Python into code variable.
    var code = [];
    var kernel_name = "kernel_{0}".format(orgFunc.randStr())
        code.push('{1} = np.ones(({0},{0}),np.uint8)\n'.format(text_size,kernel_name))
        code.push('cv2.morphologyEx({0},cv2.MORPH_OPEN,{1})\n'.format(value_name,kernel_name))
        var str_code =code.join("\n");
    // TODO: Change ORDER_NONE to the correct strength.
    return [str_code, Blockly.Python.ORDER_MEMBER];
};



Blockly.Blocks['cv_closing'] = {
    init: function() {
        this.setHelpUrl('http://www.example.com/');
        this.appendValueInput("NAME")
            .appendField("Closing: Kernel =")
            .appendField(new Blockly.FieldTextInput("5"), "SIZE");
        this.setOutput(true);
        this.setTooltip('');
    }
};

Blockly.Python['cv_closing'] = function(block) {
    var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_NONE);
    var text_size = block.getFieldValue('SIZE');
    // TODO: Assemble Python into code variable.
    var code = [];
    var kernel_name = "kernel_{0}".format(orgFunc.randStr())
        code.push('{1} = np.ones(({0},{0}),np.uint8)\n'.format(text_size,kernel_name))
        code.push('cv2.morphologyEx({0},cv2.MORPH_CLOSE,{1})\n'.format(value_name,kernel_name))
        var str_code =code.join("\n");
    // TODO: Change ORDER_NONE to the correct strength.
    return [str_code, Blockly.Python.ORDER_MEMBER];
};


