#!/usr/bin/env python2
# -*- coding: utf-8 -*-
try:
	import urllib,requests,os,argparse
except ImportError,err:
	print "[~]Invalid Module(s) !"
	print "[~]%s ." % err
	exit(-1)

__version__ = 0.1


'''
	Defining core functions and data structures
	
	-syntax_list 	: Contains a list of valid syntax supported by Pastebin
	-P_DEV_KEY 	 	: Contains user's development key
	-P_USERNAME 	: Contains user's username
	-P_PASSWORD		: Contains user's password 
'''

P_USERNAME = ""		# Your Pastebin username
P_PASSWORD = ""		# Your Pastebin password
P_DEV_KEY  = ""		# Your Pastebin Developer key

API_URI = {
	"api_login"		: 
		{
			'link' 		: "http://pastebin.com/api/api_login.php",
			'fields' 	:
				{
					'api_dev_key' 		: '',
					'api_user_name'		: '',
					'api_user_password'	: ''
				}
		},
	"api_post"		: 
		{
			'link'		: "http://pastebin.com/api/api_post.php",
			'fields'	: [
				{
					'type'				: 'paste',
					'fields'			:
						{
							'api_dev_key'			: '',
							'api_option'			: 'paste',
							'api_paste_code'		: '',
							'api_user_key'			: '',
							'api_paste_name'		: '',
							'api_paste_format'		: '',
							'api_paste_private' 	: '',
							'api_paste_expire_date'	: ''
						}
				},
				{
					'type'				: 'list',
					'fields'			:
						{
							'api_dev_key'			: '',
							'api_user_key'			: '',
							'api_results_limit'		: '50',
							'api_option'			: 'list'
						}
				},
				{
					'type'				: 'trends',
					'fields'			:
						{
							'api_dev_key'			: '',
							'api_option'			: 'trends'
						}
				},
				{
					'type'				: 'delete',
					'fields'			:
						{
							'api_dev_key'			: '',
							'api_option'			: 'delete',
							'api_user_key'			: '',
							'api_paste_key'			: ''
						}
				},
				{
					'type'				: 'userdetails',
					'fields'			:
						{
							'api_dev_key'			: '',
							'api_option'			: 'userdetails',
							'api_user_key'			: ''
						}
				}
		] 
		} ,
	"show_paste"	: 
		{
			'link'		: "http://pastebin.com/api/api_raw.php",
			'fields'	:
				{
					'api_dev_key'		: '',
					'api_option'		: 'show_paste',
					'api_user_key'		: '',
					'api_paste_key'		: ''
				}
		}
	}
		
API_OPTIONS = ['paste','list','trends','delete','userdetails']

#
		
syntax_list = ['4cs', '6502acme', '6502kickass', '6502tasm', 'abap', 'actionscript', 'actionscript3', 'ada', 'aimms', 'algol68', 'apache', 'applescript', 'apt_sources', 'arm', 'asm', 'asp', 'asymptote', 'autoconf', 'autohotkey', 'autoit', 'avisynth', 'awk', 'bascomavr', 'bash', 'basic4gl', 'dos', 'bibtex', 'blitzbasic', 'b3d', 'bmx', 'bnf', 'boo', 'bf', 'c', 'c_winapi', 'c_mac', 'cil', 'csharp', 'cpp', 'cpp-winapi', 'cpp-qt', 'c_loadrunner', 'caddcl', 'cadlisp', 'cfdg', 'chaiscript', 'chapel', 'clojure', 'klonec', 'klonecpp', 'cmake', 'cobol', 'coffeescript', 'cfm', 'css', 'cuesheet', 'd', 'dart', 'dcl', 'dcpu16', 'dcs', 'delphi', 'oxygene', 'diff', 'div', 'dot', 'e', 'ezt', 'ecmascript', 'eiffel', 'email', 'epc', 'erlang', 'euphoria', 'fsharp', 'falcon', 'filemaker', 'fo', 'f1', 'fortran', 'freebasic', 'freeswitch', 'gambas', 'gml', 'gdb', 'genero', 'genie', 'gettext', 'go', 'groovy', 'gwbasic', 'haskell', 'haxe', 'hicest', 'hq9plus', 'html4strict', 'html5', 'icon', 'idl', 'ini', 'inno', 'intercal', 'io', 'ispfpanel', 'j', 'java', 'java5', 'javascript', 'jcl', 'jquery', 'json', 'julia', 'kixtart', 'latex', 'ldif', 'lb', 'lsl2', 'lisp', 'llvm', 'locobasic', 'logtalk', 'lolcode', 'lotusformulas', 'lotusscript', 'lscript', 'lua', 'm68k', 'magiksf', 'make', 'mapbasic', 'matlab', 'mirc', 'mmix', 'modula2', 'modula3', '68000devpac', 'mpasm', 'mxml', 'mysql', 'nagios', 'netrexx', 'newlisp', 'nginx', 'nimrod', 'text', 'nsis', 'oberon2', 'objeck', 'objc', 'ocaml-brief', 'ocaml', 'octave', 'oorexx', 'pf', 'glsl', 'oobas', 'oracle11', 'oracle8', 'oz', 'parasail', 'parigp', 'pascal', 'pawn', 'pcre', 'per', 'perl', 'perl6', 'php', 'php-brief', 'pic16', 'pike', 'pixelbender', 'pli', 'plsql', 'postgresql', 'postscript', 'povray', 'powershell', 'powerbuilder', 'proftpd', 'progress', 'prolog', 'properties', 'providex', 'puppet', 'purebasic', 'pycon', 'python', 'pys60', 'q', 'qbasic', 'qml', 'rsplus', 'racket', 'rails', 'rbs', 'rebol', 'reg', 'rexx', 'robots', 'rpmspec', 'ruby', 'gnuplot', 'rust', 'sas', 'scala', 'scheme', 'scilab', 'scl', 'sdlbasic', 'smalltalk', 'smarty', 'spark', 'sparql', 'sqf', 'sql', 'standardml', 'stonescript', 'sclang', 'swift', 'systemverilog', 'tsql', 'tcl', 'teraterm', 'thinbasic', 'typoscript', 'unicon', 'uscript', 'upc', 'urbi', 'vala', 'vbnet', 'vbscript', 'vedit', 'verilog', 'vhdl', 'vim', 'visualprolog', 'vb', 'visualfoxpro', 'whitespace', 'whois', 'winbatch', 'xbasic', 'xml', 'xorg_conf', 'xpp', 'yaml', 'z80', 'zxbasic' ]


