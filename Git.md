# Git的一些相关问题
# 问题描述
```bash
      remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
      remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
      fatal: unable to access 'https://github.com/enticejin/python.git/': The requested URL returned error: 403
```

# 解决办法
```bash
    #your_token 在github中生成的token
    #USERNAME 在GitHub中的用户名（不是你的登录账号）
    #REPO 仓库名
    git remote set-url origin https://<your_token>@github.com/<USERNAME>/<REPO>.git

    例如：
     git remote set-url origin https://xxx@github.com/xxx/xxx.git
```
# 问题描述
```bash
       git pull origin master
       fatal: unable to access 'https://github.com/enticejin/python.git/': Failed to connect to github.com port 443: Timed out
```
# 解决办法
```bash
        git config --global --unset git.proxy
```
# 问题描述
```bash
		Push failed
			Unable to access 'https://github.com/enticejin/python.git/': OpenSSL SSL_read: Connection was reset, errno 10054
```
# 解决办法
```bash
		git config --global http.sslVerify "false"
```
# 问题描述
```bash
		Push failed
			Unable to access 'https://github.com/enticejin/python.git/': Failed to connect to github.com port 443: Timed out
```
# 解决办法
```bash
		出现这种情况一般都是代理出了问题
		将C:\Windows\System32\drivers\etc文件夹下的HOSTS文件中的github.com删掉重新push
```
# 全部PUSH命令
```bash
		git add .
		git commit -m “your comment”
		git push -u origin master -f
        2021-09-27：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
```
