1.gitignore 不起作用  
`git rm -r --cached .`
原因：  
 .gitignore只能忽略那些原来没有被track的文件，如果某些文件已经被纳入了版本管理中，则修改.gitignore是无效的


 2.将一个分支完全替换成另一个分支
`git checkout master` // 切换到旧的分支

`git reset --hard develop` // 将本地的旧分支 master 重置成 develop

`git push origin master --force` // 再推送到远程仓库