<h1>Pybin</h1><br>
<p>Pybin is a Python script that interacts with pastebin.com from command line using pastebin <a href="http://pastebin.com/api">API</a>.<br><br><br></p>

<u><b><h2>Usage</b></h2></u><br>
<img src="https://i.imgur.com/I9FFemt.png" height="480" width="1000"> </img>
<br>
Example generating a pastebin link for source code file Hello.py that's in the same current working directory, with expiration date 1 hour, privacy Unlisted (code 1), and title "Hello World":

./Pybin -S paste -f Hello.py -s python -e 1H -p 1 -t "Hello World"

</p>
--------------------------------------------------------------------------
<b><u><h2>Note:</h2></u></b>
- You should provide your pastebin credentials by editing the source code file:<br>
P_USERNAME = "YOUR USERNAME HERE"<br>
P_PASSWORD = "YOUR PASSWORD HERE"<br>
P_DEV_KEY  = "YOUR DEVELOPER KEY HERE"<br>


