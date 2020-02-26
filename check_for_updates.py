import git

def check_for_updates():
    repo = git.Repo(search_parent_directories=True)
    repo.remotes.origin.fetch()
    latest_tag = ""
    for tag in repo.tags:
        latest_tag = tag
    if str(latest_tag) != repo.git.describe():
        return 'There is a new update. Please perform "git pull" first. In case of docker, please do "docker pull image_similarity:{0}"'.format(str(latest_tag))
    else:
        return 'Everything is up to date'

if __name__ == '__main__':
    print(check_for_updates())