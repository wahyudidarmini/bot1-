# -*- coding: utf-8 -*-

import TOBY
from TOBY.lib.curve.ttypes import *
from datetime import datetime
import time,datetime,random,sys,re,os,json,subprocess,codecs,threading,glob

cl = TOBY.LINE()
cl.login(token="En9hx4y9BouKrcqBgrW2.AZs3a8Vf+ipnhLTOmQbtuG./pihHAssaz6gq8UFmimEnmZDziv8PuMI4++5Thy7nM0=")
cl.loginResult()

ki = TOBY.LINE()
ki.login(token="EnLIr6bNukLYv900T6c8.6aZTpsG37MxD+MqNsJxP6a.J1lbC/Zi4O+vkQg7M8T3vgi5HsFOX1yTMTcxnqWwqn4=")
ki.loginResult()

ki2 = TOBY.LINE()
ki2.login(token="EnRaRjLOTIYdcTEgb3t8.pIfscrd8L4dj1jrbrT2fca.LibQh1eMYStQdd4rkRVqTZyidACPFOqENjfIKz0y+Cs=")
ki2.loginResult()

ki3 = TOBY.LINE()
ki3.login(token="EnoTHBKNfQjnN7RXeJ6f.TxpN+3FqpfVz0URVVjPPxW.Y8ffue3uzJ9+MZvsZxQv+1yXpr7rPeJyxZIbYCX4Rfg=")
ki3.loginResult()

ki4 = TOBY.LINE()
ki4.login(token="EnAzPcQXJeglxiqAzFt4.DPUJL7N9FlH3q14qZJ5r5a.FPBT93MnyjDqwLrNZr3Fvz21Dl23Okh6++AeEB3wRFc=")
ki4.loginResult()

ki5 = TOBY.LINE()
ki5.login(token="EnHfwhDq9vK7IKV5DTp4.+Bc/Zlua/rxta3RDE9Qfra.7yYEKu0CIhg7OObLzjtLJc/5uEdDAeqOF2U/KUe0tOk=")
ki5.loginResult()

ki6 = TOBY.LINE()
ki6.login(token="EnwMMC8xDbTL4ckcYNH8.0LFAw+X66CVCLF7PSB30Qa.qLqjsqECNgos1N3ZAgBpbj/hOHUReiIdJzoybf661tY=")
ki6.loginResult()

ki7 = TOBY.LINE()
ki7.login(token="EnyKrwvSoVblLIKpTL31.hm/n508o500AIsyh+lXvmq.1CMxnMd52Uue8A0hmPenifVZ1yD5YubwZ/wQKyEHqUI=")
ki7.loginResult()

ki8 = TOBY.LINE()
ki8.login(token="EnU8PxnHFyrZhXXYkP88.5Gss6Cj7IBEXrUFBawm9oa.VUdSQtCF7gdJy7dKipuhoFlqo28yJtFwDJA1Zhuyh+E=")
ki8.loginResult()

ki9 = TOBY.LINE()
ki9.login(token="EnYRAhLylfdTQuuOHHf3.SO/fObQ10CshHFFY0L3meW.TWi/eQ5UaSo2pX79Tmyms6C4I2tuIF6LrmqLO217s7Y=")
ki9.loginResult()

ki10 = TOBY.LINE()
ki10.login(token="EnRl9lRnJSrizZzVYaL1.F998qotUGTGQIRjcj/3fKq.ygoutzb1c+LtS2AXp/NZ5+c2D2HEI4tr+JJ9F41AfRs=")
ki10.loginResult()

ki11 = TOBY.LINE()
ki11.login(token="EnPJakWiVt7MMdJjofg7.8DHCNR+5ggo//QiQT7pj9W.wIGtq9HZqsWyR/SzuWn3xnzhLuhf40iSRIKjN/KRRxc=")
ki11.loginResult()

ki12 = TOBY.LINE()
ki12.login(token="En9b8bh3juUFV1SHOtqd.rOli1dtiBis50MI658yqRq.O91BvrS4ofxXU5GfhcGFs/eeN7O9HYHiEkC9GoGSi1w=")
ki12.loginResult()

ki13 = TOBY.LINE()
ki13.login(token="En07EbJJbrlxuOlJ6Go0.JAwaMojSWCnrhb405Gw7Sa.d4ed75AGPej2rInsnKSgjE/nwv5S2hJi+Wv0nPMAtGw=")
ki13.loginResult()

ki14 = TOBY.LINE()
ki14.login(token="EndQaONNqiyXgWRk0nO2.kJj6gKL1avGlp7iF9MY8KG.atHwdmHdB079XSdZ9QtVkiek6CGwaBWDmM1Fhwh1PkM=")
ki14.loginResult()

ki15 = TOBY.LINE()
ki15.login(token="EnfFz5cD8tXkYNoGTR84.hz3BUHBhWs9y9M66OUsVXa.8t2rgeHVKXFXWoL7SoHF70Yjbaw5+VdiLPX9CotxA7A=")
ki15.loginResult()

ki16 = TOBY.LINE()
ki16.login(token="EnLmnk74dGVeobCxHjy6.zbzLgObFSJIgQgJQvcBBPG.QOZFU2NUBXZ+iv2Kdq59qddPgl3JvjRCl3IWCo47geg=")
ki16.loginResult()

ki17 = TOBY.LINE()
ki17.login(token="EnxsqCL3DhYeIVaYocL4.4tpKgyQpvX03tq+Nc2O81a.YiP01ZMhSECrB4DEbBEu8Pma3mEMXfpoBq/GBmV5p6A=")
ki17.loginResult()

ki18 = TOBY.LINE()
ki18.login(token="EnxsqCL3DhYeIVaYocL4.4tpKgyQpvX03tq+Nc2O81a.YiP01ZMhSECrB4DEbBEu8Pma3mEMXfpoBq/GBmV5p6A=")
ki18.loginResult()

ki19 = TOBY.LINE()
ki19.login(token="En9hx4y9BouKrcqBgrW2.AZs3a8Vf+ipnhLTOmQbtuG./pihHAssaz6gq8UFmimEnmZDziv8PuMI4++5Thy7nM0=")
ki19.loginResult()

ki20 = TOBY.LINE()
ki20.login(token="EnLIr6bNukLYv900T6c8.6aZTpsG37MxD+MqNsJxP6a.J1lbC/Zi4O+vkQg7M8T3vgi5HsFOX1yTMTcxnqWwqn4=")
ki20.loginResult()

ki21 = TOBY.LINE()
ki21.login(token="EnRaRjLOTIYdcTEgb3t8.pIfscrd8L4dj1jrbrT2fca.LibQh1eMYStQdd4rkRVqTZyidACPFOqENjfIKz0y+Cs=")
ki21.loginResult()

ki22 = TOBY.LINE()
ki22.login(token="EnoTHBKNfQjnN7RXeJ6f.TxpN+3FqpfVz0URVVjPPxW.Y8ffue3uzJ9+MZvsZxQv+1yXpr7rPeJyxZIbYCX4Rfg=")
ki22.loginResult()

ki23 = TOBY.LINE()
ki23.login(token="EnAzPcQXJeglxiqAzFt4.DPUJL7N9FlH3q14qZJ5r5a.FPBT93MnyjDqwLrNZr3Fvz21Dl23Okh6++AeEB3wRFc=")
ki23.loginResult()

ki24 = TOBY.LINE()
ki24.login(token="EnHfwhDq9vK7IKV5DTp4.+Bc/Zlua/rxta3RDE9Qfra.7yYEKu0CIhg7OObLzjtLJc/5uEdDAeqOF2U/KUe0tOk=")
ki24.loginResult()

ki25 = TOBY.LINE()
ki25.login(token="EnwMMC8xDbTL4ckcYNH8.0LFAw+X66CVCLF7PSB30Qa.qLqjsqECNgos1N3ZAgBpbj/hOHUReiIdJzoybf661tY=")
ki25.loginResult()

