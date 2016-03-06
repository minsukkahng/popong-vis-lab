# -*- coding: utf-8 -*-

import json
with open('data/sample.json') as f:
    vote_statements = json.load(f)

meeting.votes = []

options = ['yea', 'nay', 'forfeit']

for stmt in vote_statements:
    for option in options:
        if option in stmt['votes']:
            for person_name in stmt['votes'][option]:
                person = guess_attendee(attendees, person_name)
                statement = guess_statement(statements, stmt['name']) # TODO: this method needs to be implemented
                item = create_vote(meeting, statement, person, option)
                session.add(item)
                meeting.votes.append(item)

def create_vote(meeting, statement, person, option):
    item = MeetingStatementVote(
        meeting_id=meeting.id,
        statement_id=statement['id']
        person_id=person.id if person else None,
        vote=option,
    )
    return item


