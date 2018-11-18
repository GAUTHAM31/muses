var options = {
  valueNames: [ 'model-name', 'model-desc' ]
};

var modelList = new List('model-select', options);

$('.list-item').click(function(e) { 
	$('.selected').removeClass('selected');
    $(this).addClass('selected');
 });

var jsonInput = CodeMirror(document.getElementById("json-input"), {
  placeholder: "Enter JSON input here",
  mode:  "javascript",
  theme: "night"
});

var output = CodeMirror(document.getElementById("output"), {
  placeholder: "Output will appear here",
  mode:  "javascript",
  theme: "night"
});

var api_code = CodeMirror(document.getElementById("api_code"), {
  placeholder: "API code will appear here",
  mode:  "javascript",
  theme: "night"
});

Circles.create({
  id:           'circles-1',
  radius:       90,
  value:        43,
  maxValue:     100,
  width:        10,
  text:         function(value){return '<span class="percentage">' + value + '<span style="font-size: 30px">%</span></span>';},
  colors:       ['#2c393f', '#599eff'],
  duration:     400,
  wrpClass:     'circles-wrp',
  textClass:    'circles-text',
  styleWrapper: true,
  styleText:    true
})