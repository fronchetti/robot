import os
import json
import uuid 
from datetime import datetime

def get_experiment_status():
    if os.path.isfile('data/last_experiment.json'):
        with open('data/last_experiment.json', 'r') as status_file:
            experiment_status = json.load(status_file)
    else:
        experiment_status = set_experiment_status(status=True)

    return experiment_status

def set_experiment_status(status, participant_id = None):
    if not os.path.isdir('data'):
        os.mkdir('data')

    with open('data/last_experiment.json', 'w') as status_file:

        if participant_id is None:
            participant_id = uuid.uuid4().hex

        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        experiment_status = {'status': status, 'participant_id': str(participant_id), 'last_update': timestamp}
        json_data = json.dumps(experiment_status)
        status_file.write(json_data)

    return experiment_status