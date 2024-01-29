import git
from datetime import datetime, timedelta, timezone
import subprocess

def get_commits_for_day(repo_url, day):
    # 通过 git.remote.Remote 访问远程仓库
    repo = git.Repo.clone_from(repo_url, 'temp_repo', branch='main')

    # 获取昨天和今天的日期范围
    start_date = datetime.strptime(day, "%Y-%m-%d")
    print(start_date)
    end_date = start_date + timedelta(days=1)
    # end_date = end_date.replace(tzinfo=timezone(timedelta(hours=8)))
    print(end_date)

    commits = repo.iter_commits(rev='main',since=start_date)
    # print(commits)

    # 遍历指定日期范围内的提交
    for commit in commits:

        print(f"Commit ID: {commit.hexsha}")
        print(f"Author: {commit.author.name} <{commit.author.email}>")
        print(f"Date: {commit.authored_datetime}")
        print(f"Message: {commit.message}")
        print("\n")


def main():
    repo_url = 'https://github.com/Vinci230/2024-lanshanexam.git'  # 替换为你的 HTTPS 形式的仓库 URL
    day_to_check = '2023-01-23'  # 替换为你想要查看的日期

    get_commits_for_day(repo_url, day_to_check)


if __name__ == "__main__":
    main()
