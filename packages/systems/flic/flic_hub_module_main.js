// main.js
var buttonManager = require("buttons");
var http = require("http");
//var url = "http://192.168.11.124:8123/api/events/flic";
var url = "http://192.168.11.124:8123/api/webhook/jh76fg45iugh54!-flic";
var url2 = "http://192.168.11.124:8123/api/webhook/8hg5fgY6!qo7xw-";

buttonManager.on("buttonSingleOrDoubleClickOrHold", function(obj) {
	var button = buttonManager.getButton(obj.bdaddr);
	var clickType = obj.isSingleClick ? "click" : obj.isDoubleClick ? "double_click" : "hold";
	
	http.makeRequest({
		url: url,
		method: "POST",
		headers: {"Content-Type": "application/json"},		
		content: JSON.stringify({"button_name": button.name, "click_type": clickType, "battery_status": button.batteryStatus }),				
	}, function(err, res) {
		console.log("request status-1: " + res.statusCode);
	});
	
	// sends a 2nd seperate request to allow triggered template sensors to have battery status
	http.makeRequest({
		url: url2 + button.name,
		method: "POST",
		headers: {"Content-Type": "application/json"},		
		content: JSON.stringify({"button_name": button.name, "click_type": clickType, "battery_status": button.batteryStatus }),				
	}, function(err, res) {
		console.log("sent: " + url2 + button.name);
		console.log("sent: " + button.batteryStatus);		
		console.log("request status-2: " + res.statusCode);
	});	
});

console.log("Started");
