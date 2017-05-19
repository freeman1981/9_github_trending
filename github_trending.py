import requests
from datetime import date, timedelta


def get_trending_repositories(top_size, for_day_count):
    start_date = date.today() - timedelta(days=for_day_count)
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'created:>={}'.format(start_date),
        'sort': 'stars',
        'order': 'desc',
        'per_page': top_size
    }
    response_dict = requests.get(url, params).json()
    return response_dict['items']


def show_repository_info(repository):
    print('*' * 100)
    print('''
    Repository name: {name}
    Repository owner: {owner}
    Count open issues: {issues}
    Repository url: {url}
    '''.format(
        name=repository['name'],
        owner=repository['owner']['login'],
        issues=repository['open_issues_count'],
        url=repository['html_url']
    ))

if __name__ == '__main__':
    top_size = 20
    day_count = 7
    repositories = get_trending_repositories(top_size, day_count)
    for repository in repositories:
        show_repository_info(repository)