ki26 = TOBY.LINE()
ki26.login(token="EnyKrwvSoVblLIKpTL31.hm/n508o500AIsyh+lXvmq.1CMxnMd52Uue8A0hmPenifVZ1yD5YubwZ/wQKyEHqUI=")
ki26.loginResult()

ki27 = TOBY.LINE()
ki27.login(token="EnU8PxnHFyrZhXXYkP88.5Gss6Cj7IBEXrUFBawm9oa.VUdSQtCF7gdJy7dKipuhoFlqo28yJtFwDJA1Zhuyh+E=")
ki27.loginResult()

ki28 = TOBY.LINE()
ki28.login(token="EnYRAhLylfdTQuuOHHf3.SO/fObQ10CshHFFY0L3meW.TWi/eQ5UaSo2pX79Tmyms6C4I2tuIF6LrmqLO217s7Y=")
ki28.loginResult()

ki29 = TOBY.LINE()
ki29.login(token="EnRl9lRnJSrizZzVYaL1.F998qotUGTGQIRjcj/3fKq.ygoutzb1c+LtS2AXp/NZ5+c2D2HEI4tr+JJ9F41AfRs=")
ki29.loginResult()

ki30 = TOBY.LINE()
ki30.login(token="EnPJakWiVt7MMdJjofg7.8DHCNR+5ggo//QiQT7pj9W.wIGtq9HZqsWyR/SzuWn3xnzhLuhf40iSRIKjN/KRRxc=")
ki30.loginResult()

ki31 = TOBY.LINE()
ki31.login(token="En9b8bh3juUFV1SHOtqd.rOli1dtiBis50MI658yqRq.O91BvrS4ofxXU5GfhcGFs/eeN7O9HYHiEkC9GoGSi1w=")
ki31.loginResult()

ki32 = TOBY.LINE()
ki32.login(token="En07EbJJbrlxuOlJ6Go0.JAwaMojSWCnrhb405Gw7Sa.d4ed75AGPej2rInsnKSgjE/nwv5S2hJi+Wv0nPMAtGw=")
ki32.loginResult()

ki33 = TOBY.LINE()
ki33.login(token="EndQaONNqiyXgWRk0nO2.kJj6gKL1avGlp7iF9MY8KG.atHwdmHdB079XSdZ9QtVkiek6CGwaBWDmM1Fhwh1PkM=")
ki33.loginResult()

ki34 = TOBY.LINE()
ki34.login(token="EnfFz5cD8tXkYNoGTR84.hz3BUHBhWs9y9M66OUsVXa.8t2rgeHVKXFXWoL7SoHF70Yjbaw5+VdiLPX9CotxA7A=")
ki34.loginResult()

ki35 = TOBY.LINE()
ki35.login(token="EnLmnk74dGVeobCxHjy6.zbzLgObFSJIgQgJQvcBBPG.QOZFU2NUBXZ+iv2Kdq59qddPgl3JvjRCl3IWCo47geg=")
ki35.loginResult()

ki36 = TOBY.LINE()
ki36.login(token="EnxsqCL3DhYeIVaYocL4.4tpKgyQpvX03tq+Nc2O81a.YiP01ZMhSECrB4DEbBEu8Pma3mEMXfpoBq/GBmV5p6A=")
ki36.loginResult()

ki37 = TOBY.LINE()
ki37.login(token="EnxsqCL3DhYeIVaYocL4.4tpKgyQpvX03tq+Nc2O81a.YiP01ZMhSECrB4DEbBEu8Pma3mEMXfpoBq/GBmV5p6A=")
ki37.loginResult()
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""=====[WAHYUDI]=====

