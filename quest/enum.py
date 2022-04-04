QUEST_INFO = {
	'history': {
		'name': 'History',
		'quest_id': 1,
		'password': 'history',
	},
	'story': {
		'name': 'Story',
		'quest_id': 2,
		'password': 'story',
	},
	'connect': {
		'name': 'Connect',
		'quest_id': 3,
		'password': 'connect',
	},
	'activity': {
		'name': 'Activity',
		'quest_id': 4,
		'password': 'activity',
	},
	'structure': {
		'name': 'Structure',
		'quest_id': 5,
		'password': 'structure',
	}
}

def get_quest_info(quest_name):
	return QUEST_INFO[quest_name]
