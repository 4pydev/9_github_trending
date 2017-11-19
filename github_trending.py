import requests


def get_trending_repositories(top_size):
    github_url = "https://api.github.com/search/repositories"
    search_params = {
        'q': 'created:>2017-11-12',
        'page': '1',
        'per_page': str(top_size),
        'sort': 'stars',
        'order': 'desc'
    }
    response = requests.get(github_url, search_params)
    repos_list = response.json()['items']

    return repos_list


def get_open_issues_amount(repo):
    return repo['open_issues']


if __name__ == '__main__':
    top_size = 20
    trending_repositories = get_trending_repositories(top_size)
    for repo in trending_repositories:
        print('-------------------------------------')
        print("Repository owner: {owner}\nRepository name: {name}\nURL: {repo_url}"
              "\nOpen issuues: {issues}"
            .format(owner=repo['owner']['login'],
                    name=repo['name'],
                    repo_url=repo['owner']['html_url']+'/'+repo['name'],
                    issues=get_open_issues_amount(repo)))
