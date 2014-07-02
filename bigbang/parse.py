from pprint import pprint as pp
import email
import re
import dateutil.parser as dparse


re_cache = {
  'top_exp'     : re.compile("From .*\d\d\d\d\n"),
  'msg_id'      : re.compile("<\S*@\S*>"),
  'msg_from'    : re.compile("\(([^()]+)\)")
}

def open_mail_archive(filename):
    with open(filename, 'r') as f:
        mails = re_cache['top_exp'].split(f.read())
        return [email.message_from_string(m) for m in mails if m is not '']

def split_references(refs):
    return re_cache['msg_id'].findall(refs)

def get_refs(refs):
    return re_cache['msg_id'].findall(refs)

def clean_mid(mid):
    return get_refs(mid)[0]

def clean_from(m_from):
    return re_cache['msg_from'].findall(m_from)[0]
