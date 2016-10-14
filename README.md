<h1>Pybin</h1><br>
<p>Pybin is a Python script that interacts with pastebin.com from command line using pastebin <a href="http://pastebin.com/api">API</a>.<br><br><br></p>

<u><b><h2>Usage</b></h2></u><br>
./Pybin --help<br>
usage: pastebin [-h] [-S {paste,list,trends,delete,userdetails,show_paste}]<br>
                [-f FILE] [-s SYNTAX] [-e {N,10M,1H,1D,1W,2W,1M}] [-p {0,1,2}]<br>
                [-t TITLE] [-g] [-l LIST_LIMIT] [-d DELETE]<br>
<br>
Source code paste tool from command line<br>
<br>
optional arguments:<br>
  -h, --help            show this help message and exit<br>
  -S {paste,list,trends,delete,userdetails,show_paste}, --set_option {paste,list,trends,delete,userdetails,show_paste}<br>
                        Set an option for your request <br>
  -f FILE, --file FILE  Source Code file to share <br>
  -s SYNTAX, --syntax SYNTAX <br>
                        Paste's syntax <br>
  -e {N,10M,1H,1D,1W,2W,1M}, --expire {N,10M,1H,1D,1W,2W,1M}<br>
                        Paste's expire date <br>
  -p {0,1,2}, --privacy {0,1,2}<br>
                        Paste's privacy<br>
  -t TITLE, --title TITLE<br>
                        Paste's title<br>
  -g, --guest           Used to share a paste as a guest<br>
  -l LIST_LIMIT, --list_limit LIST_LIMIT<br>
                        Number of pastes to list, default 50<br>
  -d DELETE, --delete DELETE<br>
                        Paste's key to delete<br>
<br>
<br>
Example generating a pastebin link for source code file Hello.py that's in the same current working directory, with expiration date 1 hour, privacy Unlisted (code 1), and title "Hello World":<br>
<br>
./Pybin -S paste -f Hello.py -s python -e 1H -p 1 -t "Hello World"<br>
<br>
<br>
--------------------------------------------------------------------------
<b><u><h2>Note:</h2></u></b>
- You should provide your pastebin credentials by editing the source code file:<br>
P_USERNAME = "YOUR USERNAME HERE"<br>
P_PASSWORD = "YOUR PASSWORD HERE"<br>
P_DEV_KEY  = "YOUR DEVELOPER KEY HERE"<br>


