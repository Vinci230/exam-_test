import os
import subprocess
from datetime import datetime, timedelta

# 获取当前日期
current_date = datetime.now().strftime("%Y-%m-%d")
# GitHub 主仓库 URL
main_repo_url = 'https://github.com/Vinci230/exam-_test.git'
#先更新主仓库的子模块
git_submodule_update_command = ['git', 'submodule', 'update', '--recursive', '--remote']
subprocess.run(git_submodule_update_command)
# 进入主仓库目录
os.chdir('D:/Users/Vinci/Desktop/exam-_test/submodules')

# 获取所有子模块的路径，获取的是主仓库目录中以 submodules 开头的所有文件路径，返回一个迭代器

submodules_path = 'D:/Users/Vinci/Desktop/exam-_test/submodules'
submodule_paths = [os.path.join(submodules_path, item.name) for item in os.scandir(submodules_path) if item.is_dir()]
print(submodule_paths)

# readneme 路径
readme_path = 'D:/Users/Vinci/Desktop/exam-_test/README.md'



for submodule_path in submodule_paths:

    print(submodule_path)
    # 构建 Git 命令
    git_command = [
        'git',
        'log',
        f'--since={current_date}T00:00:00Z',  # 从今天的开始时间获取 commit
        f'--until={current_date}T23:59:59Z',  # 到今天的结束时间获取 commit
        '--pretty=format:"Commit ID: %H%nAuthor: %an <%ae>%nDate: %ad%nMessage: %s%n%n"'
    ]
    # 进入子模块目录
    os.chdir(submodule_path)
    # 执行 Git 命令
    result = subprocess.run(git_command, stdout=subprocess.PIPE, text=True, encoding='utf-8')

# 将提交信息追加到README文件
    with open(readme_path, 'a', encoding='utf-8') as readme_file:
        readme_file.write('\n\n' + result.stdout)
# 返回主仓库目录，确保每个子模块都在其自己的目录中执行 Git 操作，避免可能的问题和冲突。
    os.chdir('D:/Users/Vinci/Desktop/exam-_test/submodules')

#         # 打印每个子模块的 commit 信息
#     print(result.stdout)
# # 打印 commit 信息
# # print(result.stdout)
