#!/home/stormy/opt/anaconda3/bin/python

import json
import argparse

parser = argparse.ArgumentParser(description='tiddlers.json.')
parser.add_argument('tdljs', metavar='tiddlers.json', type=str, nargs='+',
                    help='tiddlers.json export from the site')

args = parser.parse_args()

with open(args.tdljs[0]) as jsf:
    jsstr = jsf.read()

js = json.loads(jsstr)
for tdl in js:
    tgs = []
    txt = ""
    if 'tags' in tdl.keys():
        tgs = tdl.pop('tags').split(' ')
        tgs = "".join(["    -" + tg + "\n" for tg in tgs])
    if 'text' in tdl.keys():
        txt = tdl.pop('text')
    yml = [tk + ": " + tdl.get(tk) + "\n" for tk in tdl.keys()]
    yml = "---\n" + "".join(yml)
    if len(tgs):
        yml += "tags:\n" + tgs
    yml += "---"

    with open("md/" + tdl['title'] + ".md", 'w') as f:
        f.write(yml + "\n" + txt)
