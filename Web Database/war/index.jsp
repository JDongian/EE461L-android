<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<%@ page import="com.google.appengine.api.users.User" %>

<%@ page import="com.google.appengine.api.users.UserService" %>

<%@ page import="com.google.appengine.api.users.UserServiceFactory;" %>

<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>




<html lang="en">
	<head>
		<link rel="stylesheet" media="screen" href="../assets/css/style.css">

		<title>Database Login</title>
		

	</head>
	<body>
		
		
		
		
<%  	String guestbookName = request.getParameter("guestbookName");

    if (guestbookName == null) {

        guestbookName = "default";

    }

    pageContext.setAttribute("guestbookName", guestbookName);

    UserService userService = UserServiceFactory.getUserService();

    User user = userService.getCurrentUser();

    if (user != null) {

      pageContext.setAttribute("user", user);
      
    }

%>
		
		
		
		
			
			
	<header>
		<div id="particles-js"></div>
		<div class="lj-overlay lj-overlay-color">
			<div class="toprow" style="position:absolute; left:40px; top:40px; onclick="location.href = "index.html";" onmouseover="" style="cursor: pointer;">
				<h1 id="logo">OneBase</h1>
			</div>
		</div>
		
		
			
	</header>
		
		<div id="wrapper" style="text-align: center">
			<div class="login-box">
				<div class="box-header"><br>
				<h2>Log In</h2>
				<br>
				</div>
				<label for="username">Username</label>
				<br/>
				<input id="input" type="text" id="username">
				<br/>
				<label for="password">Password</label>
				<br/>
				<input id="input" type="password" id="password">
				<br/>
				<button id="normal" type="submit">Sign In</button>
				<br/>
				or
				<br/>
				<input id="normal" type="image" src="assets/Sign-in-with-Google.png" alt="Submit" height="30px" width="155px">
			</div>
		</div>
		
		

		


		<script src="../assets/js/particles.js"></script>
		<script src="../assets/js/app.js"></script>
		<script src="https://apis.google.com/js/platform.js" async defer></script>
	</body>

</html>
