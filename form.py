#coding:utf-8
import cgi
 
print ("Content-Type: text/html; charset=utf-8\n\n")
 
html = """
<!DOCTYPE html>
<html>
<head>


<title>Page Title</title>

<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<!------ Include the above in your HEAD tag ---------->


    
   	<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">

<style>
/*Contact sectiom*/


.content-header{
    font-family: 'Oleo Script', cursive;
    color:#fcc500;
    font-size: 45px;
  }
  
  .section-content{
    text-align: center; 
  
  }
  body{
      
      font-family: 'Teko', sans-serif;
    padding-top: 60px;
    width: 100%;
    width: 100vw;
    
    background: #3a6186; /* fallback for old browsers */
    background: -webkit-linear-gradient(to left, #3a6186 , #89253e); /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to left, #3a6186 , #89253e); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
      color : #fff;    
  }
  .contact-section{
    padding-top: 40px;
  }
  .contact-section .col-md-6{
    width: 50%;
  }
  
  .form-line{
    border-right: 1px solid #B29999;
  }
  
  .form-group{
    margin-top: 10px;
  }
  label{
    font-size: 1.3em;
    line-height: 1em;
    font-weight: normal;
  }
  .form-control{
    font-size: 1.3em;
    color: #080808;
  }
  textarea.form-control {
      height: 135px;
     /* margin-top: px;*/
  }
  
  .submit{
    font-size: 1.1em;
    float: right;
    width: 150px;
    background-color: transparent;
    color: #fff;
  
  }
  

</style>
</head>
<body>

<section id="contact">

			
  

			<div class="contact-section">
            
			<div class="container">
            <div class="section-content">
				<h1>Contactez-nous</h1>
			</div>
				<form action="/formHandler.py" method="POST">
					<div class="col-md-6 form-line">
			  			<div class="form-group">
			  				<label for="userNameInputId">Nom et prénom (*) :</label>
					    	<input type="text" class="form-control" name="userNameInput" id="userNameInputId" placeholder="Votre nom et prénom">
				  		</div>
				  		<div class="form-group">
					    	<label for="emailInput">Email :</label>
					    	<input type="email" class="form-control" id="emailInputId" name"emailInput" placeholder=" Votre email">
					  	</div>	
					  	<div class="form-group">
					    	<label for="phone">Téléphone :</label>
					    	<input type="tel" class="form-control" name="phoneInput" id="phoneInputId" placeholder=" Votre numéro de téléphone">
			  			</div>
			  		</div>
			  		<div class="col-md-6">
			  			<div class="form-group">
			  				<label for ="description">Message (*) :</label>
			  			 	<textarea  class="form-control" id="messageTextId"  name="messageText" placeholder="Votre message"></textarea>
			  			</div>
			  			<div>
                          <input type="submit" class="btn btn-default submit fa fa-paper-plane" value="Envoyer">
			  				
			  			</div>
			  			
					</div>
				</form>
			</div>
		</section>

</body>
</html>





"""
 
print(html)