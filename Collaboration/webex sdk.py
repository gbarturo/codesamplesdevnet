from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI(
    access_token='Yzg3MjYwZjUtYmY3ZC00OWExLWI5ZmQtMTMzZmY4ZjgxY2UxMzZkNjFjOTAtMGRk_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f')

#### GET TEAM INFO ###

teams = api.teams.list()

for team in teams:
    print(team)
    if getattr(team, 'name') != 'CBT Team':
        create_team = api.teams.create('CBT Team')
        teamId = getattr(create_team, 'id')
    else:
        teamId = team.id


###### PEOPLE #####
print(api.people.me())
print(api.people.list())
api.people.create(emails=['ben.finkel@cbtnuggets.com'], displayName='Ben Finkel', firstName='Ben',
                  lastName='Finkel', roles=['Y2lzY29zcGFyazovL3VzL1JPTEUvaWRfZnVsbF9hZG1pbg'])

#### ROLES #####
roles = api.roles.list()
# print(roles)
for role in roles:
    print(role)


#### ROOMS #####
rooms = api.rooms.list()
evaluator = False
for room in rooms:
    if room.title == 'CBT Room':
        evaluator = True
        roomId = room.id

if evaluator == False:
    new_room = api.rooms.create('CBT Room', teamId=teamId)
    roomId = new_room.id


#### MESSAGES ####
api.messages.create(roomId, text='Posted from the SDK')

# CLEANUP
# for room in rooms:
#     if getattr(room, 'title') == 'CBT Room':
#         api.rooms.delete(getattr(room, 'id'))

# for team in teams:
#     if getattr(team, 'name') == 'CBT Team':
#         api.teams.delete(getattr(team, 'id'))
