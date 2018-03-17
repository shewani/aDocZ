# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 02:40:42 2018

@author: RashmithaY
"""

import zulip,sys,os
from wit import Wit
import utils
from typing import Any,Dict
class MyBot(object):
    def wit_query():
        client=Wit(access_token)
        resp=client.message('')
        print('Got the response:' + str(resp))
        
    def usage(self):
        return '''A personalised medical bot for medical assistance and customised suggestions based on current and previous health conditions'''
    def handle_message(self,message:Dict[str,str],bot_handler:Any)->None:
        res=[]
        query=""
        print(message["content"])
        if message["content"]=="help" :
            results.append(utils.HELP_MESSAGE)
        data=message["content"].split()
        query=data[0]
        if query=="Adocz" :
            res.append(self.wit_query())    
    
    
handler_class = MyBot
'''zulip-terminal C:/Users/RashmithaY/Desktop/zulipbot/zulipbot --bot-config-file C:/Users/RashmithaY/Desktop/zulipbot/zuliprc'''