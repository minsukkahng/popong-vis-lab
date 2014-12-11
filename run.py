from flask import Flask
from flask import render_template
import simplejson as json

app = Flask(__name__)

@app.route('/')
def vote():
	# dict for people info
	d_people = {}
	
	with open("data/assembly.json") as json_file:
		people = json.load(json_file)
		d_people = dict([(r["name_kr"], r) for r in people])
	
	options = ["yea", "nay", "forfeit"]
	d_partycolor = {u"\uc0c8\ub204\ub9ac\ub2f9": "#d00", u"\uc0c8\uc815\uce58\ubbfc\uc8fc\uc5f0\ud569": "#07d", u"\ud1b5\ud569\uc9c4\ubcf4\ub2f9": "#d0d", u"\uc815\uc758\ub2f9": "#cc0", u"\ubb34\uc18c\uc18d": "#777"}
	
	with open("data/sample.json") as json_file:
		votes = json.load(json_file)
		
		# for finding his/her party
		for r in votes:
			for o in options:
				if o in r["votes"]:
					for j in range(len(r["votes"][o])):
						if r["votes"][o][j] in d_people:
							r["votes"][o][j] = d_people[r["votes"][o][j]]
							r["votes"][o][j]["partycolor"] = d_partycolor[r["votes"][o][j]["party"]]
						else:
							r["votes"][o][j] = {"name_kr": r["votes"][o][j], "partycolor": "#999"}
							
	return render_template('vote.html', data=votes)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5015)