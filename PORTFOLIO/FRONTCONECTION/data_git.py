from github import Github
from .models import Project
from django.conf import settings
import os





def get_repositories(token):
    #print(token)
    git = Github(token)
    user = git.get_user()
    #print(user.login)

    repos = []

    for repo in user.get_repos():
        try:
            readme = repo.get_readme()
            text = ''.join([line.decode('utf-8') for line in readme.decoded_content.splitlines()])
            repos.append({
                'name': repo.name,
                'description': repo.description,
                'html_url': repo.html_url,
                'readme': text

            })
            #print('helo try')
        except:
            readme = None
            repos.append({
                'name': repo.name,
                'description': repo.description,
                'html_url': repo.html_url,
                'readme': readme
            })
            #print('helo except')

    #save in models Project
    #some checks wile send a data to the models

    for repo in repos:
        obj, created = Project.objects.get_or_create(
            title=repo['name'],
            description=repo['description'],
            html_url=repo['html_url'],
            readme=repo['readme']
                )
        if created:
            obj.save()
        else:
            continue

def main():
    token = settings.GITACCESSTOKEN
    get_repositories(token)

if __name__ == "__main__":
    main()
