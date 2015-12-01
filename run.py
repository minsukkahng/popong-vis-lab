# -*- coding: utf-8 -*-

from collections import defaultdict
import json

from flask import Flask
from flask import render_template


app = Flask(__name__)

options = ["yea", "nay", "forfeit"]
partycolors = {
    u"\uc0c8\ub204\ub9ac\ub2f9": "#d00",
    u"\uc0c8\uc815\uce58\ubbfc\uc8fc\uc5f0\ud569": "#07d",
    u"\ud1b5\ud569\uc9c4\ubcf4\ub2f9": "#d0d",
    u"\uc815\uc758\ub2f9": "#cc0",
    u"\ubb34\uc18c\uc18d": "#777"
}
actioncolors = {
    "yea": "green",
    "nay": "red",
    "forfeit": "gray"
}

with open("data/assembly.json") as f:
    d = json.load(f)
    d.append({"name_kr": "null", "party": "null"})
    people = dict([(r["name_kr"], r) for r in d])

with open("data/sample.json") as f:
    bills = json.load(f)


def person2party(person_name):
    person = people.get(person_name)
    if person:
        return person['party']
    else:
        return 'null'


# per_party
parties = set()
for bill in bills:
    party_votes = defaultdict(list)
    for action, names in bill["votes"].items():
        for name in names:
            party = person2party(name)
            parties.add(party)
            party_votes[party].append((name, actioncolors[action]))
    bill['party_votes'] = party_votes

# per_action
# FIXME: do not overwrite "votes"
for r in bills:
    for o in options:
        if o in r["votes"]:
            for j in range(len(r["votes"][o])):
                if r["votes"][o][j] in people:
                    r["votes"][o][j] = people[r["votes"][o][j]]
                    r["votes"][o][j]["partycolor"] = partycolors[r["votes"][o][j]["party"]]
                else:
                    r["votes"][o][j] = {"name_kr": r["votes"][o][j], "partycolor": "#999"}


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/action/')
def per_action():
    return render_template('action.html', bills=bills)


@app.route('/party/')
def per_party():
    return render_template('party.html', bills=bills, parties=sorted(list(parties)), persons=sorted(people.items()))



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5015)
