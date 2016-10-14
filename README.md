<h1>Pybin</h1><br>
<p>Pybin is a Python script that interacts with pastebin.com from command line using pastebin <a href="http://pastebin.com/api">API</a>.<br><br><br></p>

<u><b><h2>Usage</b></h2></u><br>
<p>./Pybin --help
usage: pastebin [-h] [-S {paste,list,trends,delete,userdetails,show_paste}]
                [-f FILE] [-s SYNTAX] [-e {N,10M,1H,1D,1W,2W,1M}] [-p {0,1,2}]
                [-t TITLE] [-g] [-l LIST_LIMIT] [-d DELETE]

Source code paste tool from command line

optional arguments:
  -h, --help            show this help message and exit
  -S {paste,list,trends,delete,userdetails,show_paste}, --set_option {paste,list,trends,delete,userdetails,show_paste}
                        Set an option for your request
  -f FILE, --file FILE  Source Code file to share
  -s SYNTAX, --syntax SYNTAX
                        Paste's syntax
  -e {N,10M,1H,1D,1W,2W,1M}, --expire {N,10M,1H,1D,1W,2W,1M}
                        Paste's expire date
  -p {0,1,2}, --privacy {0,1,2}
                        Paste's privacy
  -t TITLE, --title TITLE
                        Paste's title
  -g, --guest           Used to share a paste as a guest
  -l LIST_LIMIT, --list_limit LIST_LIMIT
                        Number of pastes to list, default 50
  -d DELETE, --delete DELETE
                        Paste's key to delete


Example generating a pastebin link for source code file Hello.py that's in the same current working directory, with expiration date 1 hour, privacy Unlisted (code 1), and title "Hello World":

./Pybin -S paste -f Hello.py -s python -e 1H -p 1 -t "Hello World"

</p>
--------------------------------------------------------------------------
<b><u><h2>Note:</h2></u></b>
- You should provide your pastebin credentials by editing the source code file:<br>
P_USERNAME = "YOUR USERNAME HERE"<br>
P_PASSWORD = "YOUR PASSWORD HERE"<br>
P_DEV_KEY  = "YOUR DEVELOPER KEY HERE"<br>


