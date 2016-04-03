# -*- coding: utf-8 -*-
from collections import defaultdict
import json

pre_name_no = {}
precincts = {}

province_code_map = {u"\uC11C\uC6B8": 11, u"\uBD80\uC0B0": 21, u"\uB300\uAD6C": 22, u"\uC778\uCC9C": 23, u"\uAD11\uC8FC": 24, u"\uB300\uC804": 25, u"\uC6B8\uC0B0": 26, u"\uc138\uc885\ud2b9\ubcc4\uc790\uce58\uc2dc": 29, u"\uACBD\uAE30": 31, u"\uAC15\uC6D0": 32, u"\uCDA9\uBD81": 33, u"\uCDA9\uB0A8": 34, u"\uC804\uBD81": 35, u"\uC804\uB0A8": 36, u"\uACBD\uBD81": 37, u"\uACBD\uB0A8": 38, u"\uC81C\uC8FC": 39}

party_color_map = {u"새누리당": "#C9252B", u"더불어민주당":"#025AAA", u"국민의당": "#659F32", u"정의당": "#FFCB08", u"무소속": "#999999"}
		
mismatch = {u'여주시양평군가평군': u'여주군양평군가평군'}

# File containing mapping municipalities in each precinct to code in map files
with open('files/precinct_table_mapping_19.tsv', 'r') as f:
	for l in f:
		t = l.split("\t")
		pre_name_no[(int(t[2][:2]), t[1])] = int(t[0])
print pre_name_no

# List of persons obtained from popong api (downloaded on March 11)
with open('files/popongdump_assembly.json', 'r') as f:
	d = json.load(f)
	for r in d:
		print r["name_en"]
		province = r["district"].split(" ")[0]
		if province != u'비례대표':
			province_code = province_code_map[province]
			precinct_name = r["district"].split(" ")[-1]
			if precinct_name in mismatch: precinct_name = mismatch[precinct_name]
			distno = pre_name_no[(province_code, precinct_name.encode("utf-8"))]
			partycolor = party_color_map[r["party"]] if r["party"] in party_color_map.keys() else "#999999"
			precincts[distno] = {"no": distno, "precinct_name": precinct_name, "person_name": r["name_kr"], "party": r["party"], "party_color": partycolor, "image": r["photo"], "province_code": province_code}

data = {"precincts": precincts}
with open('precinct_person.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

