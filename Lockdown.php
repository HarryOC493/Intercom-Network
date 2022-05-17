<?php

    $Username = $_POST['Username1'];
    $Password = $_POST['Password1'];

    $Servername = 'some-mysql';
    $SqlUsername = 'root';
    $SqlPassword = 'dev22';
    $DbName = 'CETSS';

    // Create connection
    $conn = new mysqli($Servername, $SqlUsername, $SqlPassword);

    // Check connection
    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    } 
    echo "Connected successfully";

?>

    <html>
    <Head>
        <title>Intercom Admin</title>
    </Head>
    <style>
        body {
            background-color: #293345;
        }

        #container1 { position: relative; 
            /* updated to support footer push */
            min-height: 30%;
            padding-bottom: 60px; /* must be the same as footer height */
            box-sizing: border-box;
            -webkit-box-sizing: border-box;
        }
        #below { 
            height: -10px;
        }

        footer { 
            position: absolute;
            bottom: -10;
            left: -10;
            width: 105%;
            color: white;
            text-align: center;
            background-color: #333;
            font-family: 'Cambria', monospace;
        }


        .NAvUl {
          list-style-type: none;
          margin: -10;
          padding: 0;
          overflow: hidden;
          background-color: #333;
          text-align: center;
        }
        
        .NavLi {
          float: center;
        }
        
        .NavLi p {
          display: block;
          color: white;
          padding: 14px 16px;
          text-decoration: none;
          display: inline-block;
          font-family: 'Courier New', monospace;
        }
        body h1 {
            padding: 15px;
            padding-bottom: 1px;
            text-align: center;
            color: white;
            font-size: 30px;
            font-family: Rockwell;
        }
        body h2 {
            text-align: center;
            color: white;
            font-size: 18px;
            letter-spacing: 1px;
            font-family: Optima;
        }

        .Container {
            vertical-align: top;
            display: inline-block;
            border: solid;
            border-color: white;
            padding-left: 20px;
            padding-right: 20px;
            text-align: center;
        }

        .Container h3 {
            text-align: left;
            font-family: copperplate;
            font-size: 12px;
            color: #dddeca;
        }
        .ProfilePng {
            border-radius: 50%;
        }

        .InfoContainer {
            vertical-align: top;
            display: inline-block;
            border: solid;
            border-color: white;
            padding-left: 20px;
            padding-right: 20px;
            text-align: left;
            color: #dddeca;
            font-family: 'monaco';
            font-size: 9px;
        }

        .InfoContainer ul {
            list-style-type: square;
            font-size: 12px;
        }

        .ActionContainer {
            width: 55%;
            vertical-align: top;
            display: inline-block;
            border: solid;
            border-color: white;

            text-align: left;
            color: #dddeca;
            font-family: 'monaco';
            font-size: 9px;

        }

        .switch {
            position: relative;
            display: inline-block;
            width: 40px;
            height: 25px;
        }

        .switch input { 
            opacity: 0;
            width: 0;
            height: 15;
        }

        .slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            -webkit-transition: .4s;
            transition: .4s;
            border-radius: 35%;
        }

        .slider:before {
            position: absolute;
            content: '';
            height:18px;
            width: 18px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            -webkit-transition: .4s;
            transition: .4s;
            border-radius: 50%;
        }

        input:checked + .slider {
            background-color: #2196F3;
        }

            input:focus + .slider {
            box-shadow: 0 0 1px #2196F3;
        }

        input:checked + .slider:before {
            -webkit-transform: translateX(13px);
            -ms-transform: translateX(13px);
            transform: translateX(13px);
        }

        hr.solid {
            border-top: 1.5px solid #bbb;
            border-radius: 75%;
            width: 90%;
        }

        .ActionContainer h5{
            font-size: 12px;
            margin-left: 5%;
        }

        .ActionContainer h6{
            font-size: 8px;
            margin-left: 5%;
            font-style: italic;
        }

        a {
            color: #46d141;
        }

        .checkbox {
            color: #bbb

        }

        .submit {
            color: white;
            background-color: #072e09;
            border-radius: 25%;
            width: 100px;
        }
        
        .LockDownBtn {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            display: inline;
            margin-left: 10%;
            color: white;
            background-color: red;
        }

        @keyframes glowing {
            0% {
            background-color: red;
            }

            100% {
            background-color: transparent;
            }
        }

        @keyframes glowing1 {
            0% {
            background-color: red;
            }

            100% {
            background-color: orange;
            }
        }

        .LockdownForm:hover .Button1 {
            animation: glowing1 100ms infinite;
        }
        .LockdownForm:hover .LockdownLogin {
            animation: glowing1 100ms infinite;
        }

        .LoginInfo {
            width: 100px;
            height: 25px;
            border-radius: 10%;
            background-color: #bbb;
        }

        .placeholder {
            color: white; 
            opacity: 1;
        }
    </style>
    </head>
    <body>
        
        <ul class='NavUl'>
          <li class='NavLi'><p>CETSS Intercom System</p></li>
        </ul>

        <h1><?php echo '"Welcome To: " . $Username . "'?></h1>
        <!--<h2>Here you can send messages to any class you like, overwrite rain indicators, inicate a schoolwide lockdown and more(Comming Soon)</h2>-->
        </h1>
        
    </body>
    <div id='container1'>
        <footer><p><br>Website By Harry O'Connor<br><br>Intercom Network by: Harry O'Connor | Cael Cheers | Jack Dennehy<br><br></p></footer>
    </div>
    <div id='below'></div>
    </html>"

    ?>
