import os
import subprocess
from datetime import datetime, timedelta

# # 指定日期范围（例如，27号）
# target_date = '2024-01-20'
# start_date = datetime.strptime(target_date, "%Y-%m-%d")
# end_date = start_date + timedelta(days=1)
# 获取当前日期
current_date = datetime.now().strftime("%Y-%m-%d")
# GitHub 主仓库 URL
main_repo_url = 'https://github.com/Vinci230/exam-_test.git'

# 克隆主仓库到临时目录
main_repo_path = 'main_repo'
git_clone_command = ['git', 'clone','--recursive', main_repo_url, main_repo_path]
subprocess.run(git_clone_command)

# 进入主仓库临时目录
os.chdir(main_repo_path)
# 获取所有子模块的路径，获取的是主仓库目录中以submoudles开头的所有文件路径，返回一个迭代器
submodule_paths = [item.path for item in os.scandir() if item.is_dir() and item.name.startswith('submodules/')]

# 更新子模块内容
git_submodule_update_command = ['git', 'submodule', 'update', '--recursive', '--remote']
subprocess.run(git_submodule_update_command)

# 遍历每个子模块
for submodule_path in submodule_paths:
    # 进入子模块目录
    os.chdir(submodule_path)

    # # 切换到主分支
    # git_checkout_command = ['git', 'checkout', 'main']  # 你的主分支名称，可能是 main、master 等
    # subprocess.run(git_checkout_command)
    #
    # # 拉取子模块最新的变更
    # git_pull_command = ['git', 'pull']
    # subprocess.run(git_pull_command)

    # 构建 Git 命令
    git_command = [
        'git',
        'log',
        f'--since={current_date}T00:00:00Z',  # 从今天的开始时间获取 commit
        f'--until={current_date}T23:59:59Z',  # 到今天的结束时间获取 commit
        '--pretty=format:"Commit ID: %H%nAuthor: %an <%ae>%nDate: %ad%nMessage: %s%n%n"'
    ]

    # 执行 Git 命令
    result = subprocess.run(git_command, stdout=subprocess.PIPE, text=True, encoding='utf-8')

    # 返回主仓库目录，将工作目录切换回主仓库的目录，确保每个子模块都在其自己的目录中执行 Git 操作，避免可能的问题和冲突。
    os.chdir(main_repo_path)

    # readneme path
    readme_path = 'D:/Users/Vinci/Desktop/exam-_test/README.md'

    # 将提交信息追加到README文件
    with open(readme_path, 'a', encoding='utf-8') as readme_file:
        readme_file.write('\n\n' + result.stdout)
    # 打印 commit 信息
    # print(result.stdout)
