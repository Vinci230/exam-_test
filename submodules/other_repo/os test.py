import os
import subprocess
from datetime import datetime, timedelta

# 指定日期范围（例如，27号）
target_date = '2024-01-27'
start_date = datetime.strptime(target_date, "%Y-%m-%d")
end_date = start_date + timedelta(days=1)
# GitHub 仓库 URL
repo_url = 'https://github.com/Vinci230/2024-lanshanexam.git'

# 克隆仓库到临时目录
temp_repo_path = 'temp_repo'
git_clone_command = ['git', 'clone', repo_url, temp_repo_path]
subprocess.run(git_clone_command)

# 进入临时目录
os.chdir(temp_repo_path)

# 构建 Git 命令
git_command = [
    'git',
    'log',
    f'--since={start_date.isoformat()}',
    f'--until={end_date.isoformat()}',
    '--pretty=format:"Commit ID: %H%nAuthor: %an <%ae>%nDate: %ad%nMessage: %s%n%n"'
]

# 执行 Git 命令
result = subprocess.run(git_command, stdout=subprocess.PIPE, text=True,encoding='utf-8')
#readneme path
readme_path = 'D:/Users/Vinci/Desktop/2024-lanshanexam/README.md'
# 将提交信息追加到README文件
with open(readme_path, 'a', encoding='utf-8') as readme_file:
    readme_file.write('\n\n' + result.stdout)
# 打印 commit 信息
#print(result.stdout)
