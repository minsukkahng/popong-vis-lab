import psycopg2
from collections import defaultdict
import json

with open('database_config.json', 'r') as config_file:
	config = json.load(config_file)
	conn = psycopg2.connect(host=config["host"], port=config["port"], database=config["database"], user=config["user"], password=config["password"])
cur = conn.cursor() 

q = """
	SELECT c.vote_score, district_id, district, 
		c.person_id, p.name, p.gender, p.birthday, p.image, 
		e.is_regular, 
		c.party_id, r.name, r.color
	FROM candidacy c 
	LEFT OUTER JOIN person p ON c.person_id = p.id
	LEFT OUTER JOIN election e ON c.election_Id = e.id
	LEFT OUTER JOIN party r ON c.party_id = r.id
	WHERE e.assembly_id = 19 AND c.is_elected = 't'
	ORDER BY c.id
"""
cur.execute(q)
rows = cur.fetchall()

provinces = []
municipalities = []

persons = {}
districts = {}

for r in rows:
	person_id = int(r[3])
	if person_id not in persons.keys():
		persons[person_id] = {"id": person_id, "name": r[4], "party": r[10], "party_color": r[11], "image": r[7], "districts": []}
	for j, district_id in enumerate(r[1]):
		if district_id:
			district_id = int(district_id)
			if district_id not in districts.keys():
				districts[district_id] = {"id": district_id, "name": r[2][j], "persons": []}
			districts[district_id]["persons"].append({"id": person_id, "name": persons[person_id]["name"], "district_names": " ".join(r[2])})
			persons[person_id]["districts"].append(district_id)
			
print persons
print districts

data = {"persons": persons, "districts": districts}
with open('person_district.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

conn.close()