import git, datetime

def check_for_updates():
    last_update_file = open('last_update_timestamp', mode='r')
    last_update_time = datetime.datetime.fromtimestamp(int(last_update_file.readline()))
    check_update_threshold = 24.0
    now = datetime.datetime.now().replace(microsecond=0)
    diff = now-last_update_time
    if diff.total_seconds()/3600 > check_update_threshold:
        repo = git.Repo(search_parent_directories=True)
        repo.remotes.origin.fetch()
        latest_tag = ""
        last_update_file = open('last_update_timestamp', mode='w')
        last_update_file.write((datetime.datetime.now().strftime('%s')))
        last_update_file.close()
        for tag in repo.tags:
            latest_tag = tag
        if str(latest_tag) != repo.git.describe():
            return 'There is a new update. Please perform "git pull" first. In case of docker, please do "docker pull image_similarity:{0}"'.format(str(latest_tag))
        else:
            return 'Everything is up to date'
    else:
        return 'Already checked for update in last {0} hours'.format(check_update_threshold)

if __name__ == '__main__':
    print(check_for_updates())