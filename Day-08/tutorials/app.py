import os

# print(os.name)                # 'posix' hoặc 'nt'
# print(os.getenv('HOME'))      # thư mục home (Unix) hoặc None
# print(os.environ.get('PATH')) # PATH


cwd = os.getcwd()
print("Current:", cwd)

for name in os.listdir('.'):
    print(name)