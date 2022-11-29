var express=require("express");
var bodyParser=require("body-parser");
var passport = require("passport");
var LocalStrategy = require("passport-local");
var passportLocalMongoose = require("passport-local-mongoose");


const mongoose = require('mongoose');
mongoose.connect('mongodb://0.0.0.0:27017/smart');
var db=mongoose.connection;
db.on('error', console.log.bind(console, "connection error"));
db.once('open', function(callback){
	console.log("connection succeeded");
})

var app=express()


app.use(bodyParser.json());
app.use(express.static('MainPages'));
app.use(bodyParser.urlencoded({
	extended: true
}));

app.post('/sign_up', function(req,res){
	var name = req.body.name;
	var email =req.body.email;
	var pass = req.body.password;
	var phno =req.body.phno;
    var username =req.body.username;

	var data = {
		"name": name,
		"email":email,
        "username":username,
		"password":pass,
		"phno":phno
	}
db.collection('details').insertOne(data,function(err, collection){
		if (err) throw err;
		console.log("Record inserted Successfully");
			
	});
		
	return res.redirect('');
})
app.get("/login", function (req, res) {
	res.render("login");
});

app.post("/login", function (req, res){
    
}) 



app.get('/',function(req,res){
res.set({
	'Access-control-Allow-Origin': '*'
	});
return res.redirect('DashBoard\index.html');
}).listen(3000)


console.log("server listening at port 3000");
