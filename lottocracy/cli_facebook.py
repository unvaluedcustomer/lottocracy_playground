import json
import random
import secrets
import urllib.parse

import requests
from docopt import docopt
from PyInquirer import prompt


class Facebook:
    """Lottocracy Facebook playground

    Usage:
        lottocracy facebook <access_token>
        lottocracy facebook <access_token> batch [<answers>...]

    Options:
        -h --help     Show this screen.
        --version     Show version.
    """

    def __init__(self):
        pass

    @staticmethod
    def clean_key(key: str) -> str:
        return '_' + key.strip().replace('-', '_').replace('<', '').replace('>', '')

    def request(self, path, query=None):
        if query is None:
            query = {}
        query['access_token'] = self._access_token
        response = requests.get(f"https://graph.facebook.com/v10.0/{path}", params=query)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(f'Status code {response.status_code} from Facebook {response.text}')

    def ask_questions(self, questions):
        enumerated_answers = {}
        answers = {}
        if self._answers:
            for question in questions:
                answer = self._answers.pop(0)
                if question['type'] in ('list', 'rawlist'):
                    if answer.isdigit():
                        answers[question['name']] = question['choices'][int(answer)-1]
                    else:
                        assert answer in question['choices']
                        answers[question['name']] = answer
                else:
                    answers[question['name']] = answer
        else:
            answers = prompt(questions)
        for question in questions:
            for answer_key, answer_value in answers.items():
                if question['type'] in ('list', 'rawlist'):
                    for choice in enumerate(question['choices']):
                        if choice[1] == answer_value:
                            enumerated_answers[answer_key] = choice
                            break
                else:
                    enumerated_answers[answer_key] = (0, answer_value)
        return enumerated_answers

    def execute(self, argv):
        args = docopt(self.__class__.__doc__, argv)
        for key, value in args.items():
            setattr(self, Facebook.clean_key(key), value)
        answers = self.ask_questions([{'type': 'rawlist',
                      'name': 'action',
                      'message': 'What do you want to do?',
                      'choices': ['Run Lottery On Facebook Group']
                      }])
        if answers['action'][0] == 0:
            self.run_lottery()

    def run_lottery(self):
        group_data = self.request("me", query={'fields':'groups'})['groups']['data']
        answers = self.ask_questions([{'type': 'list',
                      'name': 'group',
                      'message': 'Which group should the lottery be run on?',
                      'choices': [group['name'] for group in group_data]
                      }])
        group_id = list(filter(lambda g: g['name'] == answers['group'][1], group_data))[0]['id']
        opted_in_members = self.request(f'{group_id}/opted_in_members')['data']
        print(f'Found {len(opted_in_members)} members')
        answers = self.ask_questions([{'type': 'input',
                      'name': 'max_size',
                      'message': 'What is the maximum group size that should be used?',
                      'validate': lambda x: x.isdigit(),
                      }])
        chunk_size = max(int(len(opted_in_members)/int(answers['max_size'][1])), 3)
        random.shuffle(opted_in_members)
        print([chunk for chunk in opted_in_members[::chunk_size]])
