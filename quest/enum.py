QUEST_INFO = {
	'history': {
		'name': 'History',
		'quest_id': 1,
		'password': 'history',
		'next_quest': 'story',
	},
	'story': {
		'name': 'Story',
		'quest_id': 2,
		'password': 'story',
		'next_quest': 'connect',
	},
	'connect': {
		'name': 'Connect',
		'quest_id': 3,
		'password': 'connect',
		'next_quest': 'activity',
	},
	'activity': {
		'name': 'Activity',
		'quest_id': 4,
		'password': 'activity',
		'next_quest': 'structure',
	},
	'structure': {
		'name': 'Structure',
		'quest_id': 5,
		'password': 'structure',
		'next_quest': None,
	}
}

def get_quest_info(quest_name):
	# if not exist, return None
	if quest_name not in QUEST_INFO:
		return None

	return QUEST_INFO[quest_name]