if __name__ == "__main__":
	ArgumentHandler = argparse.ArgumentParser( description = "Source code paste tool from terminal" )
	ArgumentHandler.add_argument( "-S", "--set_option", help = "Set an option for your request", choices = ['paste','list','trends','delete','userdetails','show_paste'])
	ArgumentHandler.add_argument( "-f", "--file", help = "Source code file to share" )
	ArgumentHandler.add_argument( "-s", "--syntax", help = "Paste's syntax" )
	ArgumentHandler.add_argument( "-e", "--expire", help = "Paste's expire date", choices = ['N','10M','1H','1D','1W','2W','1M'] )
	ArgumentHandler.add_argument( "-p", "--privacy", help = "Paste's privacy", choices = ['0','1','2'])
	ArgumentHandler.add_argument( "-t", "--title", help = "Paste's title" )
	ArgumentHandler.add_argument( "-g", "--guest", help = "Used to share a paste as a guest", action = "store_true" )
	ArgumentHandler.add_argument( "-l", "--list_limit", help = "Number of pastes to list, default 50")
	ArgumentHandler.add_argument( "-d", "--delete", help = "Paste's key to delete")
	
	args = ArgumentHandler.parse_args()
	
	if args.set_option == None:
		print "[!] You must specify an option!\n\n"
		exit(-1)
	if (args.set_option == 'paste') and (args.file == None):
		print "[!] You must specify a file!\n\n"
		exit(-1)
	if (args.set_option == 'delete') and (args.delete == None):
		print "[!] You must specify a paste key to delete!\n\n"
		exit(-1)
	if (args.set_option == 'paste' ) and (args.syntax not in syntax_list):
		print "[!] Invalid syntax identifier, please check out the syntax identifier list!\n\n"
		exit(-1)
	if args.syntax == None:
		args.syntax = ''
	if args.expire == None:
		args.expire = 'N'
	if args.privacy == None:
		args.privacy = '0'
	if args.title == None:
		args.title = ''
	
	
	API_URI['api_login']['fields']['api_dev_key'] = P_DEV_KEY
	API_URI['api_login']['fields']['api_user_name'] = P_USERNAME
	API_URI['api_login']['fields']['api_user_password'] = P_PASSWORD
	
	try:
		req = requests.post( API_URI['api_login']['link'], data = API_URI['api_login']['fields'] )
		user_key = req.text
	except:
		print "[!] Cannot complete the login request\n\n"
		exit(-1)
	
	if args.set_option == "paste":
		try:
			paste_file = open( args.file, "r" )
		except:
			print "[!] Canno open the specified file\n\n"
			exit(-1);

		API_URI['api_post']['fields'][0]['fields']['api_dev_key'] = P_DEV_KEY
		API_URI['api_post']['fields'][0]['fields']['api_paste_code'] = paste_file.read()
		API_URI['api_post']['fields'][0]['fields']['api_paste_private'] = args.privacy
		API_URI['api_post']['fields'][0]['fields']['api_paste_name'] = args.title
		API_URI['api_post']['fields'][0]['fields']['api_paste_expire_date'] = args.expire
		API_URI['api_post']['fields'][0]['fields']['api_paste_format'] = args.syntax
		API_URI['api_post']['fields'][0]['fields']['api_user_key'] = ( "" if args.guest else user_key )
	
		try:
			req = requests.post( API_URI['api_post']['link'], data = API_URI['api_post']['fields'][0]['fields'] )
			paste_link = req.text
		except:
			print "[!] Cannot complete the post request\n\n"
			exit(-1)
		print "[~] Paste link: %s \n\n" % (paste_link)
	
	elif args.set_option == "delete":
		
		API_URI['api_post']['fields'][3]['fields']['api_dev_key'] = P_DEV_KEY
		API_URI['api_post']['fields'][3]['fields']['api_user_key'] = user_key
		API_URI['api_post']['fields'][3]['fields']['api_paste_key'] = args.delete
		
		try:
			req = requests.post( API_URI['api_post']['link'], data = API_URI['api_post']['fields'][3]['fields'])
			print req.text
		except:
			print "[!] Cannot delete this paste!\n\n"
			exit(-1)
			
	elif args.set_option == "trends":
		API_URI['api_post']['fields'][2]['fields']['api_dev_key'] = P_DEV_KEY
		
		try:
			req = requests.post( API_URI['api_post']['link'], data = API_URI['api_post']['fields'][2]['fields'])
			print req.text
		except:
			print "[!] Cannot list trending pastes!\n\n"
			exit(-1)
