import requests
import json


def get_trending_repositories(top_size):
    url = 'https://api.github.com/search/repositories?sort=stars&q=stars'
    result = requests.get(url)
    data = json.loads(result.text)
    return data


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{owner}/{repo}/issues'.format(owner=repo_owner, repo=repo_name)
    result = requests.get(url)
    data = json.loads(result.text)
    return data

if __name__ == '__main__':
    data = get_trending_repositories(123)
    for item in data['items']:
        print('*'*100)
        print('Name={name}:Owner={owner}:Issues={issues}:url={url}'.format(
            name=item['name'], owner=item['owner']['login'], issues=item['open_issues_count'], url=item['html_url']
        ))
        data = get_open_issues_amount(item['owner']['id'], item['id'])
        pass