[WAHYUDI]
?[My help]
?[Mybot]
?[Me]
?[Kb-Kb18?Contact Bot?]
?[Gift-Gift3]
?[Contact]
?[Mid]
?[All mid]
?[TL:?Text?
?[Mybio:?Text?]
?[MyName:?Text?]
?[Mid:?mid?]
?[Contact ?On/Off?]
?[Auto Join ?On/Off?]
?[Add ?On/Off?]
?[Share ?On/Off?]
?[Jam ?On/Off?]
?[Leave ?On/Off?]
?[Group Cancel:]
?[Jam Say:?Nama?]
?[Update]
?[Groups]
?[Mcheck]
?[Pesan Cek]
?[Blocklist]
?[Creator]
?[Pesan set:?Text?]

[WAHYUDI]

?[Kick:?mid?]
?[Invite:?mid?]
?[Cancel]
?[Ourl]
?[Banlist]
?[Curl]
?[Invite:gcreator]
?[Protect ?On/Off?]
?[Qr ?On/Off?]
?[Cancel ?On/Off?]
?[Invite ?On/Off?]
?[Ginfo]
?[Backup]
?[Sayang]
?[Gn ?Nama Grup?]
?[Album:?ID?]
?[Gurl ?ID?]
?[Nk?nama?]
?[Ban]
?[Unban]
?[Ban:]
?[Unban:]  

=====[WAHYUDI]=====
"""
KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10,ki11,ki12,ki13,ki14,ki15,ki16,ki17,ki18,ki19,ki20,ki21,ki22,ki23,ki24,ki25,ki26,ki27,ki28,ki29,ki30,ki31,ki32,ki33,ki34,ki35,ki36,ki37]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
ki10mid = ki10.getProfile().mid
ki11mid = ki11.getProfile().mid
ki12mid = ki12.getProfile().mid
ki13mid = ki13.getProfile().mid
ki14mid = ki14.getProfile().mid
ki15mid = ki15.getProfile().mid
ki16mid = ki16.getProfile().mid
ki17mid = ki17.getProfile().mid
ki18mid = ki18.getProfile().mid
ki19mid = cl.getProfile().mid
ki20mid = ki.getProfile().mid
ki21mid = ki2.getProfile().mid
ki22mid = ki3.getProfile().mid
ki23mid = ki4.getProfile().mid
ki24mid = ki5.getProfile().mid
ki25mid = ki6.getProfile().mid
ki26mid = ki7.getProfile().mid
ki27mid = ki8.getProfile().mid
ki28mid = ki9.getProfile().mid
ki29mid = ki10.getProfile().mid
ki30mid = ki11.getProfile().mid
ki31mid = ki12.getProfile().mid
ki32mid = ki13.getProfile().mid
ki33mid = ki14.getProfile().mid
ki34mid = ki15.getProfile().mid
ki35mid = ki16.getProfile().mid
ki36mid = ki17.getProfile().mid
ki37mid = ki18.getProfile().mid
Bots=[mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid,ki6mid,ki7mid,ki8mid,ki9mid,ki10mid,ki11mid,ki12mid,ki13mid,ki14mid,ki15mid,ki16mid,ki17mid,ki18mid,ki19mid,ki20mid,ki21mid,ki22mid,ki23mid,ki24mid,ki25mid,ki26mid,ki27mid,ki28mid,ki29mid,ki30mid,ki31mid,ki32mid,ki33mid,ki34mid,ki35mid,ki36mid,ki37mid]
admsa = "u6b34b703cbc5fc83cd1e5b6832a05352"

wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":3},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"??a??? fs? a????g ?? a? a f????d",
    "lang":"JP",
    "comment":"Thanks For Add Me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":True,
    "cancelprotect":True,
    "inviteprotect":True,
    "linkprotect":True,
   }

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","^","???:","???:","???:","???:"]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
	
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u6b34b703cbc5fc83cd1e5b6832a05352":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'my menu':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
            elif 'gn ' in msg.text.lower():
                if msg.toType == 2:
                    aditya = cl.getGroup(msg.to)
                    aditya.name = msg.text.replace("Gn ","")
                    cl.updateGroup(aditya)
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif 'invite ' in msg.text.lower():
                    key = msg.text[-33:]
                    cl.findAndAddContactsByMid(key)
                    cl.inviteIntoGroup(msg.to, [key])
                    contact = cl.getContact(key)
            elif msg.text.lower() == 'mybot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki11mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki12mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki13mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki14mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki15mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki16mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki17mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki18mid}
                cl.sendMessage(msg)
		msg.contentMetadata = {'mid': ki19mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki20mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki21mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki22mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki23mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki24mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki25mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki26mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki27mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki28mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki29mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki30mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki31mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki32mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki33mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki34mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki35mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki36mid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'dit':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'kb':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif msg.text.lower() == 'kb2':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif msg.text.lower() == 'kb3':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif msg.text.lower() == 'kb4':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif msg.text.lower() == 'kb5':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            elif msg.text.lower() == 'kb6':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
            elif msg.text.lower() == 'kb7':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
            elif msg.text.lower() == 'kb8':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
            elif msg.text.lower() == 'kb9':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
            elif msg.text.lower() == 'kb10':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                ki10.sendMessage(msg)
            elif msg.text.lower() == 'kb11':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki11mid}
                ki11.sendMessage(msg)
            elif msg.text.lower() == 'kb12':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki12mid}
                ki12.sendMessage(msg)
            elif msg.text.lower() == 'kb13':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki13mid}
                ki13.sendMessage(msg)
            elif msg.text.lower() == 'kb14':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki14mid}
                ki14.sendMessage(msg)
            elif msg.text.lower() == 'kb15':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki15mid}
                ki15.sendMessage(msg)
            elif msg.text.lower() == 'kb16':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki16mid}
                ki16.sendMessage(msg)
            elif msg.text.lower() == 'kb17':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki17mid}
                ki17.sendMessage(msg)
            elif msg.text.lower() == 'kb18':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki18mid}
		ki18.sendMessage(msg)
	    elif msg.text.lower() == 'kb19':
		msg.contentType = 13
                msg.contentMetadata = {'mid': ki19mid}
                ki19.sendMessage(msg)
	    elif msg.text.lower() == 'kb20':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki20mid}
                ki20.sendMessage(msg)
            elif msg.text.lower() == 'kb21':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki21mid}
                ki21.sendMessage(msg)
            elif msg.text.lower() == 'kb22':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki22mid}
                ki22.sendMessage(msg)
            elif msg.text.lower() == 'kb23':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki23mid}
                ki23.sendMessage(msg)
            elif msg.text.lower() == 'kb24':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki24mid}
                ki24.sendMessage(msg)
            elif msg.text.lower() == 'kb25':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki25mid}
                ki25.sendMessage(msg)
            elif msg.text.lower() == 'kb26':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki26mid}
                ki26.sendMessage(msg)
            elif msg.text.lower() == 'kb27':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki27mid}
                ki27.sendMessage(msg)
            elif msg.text.lower() == 'kb28':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki28mid}
                ki28.sendMessage(msg)
            elif msg.text.lower() == 'kb29':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki29mid}
                ki29.sendMessage(msg)
            elif msg.text.lower() == 'kb30':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki30mid}
                ki30.sendMessage(msg)
            elif msg.text.lower() == 'kb31':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki31mid}
                ki31.sendMessage(msg)
            elif msg.text.lower() == 'kb32':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki32mid}
                ki32.sendMessage(msg)
            elif msg.text.lower() == 'kb33':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki33mid}
                ki33.sendMessage(msg)
            elif msg.text.lower() == 'kb34':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki34mid}
                ki34.sendMessage(msg)
            elif msg.text.lower() == 'kb35':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki35mid}
                ki35.sendMessage(msg)
            elif msg.text.lower() == 'kb36':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki36mid}
                ki36.sendMessage(msg)
            elif msg.text.lower() == 'kb37':
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki37mid}
                ki37.sendMessage(msg)
            elif msg.text.lower() == 'hore':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846756",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'ok':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846755",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'siap bos':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846757",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'thx':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846759",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'lol':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846776",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'tidak':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'no':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "16846777",
                                     "STKPKGID": "8543",
                                     "STKVER": "7" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'suntuk':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875040",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'apa?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == '?':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875046",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == 'pose dulu':
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "14875030",
                                     "STKPKGID": "1380280",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
            elif msg.text.lower() == '250c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1380280'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == '200c':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1319678'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'mukineko':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '1300191'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'chino':
                msg.contentType = 9
                msg.contentMetadata={'PRDTYPE': 'STICKER',
                                    'STKVER': '1',
                                    'MSGTPL': '5',
                                    'STKPKGID': '5033'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tidak ada undangan")
                        else:
                            cl.sendText(msg.to,"Invitan tidak ada")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"Invitan tidak ada")
            elif msg.text.lower() == 'ourl':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text.lower() == 'curl':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than")
            elif msg.text.lower() == 'invite:gcreator':
                if msg.toType == 2:
                       ginfo = cl.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           cl.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           cl.inviteIntoGroup(msg.to,[gcmid])
            elif msg.text.lower() == 'bot:gcreator':
                if msg.toType == 2:
                       ginfo = ki.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           ki.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           ki.inviteIntoGroup(msg.to,[gcmid])
            elif msg.text.lower() == 'ginfo':
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact':
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'mid':
                cl.sendText(msg.to,mid)
            elif msg.text.lower() == 'kb mid':
                ki.sendText(msg.to,kimid)
            elif msg.text.lower() == 'kb2 mid':
                ki2.sendText(msg.to,ki2mid)
            elif msg.text.lower() == 'kb3 mid':
                ki3.sendText(msg.to,ki3mid)
            elif msg.text.lower() == 'kb4 mid':
                ki4.sendText(msg.to,ki4mid)
            elif msg.text.lower() == 'kb5 mid':
                ki5.sendText(msg.to,ki5mid)
            elif "all mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                ki6.sendText(msg.to,ki6mid)
                ki7.sendText(msg.to,ki7mid)
                ki8.sendText(msg.to,ki8mid)
                ki9.sendText(msg.to,ki9mid)
                ki10.sendText(msg.to,ki10mid)
                ki11.sendText(msg.to,ki11mid)
                ki12.sendText(msg.to,ki12mid)
                ki13.sendText(msg.to,ki13mid)
                ki14.sendText(msg.to,ki14mid)
                ki15.sendText(msg.to,ki15mid)
                ki16.sendText(msg.to,ki16mid)
                ki17.sendText(msg.to,ki16mid)
		ki18.sendText(msg.to,ki17mid)
                ki19.sendText(msg.to,ki18mid)
                ki20.sendText(msg.to,ki19mid)
                ki21.sendText(msg.to,ki20mid)
                ki22.sendText(msg.to,ki21mid)
                ki23.sendText(msg.to,ki22mid)
                ki24.sendText(msg.to,ki23mid)
                ki25.sendText(msg.to,ki24mid)
                ki26.sendText(msg.to,ki25mid)
                ki27.sendText(msg.to,ki26mid)
                ki28.sendText(msg.to,ki27mid)
                ki29.sendText(msg.to,ki28mid)
                ki30.sendText(msg.to,ki29mid)
                ki31.sendText(msg.to,ki30mid)
                ki32.sendText(msg.to,ki31mid)
                ki33.sendText(msg.to,ki32mid)
                ki34.sendText(msg.to,ki33mid)
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki11.getProfile()
                    profile.displayName = string
                    ki11.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki12.getProfile()
                    profile.displayName = string
                    ki12.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki13.getProfile()
                    profile.displayName = string
                    ki13.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki14.getProfile()
                    profile.displayName = string
                    ki14.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki15.getProfile()
                    profile.displayName = string
                    ki15.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki16.getProfile()
                    profile.displayName = string
                    ki16.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki17.getProfile()
                    profile.displayName = string
                    ki17.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki18.getProfile()
                    profile.displayName = string
                    ki18.updateProfile(profile)
		if len(string.decode('utf-8')) <= 20:
                    profile = ki19.getProfile()
                    profile.displayName = string
                    ki19.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki20.getProfile()
                    profile.displayName = string
                    ki20.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki21.getProfile()
                    profile.displayName = string
                    ki21.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki22.getProfile()
                    profile.displayName = string
                    ki22.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki23.getProfile()
                    profile.displayName = string
                    ki23.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki24.getProfile()
                    profile.displayName = string
                    ki24.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki25.getProfile()
                    profile.displayName = string
                    ki25.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki26.getProfile()
                    profile.displayName = string
                    ki26.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki27.getProfile()
                    profile.displayName = string
                    ki27.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki28.getProfile()
                    profile.displayName = string
                    ki28.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki29.getProfile()
                    profile.displayName = string
                    ki29.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki30.getProfile()
                    profile.displayName = string
                    ki30.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki31.getProfile()
                    profile.displayName = string
                    ki31.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki32.getProfile()
                    profile.displayName = string
                    ki32.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki33.getProfile()
                    profile.displayName = string
                    ki33.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki34.getProfile()
                    profile.displayName = string
                    ki34.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki35.getProfile()
                    profile.displayName = string
                    ki35.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki36.getProfile()
                    profile.displayName = string
                    ki36.updateProfile(profile)
                    cl.sendText(msg.to,"nama berubah menjadi " + string + "")
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki3.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki4.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki5.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki6.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki7.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki8.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki9.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki10.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki11.getProfile()
                    profile.statusMessage = string
                    ki11.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki12.getProfile()
                    profile.statusMessage = string
                    ki12.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki13.getProfile()
                    profile.statusMessage = string
                    ki13.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki14.getProfile()
                    profile.statusMessage = string
                    ki14.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki15.getProfile()
                    profile.statusMessage = string
                    ki15.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki16.getProfile()
                    profile.statusMessage = string
                    ki16.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki17.getProfile()
                    profile.statusMessage = string
                    ki17.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki18.getProfile()
                    profile.statusMessage = string
                    ki18.updateProfile(profile)
		if len(string.decode('utf-8')) <= 500:
                    profile = ki19.getProfile()
                    profile.statusMessage = string
                    ki19.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki20.getProfile()
                    profile.statusMessage = string
                    ki20.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki21.getProfile()
                    profile.statusMessage = string
                    ki21.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki22.getProfile()
                    profile.statusMessage = string
                    ki22.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki23.getProfile()
                    profile.statusMessage = string
                    ki23.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki24.getProfile()
                    profile.statusMessage = string
                    ki24.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki25.getProfile()
                    profile.statusMessage = string
                    ki25.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki26.getProfile()
                    profile.statusMessage = string
                    ki26.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki27.getProfile()
                    profile.statusMessage = string
                    ki27.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki28.getProfile()
                    profile.statusMessage = string
                    ki28.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki29.getProfile()
                    profile.statusMessage = string
                    ki29.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki30.getProfile()
                    profile.statusMessage = string
                    ki30.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki31.getProfile()
                    profile.statusMessage = string
                    ki31.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki32.getProfile()
                    profile.statusMessage = string
                    ki32.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki33.getProfile()
                    profile.statusMessage = string
                    ki33.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki34.getProfile()
                    profile.statusMessage = string
                    ki34.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki35.getProfile()
                    profile.statusMessage = string
                    ki36.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki37.getProfile()
                    profile.statusMessage = string
                    ki37.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
                if msg.text == "set":
                    sendMessage(msg.to, "I have set a read point ?\n?tes?I will show you who I have read ?")
                    try:
                        del wait['readPoint'][msg.to]
                        del wait['readMember'][msg.to]
                    except:
                        pass
                    wait['readPoint'][msg.to] = msg.id
                    wait['readMember'][msg.to] = ""
                    wait['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait['ROM'][msg.to] = {}
                    print wait
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Names Menjadi : " + string + "")
#---------------------------------------------------------
            elif "1name:" in msg.text:
                string = msg.text.replace("1name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "2name:" in msg.text:
                string = msg.text.replace("2name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "3name:" in msg.text:
                string = msg.text.replace("3name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "4name:" in msg.text:
                string = msg.text.replace("4name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "Mybio:" in msg.text:
                string = msg.text.replace("Mybio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Bio??" + string + "")
#--------------------------------------------------------
            elif "5name:" in msg.text:
                string = msg.text.replace("5name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "6name:" in msg.text:
                string = msg.text.replace("6name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki6.getProfile()
                    profile.displayName = string
                    ki6.updateProfile(profile)
                    ki6.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "7name:" in msg.text:
                string = msg.text.replace("7name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki7.getProfile()
                    profile.displayName = string
                    ki7.updateProfile(profile)
                    ki7.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "8name:" in msg.text:
                string = msg.text.replace("8name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki8.getProfile()
                    profile.displayName = string
                    ki8.updateProfile(profile)
                    ki8.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "9name:" in msg.text:
                string = msg.text.replace("9name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki9.getProfile()
                    profile.displayName = string
                    ki9.updateProfile(profile)
                    ki9.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "10name:" in msg.text:
                string = msg.text.replace("10name:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki10.getProfile()
                    profile.displayName = string
                    ki10.updateProfile(profile)
                    ki10.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "11names:" in msg.text:
                string = msg.text.replace("11names:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki11.getProfile()
                    profile.displayName = string
                    ki11.updateProfile(profile)
                    ki11.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "12names:" in msg.text:
                string = msg.text.replace("12names:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki12.getProfile()
                    profile.displayName = string
                    ki12.updateProfile(profile)
                    ki12.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "13names:" in msg.text:
                string = msg.text.replace("13names:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki13.getProfile()
                    profile.displayName = string
                    ki13.updateProfile(profile)
                    ki13.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "14names:" in msg.text:
                string = msg.text.replace("14names:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki14.getProfile()
                    profile.displayName = string
                    ki14.updateProfile(profile)
                    ki14.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "15names:" in msg.text:
                string = msg.text.replace("15names:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki15.getProfile()
                    profile.displayName = string
                    ki15.updateProfile(profile)
                    ki15.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "16names:" in msg.text:
                string = msg.text.replace("16names:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki16.getProfile()
                    profile.displayName = string
                    ki16.updateProfile(profile)
                    ki16.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "17names:" in msg.text:
                string = msg.text.replace("17names:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki17.getProfile()
                    profile.displayName = string
                    ki17.updateProfile(profile)
                    ki17.sendText(msg.to,"Update Names Menjadi :" + string + "")
            elif "18names:" in msg.text:
                string = msg.text.replace("18names:","")
                if len(string.decode('utf-8')) <= 30:
                    profile = ki18.getProfile()
                    profile.displayName = string
                    ki18.updateProfile(profile)
                    ki18.sendText(msg.to,"Update Names Menjadi :" + string + "")
#--------------------------------------------------------
            elif "Cstatus:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                else:
                    cl.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus1:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                else:
                    ki.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus2:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
                else:
                    ki2.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus3:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki3.updateProfile(profile)
                else:
                    ki3.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus4:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    ki4.updateProfile(profile)
                else:
                    ki4.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus5:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki5.updateProfile(profile)
                else:
                    ki5.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus6:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    ki6.updateProfile(profile)
                else:
                    ki6.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus7:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki7.updateProfile(profile)
                else:
                    ki7.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus8:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki8.updateProfile(profile)
                else:
                    ki8.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus9:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki9.updateProfile(profile)
                else:
                    ki9.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus10:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki10.updateProfile(profile)
                else:
                    ki10.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus11:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki11.updateProfile(profile)
                else:
                    ki11.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus12:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki12.updateProfile(profile)
                else:
                    ki12.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus13:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki13.updateProfile(profile)
                else:
                    ki13.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus14:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki14.updateProfile(profile)
                else:
                    ki14.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus15:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki15.updateProfile(profile)
                else:
                    ki15.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus16:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki16.updateProfile(profile)
                else:
                    ki16.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus17:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki17.updateProfile(profile)
                else:
                    ki17.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Cstatus18:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki18.updateProfile(profile)
                else:
                    ki18.sendText(msg.to,"Done")
#---------------------------------------------------------
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to on")
                    else:
                        cl.sendText(msg.to,"contact already on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to on")
                    else:
                        cl.sendText(msg.to,"contact already on")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to off")
                    else:
                        cl.sendText(msg.to,"contact already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"contact set to off")
                    else:
                        cl.sendText(msg.to,"contact already off")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to on")
                    else:
                        cl.sendText(msg.to,"Protection already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to on")
                    else:
                        cl.sendText(msg.to,"Protection already on")
            elif msg.text.lower() == 'qr on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to on")
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to on")
                    else:
                        cl.sendText(msg.to,"Protection Qr already on")
            elif msg.text.lower() == 'invit on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to on")
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to on")
                    else:
                        cl.sendText(msg.to,"Protection Invite already on")
            elif msg.text.lower() == 'cancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        cl.sendText(msg.to,"Cancel Protection already on")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to on")
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to on")
                    else:
                        cl.sendText(msg.to,"Autojoin already on")
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to off")
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Autojoin set to off")
                    else:
                        cl.sendText(msg.to,"Autojoin already off")
            elif msg.text.lower() == 'protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to off")
                    else:
                        cl.sendText(msg.to,"Protection already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection set to off")
                    else:
                        cl.sendText(msg.to,"Protection already off")
            elif msg.text.lower() == 'qr off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Qr set to off")
                    else:
                        cl.sendText(msg.to,"Protection Qr already off")
            elif msg.text.lower() == 'invit off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Protection Invite already off")
            elif msg.text.lower() == 'cancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        cl.sendText(msg.to,"Cancel Protection Invite already off")
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Nilai tidak benar")
                    else:
                        cl.sendText(msg.to,"Weird value??")
            elif msg.text.lower() == 'leave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'leave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        cl.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == 'share on':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to on")
                    else:
                        cl.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to on")
                    else:
                        cl.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'share off':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to off")
                    else:
                        cl.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share set to off")
                    else:
                        cl.sendText(msg.to,"Share already off")
            elif msg.text.lower() == 'menu':
                md = ""
                if wait["contact"] == True: md+="?????? Contact:on ??????\n"
                else: md+="?????? Contact:off??????\n"
                if wait["autoJoin"] == True: md+="?????? Auto Join:on ??????\n"
                else: md +="?????? Auto Join:off??????\n"
                if wait["autoCancel"]["on"] == True:md+="?????? Auto cancel:" + str(wait["autoCancel"]["members"]) + "??????\n"
                else: md+= "?????? Group cancel:off ??????\n"
                if wait["leaveRoom"] == True: md+="?????? Auto leave:on ??????\n"
                else: md+="?????? Auto leave:off ??????\n"
                if wait["timeline"] == True: md+="?????? Share:on ??????\n"
                else:md+="?????? Share:off ??????\n"
                if wait["autoAdd"] == True: md+="?????? Auto add:on ??????\n"
                else:md+="?????? Auto add:off ??????\n"
                if wait["protect"] == True: md+="?????? Protect:on ??????\n"
                else:md+="?????? Protect:off ??????\n"
                if wait["linkprotect"] == True: md+="??????Link Protect:on ??????\n"
                else:md+="??????Link Protect:off ??????\n"
                if wait["inviteprotect"] == True: md+="??????Invitation Protect:on ??????\n"
                else:md+="??????Invitation Protect:off ??????\n"
                if wait["cancelprotect"] == True: md+="??????Cancel Protect:on ??????\n"
                else:md+="??????Cancel Protect:off ??????\n"
                cl.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                cl.sendText(msg.to,"????down??????down??????down??????down??????down??????down??????down??")
                cl.sendMessage(msg)
                cl.sendText(msg.to,"????up??????up??????up??????up??????up??????up??????up??")
            elif "Album:" in msg.text:
                gid = msg.text.replace("Album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text.lower() == 'kicker':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki6mid}
                ki6.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki7mid}
                ki7.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki8mid}
                ki8.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki9mid}
                ki9.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki10mid}
                ki10.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki11mid}
                ki11.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki12mid}
                ki12.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki13mid}
                ki13.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki14mid}
                ki14.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki15mid}
                ki15.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki16mid}
                ki16.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki17mid}
                ki17.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki18mid}
                ki18.sendMessage(msg)
		msg.contentType = 13
                msg.contentMetadata = {'mid': ki19mid}
                ki19.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki20mid}
                ki20.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki21mid}
                ki21.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki22mid}
                ki22.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki23mid}
                ki23.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki24mid}
                ki24.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki25mid}
                ki25.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki26mid}
                ki26.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki27mid}
                ki27.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki28mid}
                ki28.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki29mid}
                ki29.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki30mid}
                ki30.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki31mid}
                ki31.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki32mid}
                ki32.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki33mid}
                ki33.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki34mid}
                ki34.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki35mid}
                ki35.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki36mid}
                ki36.sendMessage(msg)
            elif msg.text.lower() == 'out':
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                gid = ki6.getGroupIdsJoined()
                gid = ki7.getGroupIdsJoined()
                gid = ki8.getGroupIdsJoined()
                gid = ki9.getGroupIdsJoined()
                gid = ki10.getGroupIdsJoined()
                gid = ki11.getGroupIdsJoined()
                gid = ki13.getGroupIdsJoined()
                gid = ki14.getGroupIdsJoined()
                gid = ki15.getGroupIdsJoined()
                gid = ki16.getGroupIdsJoined()
                gid = ki17.getGroupIdsJoined()
                gid = ki18.getGroupIdsJoined()
		gid = ki19.getGroupIdsJoined()
                gid = ki20.getGroupIdsJoined()
                gid = ki21.getGroupIdsJoined()
                gid = ki22.getGroupIdsJoined()
                gid = ki23.getGroupIdsJoined()
                gid = ki24.getGroupIdsJoined()
                gid = ki25.getGroupIdsJoined()
                gid = ki26.getGroupIdsJoined()
                gid = ki27.getGroupIdsJoined()
                gid = ki28.getGroupIdsJoined()
                gid = ki29.getGroupIdsJoined()
                gid = ki30.getGroupIdsJoined()
                gid = ki31.getGroupIdsJoined()
                gid = ki32.getGroupIdsJoined()
                gid = ki33.getGroupIdsJoined()
                gid = ki32.getGroupIdsJoined()
                gid = ki33.getGroupIdsJoined()
                gid = ki34.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)
                    ki4.leaveGroup(i)
                    ki5.leaveGroup(i)
                    ki6.leaveGroup(i)
                    ki7.leaveGroup(i)
                    ki8.leaveGroup(i)
                    ki9.leaveGroup(i)
                    ki10.leaveGroup(i)
                    ki11.leaveGroup(i)
                    ki13.leaveGroup(i)
                    ki14.leaveGroup(i)
                    ki15.leaveGroup(i)
                    ki16.leaveGroup(i)
                    ki17.leaveGroup(i)
                    ki18.leaveGroup(i)
		    ki19.leaveGroup(i)
                    ki20.leaveGroup(i)
                    ki21.leaveGroup(i)
                    ki22.leaveGroup(i)
                    ki23.leaveGroup(i)
                    ki24.leaveGroup(i)
                    ki25.leaveGroup(i)
                    ki26.leaveGroup(i)
                    ki27.leaveGroup(i)
                    ki28.leaveGroup(i)
                    ki29.leaveGroup(i)
                    ki30.leaveGroup(i)
                    ki31.leaveGroup(i)
                    ki32.leaveGroup(i)
                    ki33.leaveGroup(i)
                    ki34.leaveGroup(i)
                    ki35.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Wahyudi Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif msg.text.lower() == 'gcancel':
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
            elif "Hapus:" in msg.text:
                gid = msg.text.replace("Hapus:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album")
            elif msg.text.lower() == 'add on':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to on")
                    else:
                        cl.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'add off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add set to off")
                    else:
                        cl.sendText(msg.to,"Auto add already off")
            elif "Pesan set:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                cl.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah??\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di")
                    else:
                        cl.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"オンにしました")
                    else:
                        cl.sendText(msg.to,"要了开")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text.lower() == 'url':
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text.lower() == 'url1':
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        ki.updateGroup(g)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        ki.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif 'gurl ' in msg.text.lower():
                if msg.toType == 2:
                    gid = msg.text.replace("Gurl ","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist􀜁􀅔")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist􀜁􀅔")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklist􀜁??")
                else:
                    cl.sendText(msg.to,"The following is a blacklist􀜁")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Jam already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Jam already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Jam")

            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki37.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.01)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki37.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki37.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#-----------------------------------------------------------

            elif ("Bunuh " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif ("Telan " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki.kickoutFromGroup(msg.to,[target])
                       except:
                           ki.sendText(msg.to,"Error")

            elif ("Telan2 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif ("Telan3 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki3.kickoutFromGroup(msg.to,[target])
                       except:
                           ki3.sendText(msg.to,"Error")
            elif ("Telan4 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki4.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")
            elif ("Telan5 " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki5.kickoutFromGroup(msg.to,[target])
                       except:
                           ki5.sendText(msg.to,"Error")
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Beb " in msg.text:
                if msg.toType == 2:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Beb","")
                        gs = cl.getGroup(msg.to)
                        cl.sendText(msg.to,"Group cleansing begin")
                        ki.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9,ki10]
                                    kicker=random.choice(klist)
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group Bersihkan")
            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    gs = ki7.getGroup(msg.to)
                    gs = ki8.getGroup(msg.to)
                    gs = ki9.getGroup(msg.to)
                    gs = ki10.getGroup(msg.to)
                    gs = ki11.getGroup(msg.to)
                    gs = ki12.getGroup(msg.to)
                    gs = ki13.getGroup(msg.to)
                    gs = ki14.getGroup(msg.to)
                    gs = ki15.getGroup(msg.to)
                    gs = ki16.getGroup(msg.to)
                    gs = ki17.getGroup(msg.to)
                    gs = ki18.getGroup(msg.to)
		    gs = ki19.getGroup(msg.to)
                    gs = ki20.getGroup(msg.to)
                    gs = ki21.getGroup(msg.to)
                    gs = ki22.getGroup(msg.to)
                    gs = ki23.getGroup(msg.to)
                    gs = ki24.getGroup(msg.to)
                    gs = ki25.getGroup(msg.to)
                    gs = ki26.getGroup(msg.to)
                    gs = ki27.getGroup(msg.to)
                    gs = ki28.getGroup(msg.to)
                    gs = ki29.getGroup(msg.to)
                    gs = ki30.getGroup(msg.to)
                    gs = ki31.getGroup(msg.to)
                    gs = ki32.getGroup(msg.to)
                    gs = ki33.getGroup(msg.to)
                    gs = ki34.getGroup(msg.to)
                    gs = ki35.getGroup(msg.to)
                    gs = ki36.getGroup(msg.to)
                    ki.sendText(msg.to,"Just some casual cleansing")
                    kk.sendText(msg.to,"Group cleansed.")
                    kc.sendText(msg.to,"GoodBye All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        kk.sendText(msg.to,"Not found.")
                        kc.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Group cleanse")
                                kk.sendText(msg.to,"Group cleanse")
                                kc.sendText(msg.to,"Group cleanse")
#-----------------------------------------------------------

#-----------------------------------------------------------
	    elif "Ban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                cl.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                cl.sendText(msg.to,"Error")
	    elif ("Test" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                	   msg.contentType = 9
                           msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                           msg.text = None
                           cl.sendMessage(msg)
                           cl.sendMessage(msg,target)
                       except:
			   cl.sendText(msg.to,"Gift send to member")
	    elif "Unban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                cl.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                cl.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    cl.sendText(msg.to,_name + " Not In Blacklist")
#-----------------------------------------------------------
#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
            elif cms(msg.text,["matikan"]):
                    cl.sendText(msg.to,"Reboot")
                    exit(1)
#-----------------------------------------------------------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------

#-----------------------------------------------------------
            elif msg.text.lower() == 'respon':
                profile = ki.getProfile()
                text = profile.displayName + ""
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + ""
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + ""
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + ""
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + ""
                ki5.sendText(msg.to, text)
                profile = ki6.getProfile()
                text = profile.displayName + ""
                ki6.sendText(msg.to, text)
                profile = ki7.getProfile()
                text = profile.displayName + ""
                ki7.sendText(msg.to, text)
                profile = ki8.getProfile()
                text = profile.displayName + ""
                ki8.sendText(msg.to, text)
                profile = ki9.getProfile()
                text = profile.displayName + ""
                ki9.sendText(msg.to, text)
                profile = ki10.getProfile()
                text = profile.displayName + ""
                ki10.sendText(msg.to, text)
                profile = ki11.getProfile()
                text = profile.displayName + ""
                ki11.sendText(msg.to, text)
                profile = ki12.getProfile()
                text = profile.displayName + ""
                ki12.sendText(msg.to, text)
                profile = ki13.getProfile()
                text = profile.displayName + ""
                ki13.sendText(msg.to, text)
                profile = ki14.getProfile()
                text = profile.displayName + ""
                ki14.sendText(msg.to, text)
                profile = ki15.getProfile()
                text = profile.displayName + ""
                ki15.sendText(msg.to, text)
                profile = ki16.getProfile()
                text = profile.displayName + ""
                ki16.sendText(msg.to, text)
                profile = ki17.getProfile()
                text = profile.displayName + ""
                ki17.sendText(msg.to, text)
                profile = ki18.getProfile()
                text = profile.displayName + ""
                ki18.sendText(msg.to, text)
		profile = ki19.getProfile()
                text = profile.displayName + ""
                ki19.sendText(msg.to, text)
                profile = ki20.getProfile()
                text = profile.displayName + ""
                ki20.sendText(msg.to, text)
                profile = ki21.getProfile()
                text = profile.displayName + ""
                ki21.sendText(msg.to, text)
                profile = ki22.getProfile()
                text = profile.displayName + ""
                ki22.sendText(msg.to, text)
                profile = ki23.getProfile()
                text = profile.displayName + ""
                ki23.sendText(msg.to, text)
                profile = ki24.getProfile()
                text = profile.displayName + ""
                ki24.sendText(msg.to, text)
                profile = ki25.getProfile()
                text = profile.displayName + ""
                ki25.sendText(msg.to, text)
                profile = ki26.getProfile()
                text = profile.displayName + ""
                ki26.sendText(msg.to, text)
                profile = ki27.getProfile()
                text = profile.displayName + ""
                ki27.sendText(msg.to, text)
                profile = ki28.getProfile()
                text = profile.displayName + ""
                ki28.sendText(msg.to, text)
                profile = ki29.getProfile()
                text = profile.displayName + ""
                ki29.sendText(msg.to, text)
                profile = ki30.getProfile()
                text = profile.displayName + ""
                ki30.sendText(msg.to, text)
                profile = ki31.getProfile()
                text = profile.displayName + ""
                ki31.sendText(msg.to, text)
                profile = ki32.getProfile()
                text = profile.displayName + ""
                ki32.sendText(msg.to, text)
                profile = ki33.getProfile()
                text = profile.displayName + ""
                ki34.sendText(msg.to, text)
                profile = ki35.getProfile()
                text = profile.displayName + ""
                ki35.sendText(msg.to, text)
                profile = ki36.getProfile()
                text = profile.displayName + ""
                ki36.sendText(msg.to, text)
                profile = ki37.getProfile()
                text = profile.displayName + ""
                ki37.sendText(msg.to, text)

#-----------------------------------------------------------speed
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"?????? Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"?????? following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += ">" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["say","Tagall"]:
            	 if msg.toType == 2:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += ">" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "Daftar Hitam")
            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled")
            elif "Spam album:" in msg.text:
                try:
                    albumtags = msg.text.replace("Spam album:","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,"We created an album" + name)
                except:
                    cl.sendText(msg.to,"Error")

#-----------------------------------------------

#-----------------------------------------------
            elif msg.text.lower() == '123':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki17.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
			ki19.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki20.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki21.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki22.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki23.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki24.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki25.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki26.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki27.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki28.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki29.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki30.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki31.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki32.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki33.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki34.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki35.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki36.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
                       
#-----------------------------------------------
            elif msg.text.lower() == 'backup':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text.lower() == '1':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Bot1 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Bot2 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Bot3 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#-----------------------------------------------
            elif "Bot4 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "Bot5 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#-----------------------------------------------
            elif "Bot6 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki6.updateGroup(G)
#-----------------------------------------------
            elif "Bot7 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki7.updateGroup(G)
#-----------------------------------------------
            elif "Bot8 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki8.updateGroup(G)
#-----------------------------------------------
            elif "Bot9 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki9.updateGroup(G)
#-----------------------------------------------
            elif "Bot10 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki10.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki10.updateGroup(G)
#-----------------------------------------------
            elif "Bot11 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki11.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki11.updateGroup(G)
#-----------------------------------------------
            elif "Bot12 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki12.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki12.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki12.updateGroup(G)
#-----------------------------------------------
            elif "Bot13 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki13.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki13.updateGroup(G)
#-----------------------------------------------
            elif "Bot14 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki14.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki14.updateGroup(G)
#-----------------------------------------------
            elif "Bot15 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki15.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki15.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki15.updateGroup(G)
#-----------------------------------------------
            elif "Bot16 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki16.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki16.updateGroup(G)
            elif "Bot17 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki16.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki17.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki17.updateGroup(G)
            elif "Bot18 in" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki18.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki18.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki18.updateGroup(G)
#-----------------------------------------------
            elif msg.text.lower() == 'moleh':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"??????Bye Bye "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to)
                        ki5.leaveGroup(msg.to)
                        ki6.leaveGroup(msg.to)
                        ki7.leaveGroup(msg.to)
                        ki8.leaveGroup(msg.to)
                        ki9.leaveGroup(msg.to)
                        ki10.leaveGroup(msg.to)
                        ki11.leaveGroup(msg.to)
                        ki12.leaveGroup(msg.to)
                        ki13.leaveGroup(msg.to)
                        ki14.leaveGroup(msg.to)
                        ki15.leaveGroup(msg.to)
                        ki16.leaveGroup(msg.to)
                        ki17.leaveGroup(msg.to)
                        ki18.leaveGroup(msg.to)
			ki19.leaveGroup(msg.to)
                        ki20.leaveGroup(msg.to)
                        ki21.leaveGroup(msg.to)
                        ki22.leaveGroup(msg.to)
                        ki23.leaveGroup(msg.to)
                        ki24.leaveGroup(msg.to)
                        ki25.leaveGroup(msg.to)
                        ki26.leaveGroup(msg.to)
                        ki27.leaveGroup(msg.to)
                        ki28.leaveGroup(msg.to)
                        ki29.leaveGroup(msg.to)
                        ki30.leaveGroup(msg.to)
                        ki31.leaveGroup(msg.to)
                        ki32.leaveGroup(msg.to)
                        ki33.leaveGroup(msg.to)
                        ki34.leaveGroup(msg.to)
                        ki35.leaveGroup(msg.to)
                        ki36.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot1 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot2 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot3 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot4 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot5 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot6 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki6.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot7 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki7.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot8 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki8.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot9 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki9.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot10 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki10.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot11 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki11.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot12 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki12.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot13 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki13.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot14 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki14.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot15 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki15.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot16 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki16.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Kb17 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki17.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot18 bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki18.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Bot Key" in msg.text:
                ki.sendText(msg.to,"""      ???????????? WAHYUDI BOT CRIME [=] ????????????  \n\n ?????? key Only Kicker ?????? \n\n??????[Kb1 in]\n??????[1name:]\n??????[B Cancel]\n??????[kick @]\n??????[Ban @]\n??????[kill]\n??????[BotChat]\n??????[Respons]\n??????[Kb1 Gift]\n??????[Kb1 bye]\n\n   
""")
#-----------------------------------------------
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Hi " in msg.text:
				bctxt = msg.text.replace("Hi ","")
				ki19.sendText(msg.to,(bctxt))
            elif "Say " in msg.text:
				bctxt = msg.text.replace("Bot Say ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				ki3.sendText(msg.to,(bctxt))
				ki4.sendText(msg.to,(bctxt))
				ki5.sendText(msg.to,(bctxt))
				ki6.sendText(msg.to,(bctxt))
				ki7.sendText(msg.to,(bctxt))
				ki8.sendText(msg.to,(bctxt))
				ki9.sendText(msg.to,(bctxt))
				ki10.sendText(msg.to,(bctxt))
				ki11.sendText(msg.to,(bctxt))
				ki12.sendText(msg.to,(bctxt))
				ki13.sendText(msg.to,(bctxt))
				ki14.sendText(msg.to,(bctxt))
				ki15.sendText(msg.to,(bctxt))
				ki16.sendText(msg.to,(bctxt))
				ki17.sendText(msg.to,(bctxt))
				ki18.sendText(msg.to,(bctxt))
				ki19.sendText(msg.to,(bctxt))
				ki20.sendText(msg.to,(bctxt))
				ki21.sendText(msg.to,(bctxt))
				ki22.sendText(msg.to,(bctxt))
				ki23.sendText(msg.to,(bctxt))
				ki24.sendText(msg.to,(bctxt))
				ki25.sendText(msg.to,(bctxt))
				ki26.sendText(msg.to,(bctxt))
				ki27.sendText(msg.to,(bctxt))
				ki28.sendText(msg.to,(bctxt))
				ki29.sendText(msg.to,(bctxt))
				ki30.sendText(msg.to,(bctxt))
				ki31.sendText(msg.to,(bctxt))
				ki32.sendText(msg.to,(bctxt))
				ki33.sendText(msg.to,(bctxt))
				ki34.sendText(msg.to,(bctxt))
            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Ping ??????")
                ki2.sendText(msg.to,"Ping ??????")
                ki3.sendText(msg.to,"Ping ??????")
                ki4.sendText(msg.to,"Ping ??????")
                ki5.sendText(msg.to,"Ping ??????")
                ki6.sendText(msg.to,"Ping ??????")
                ki7.sendText(msg.to,"Ping ??????")
                ki8.sendText(msg.to,"Ping ??????")
                ki9.sendText(msg.to,"Ping ??????")
                ki10.sendText(msg.to,"Ping ??????")
                ki11.sendText(msg.to,"Ping ??????")
                ki12.sendText(msg.to,"Ping ??????")
                ki13.sendText(msg.to,"Ping ??????")
                ki14.sendText(msg.to,"Ping ??????")
                ki15.sendText(msg.to,"Ping ??????")
                ki16.sendText(msg.to,"Ping ??????")
                ki17.sendText(msg.to,"Ping ??????")
                ki18.sendText(msg.to,"Ping ??????")
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki3mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki7.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)
                    else:
                        G = ki7.getGroup(op.param1)

                        
                        ki7.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki7.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki7.updateGroup(G)

                elif op.param3 in ki9mid:
                    if op.param2 in ki8mid:
                        G = ki8.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)
                    else:
                        G = ki8.getGroup(op.param1)

                        
                        ki8.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki8.updateGroup(G)
                        Ticket = ki8.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki8.updateGroup(G)

                elif op.param3 in ki10mid:
                    if op.param2 in ki9mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)

                elif op.param3 in ki11mid:
                    if op.param2 in ki10mid:
                        G = ki10.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)
                    else:
                        G = ki10.getGroup(op.param1)

                        
                        ki10.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki10.updateGroup(G)
                        Ticket = ki10.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki10.updateGroup(G)

                elif op.param3 in ki12mid:
                    if op.param2 in ki11mid:
                        G = ki11.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)
                    else:
                        G = ki11.getGroup(op.param1)

                        
                        ki11.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki11.updateGroup(G)
                        Ticket = ki11.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki11.updateGroup(G)

                elif op.param3 in ki13mid:
                    if op.param2 in ki12mid:
                        G = ki12.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki12.updateGroup(G)
                    else:
                        G = ki12.getGroup(op.param1)

                        
                        ki12.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki12.updateGroup(G)
                        Ticket = ki12.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki12.updateGroup(G)

                elif op.param3 in ki14mid:
                    if op.param2 in ki13mid:
                        G = ki13.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)
                    else:
                        G = ki13.getGroup(op.param1)

                        
                        ki13.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki13.updateGroup(G)
                        Ticket = ki13.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki13.updateGroup(G)

                elif op.param3 in ki15mid:
                    if op.param2 in ki14mid:
                        G = ki14.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)
                    else:
                        G = ki14.getGroup(op.param1)

                        
                        ki14.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki14.updateGroup(G)
                        Ticket = ki14.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki14.updateGroup(G)

                elif op.param3 in ki16mid:
                    if op.param2 in ki15mid:
                        G = ki15.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki15.updateGroup(G)
                        Ticket = ki15.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki15.updateGroup(G)
                    else:
                        G = ki15.getGroup(op.param1)

                        
                        ki15.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki15.updateGroup(G)
                        Ticket = ki15.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki15.updateGroup(G)

		elif op.param3 in ki17mid:
                    if op.param2 in ki16mid:
                        G = ki16.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki16.updateGroup(G)
                        Ticket = ki16.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki16.updateGroup(G)
                    else:
                        G = ki16.getGroup(op.param1)

                        ki16.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki16.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki16.updateGroup(G)


                elif op.param3 in ki18mid:
                    if op.param2 in ki17mid:
                        G = ki17.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki17.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki17.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki17.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki17.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki17.updateGroup(G)
                        
                elif op.param3 in ki19mid:
                    if op.param2 in ki18mid:
                        G = ki18.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki18.updateGroup(G)
                        Ticket = ki18.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki18.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki18.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki18.updateGroup(G)
                        Ticket = ki18.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki18.updateGroup(G)
                        
                elif op.param3 in ki20mid:
                    if op.param2 in ki19mid:
                        G = ki19.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki19.updateGroup(G)
                        Ticket = ki19.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki19.getGroup(op.param1)

                        
                        ki19.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki19.updateGroup(G)
                        Ticket = ki19.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki19.updateGroup(G)

                elif op.param3 in ki21mid:
                    if op.param2 in ki20mid:
                        G = ki20.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki20.updateGroup(G)
                        Ticket = ki20.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki20.updateGroup(G)
                    else:
                        G = ki20.getGroup(op.param1)

                        
                        ki20.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki20.updateGroup(G)
                        Ticket = ki20.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki20.updateGroup(G)

                elif op.param3 in ki22mid:
                    if op.param2 in ki21mid:
                        G = ki21.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki21.updateGroup(G)
                        Ticket = ki21.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki21.updateGroup(G)
                    else:
                        G = ki21.getGroup(op.param1)

                        
                        ki21.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki21.updateGroup(G)
                        Ticket = ki21.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki21.updateGroup(G)

                elif op.param3 in ki23mid:
                    if op.param2 in ki22mid:
                        G = ki22.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki22.updateGroup(G)
                        Ticket = ki22.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki22.updateGroup(G)
                    else:
                        G = ki22.getGroup(op.param1)

                        
                        ki22.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki22.updateGroup(G)
                        Ticket = ki22.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)

                elif op.param3 in ki24mid:
                    if op.param2 in ki23mid:
                        G = ki23.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki23.updateGroup(G)
                        Ticket = ki23.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki23.updateGroup(G)
                    else:
                        G = ki23.getGroup(op.param1)

                        
                        ki23.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki23.updateGroup(G)
                        Ticket = ki23.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki23.updateGroup(G)

                elif op.param3 in ki25mid:
                    if op.param2 in ki24mid:
                        G = ki24.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki24.updateGroup(G)
                        Ticket = ki24.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki24.updateGroup(G)
                    else:
                        G = ki24.getGroup(op.param1)

                        
                        ki24.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki24.updateGroup(G)
                        Ticket = ki24.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki24.updateGroup(G)

                elif op.param3 in ki26mid:
                    if op.param2 in ki25mid:
                        G = ki25.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki25.updateGroup(G)
                        Ticket = ki25.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki25.updateGroup(G)
                    else:
                        G = ki25.getGroup(op.param1)

                        
                        ki25.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki25.updateGroup(G)
                        Ticket = ki25.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki25.updateGroup(G)

                elif op.param3 in ki27mid:
                    if op.param2 in ki26mid:
                        G = ki26.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki26.updateGroup(G)
                        Ticket = ki26.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki26.updateGroup(G)
                    else:
                        G = ki26.getGroup(op.param1)

                        
                        ki26.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki26.updateGroup(G)
                        Ticket = ki26.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki26.updateGroup(G)

                elif op.param3 in ki28mid:
                    if op.param2 in ki27mid:
                        G = ki27.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki27.updateGroup(G)
                        Ticket = ki27.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki27.updateGroup(G)
                    else:
                        G = ki27.getGroup(op.param1)

                        
                        ki27.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki27.updateGroup(G)
                        Ticket = ki27.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki27.updateGroup(G)

                elif op.param3 in ki29mid:
                    if op.param2 in ki28mid:
                        G = ki28.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki28.updateGroup(G)
                        Ticket = ki28.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki28.updateGroup(G)
                    else:
                        G = ki28.getGroup(op.param1)

                        
                        ki28.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki28.updateGroup(G)
                        Ticket = ki28.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki28.updateGroup(G)

                elif op.param3 in ki30mid:
                    if op.param2 in ki29mid:
                        G = ki29.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki29.updateGroup(G)
                        Ticket = ki29.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki29.updateGroup(G)
                    else:
                        G = ki29.getGroup(op.param1)

                        
                        ki29.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki29.updateGroup(G)
                        Ticket = ki29.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki29.updateGroup(G)

                elif op.param3 in ki31mid:
                    if op.param2 in ki30mid:
                        G = ki30.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki30.updateGroup(G)
                        Ticket = ki30.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki30.updateGroup(G)
                    else:
                        G = ki30.getGroup(op.param1)

                        
                        ki30.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki30.updateGroup(G)
                        Ticket = ki30.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki30.updateGroup(G)

                elif op.param3 in ki32mid:
                    if op.param2 in ki31mid:
                        G = ki31.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki31.updateGroup(G)
                        Ticket = ki31.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki31.updateGroup(G)
                    else:
                        G = ki31.getGroup(op.param1)

                        
                        ki31.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki31.updateGroup(G)
                        Ticket = ki31.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki11.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki12.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki13.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki14.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki15.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki16.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki17.acceptGroupInvitationByTicket(op.param1,Ticket)
			ki18.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki19.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki20.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki21.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki22.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki23.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki24.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki25.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki26.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki27.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki28.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki29.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki30.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki31.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki32.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki33.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki34.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki35.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki31.updateGroup(G)
            except:
                pass
	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			random.choice(KAC).updateGroup(G)
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            if op.param2 not in Bots:
       	        if op.param2 in Bots:
       	           pass
                elif wait["cancelprotect"] == True:
                   cl.cancelGroupInvitation(op.param1,[contact.mid for contact in cl.getGroup(op.param1).invitee])
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"?%H:%M?")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
