**przydatne strony**
* https://github.com/wojciech11/se_teaching_vm_images/blob/master/vagrant/ubuntu/Vagrantfile
* https://octodex.github.com/


**komendy**

```tester@tester-m:~/nauka_gita$ git init
Initialized empty Git repository in /home/tester/nauka_gita/.git/
tester@tester-m:~/nauka_gita$ git config -l
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
tester@tester-m:~/nauka_gita$ git config --global user.name luuc13
tester@tester-m:~/nauka_gita$ git config -l
user.name=luuc13
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
tester@tester-m:~/nauka_gita$ git config --global user.email luuc13@users.noreply.github.com
tester@tester-m:~/nauka_gita$ git config -l
user.name=luuc13
user.email=luuc13@users.noreply.github.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
tester@tester-m:~/nauka_gita$ git init
Reinitialized existing Git repository in /home/tester/nauka_gita/.git/
tester@tester-m:~/nauka_gita$ ls
tester@tester-m:~/nauka_gita$ touch README.md
tester@tester-m:~/nauka_gita$ ls
README.md
tester@tester-m:~/nauka_gita$ atom README.md
tester@tester-m:~/nauka_gita$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	README.md

nothing added to commit but untracked files present (use "git add" to track)
tester@tester-m:~/nauka_gita$ ls -a
.  ..  .git  README.md
tester@tester-m:~/nauka_gita$ ls .git
branches  config  description  HEAD  hooks  info  objects  refs
tester@tester-m:~/nauka_gita$ cat .git/config
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
tester@tester-m:~/nauka_gita$ git add README.md
tester@tester-m:~/nauka_gita$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   README.md

tester@tester-m:~/nauka_gita$ git commit -m "Pierwsza wersja pliku README"
[master (root-commit) 4c7750f] Pierwsza wersja pliku README
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
tester@tester-m:~/nauka_gita$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
tester@tester-m:~/nauka_gita$ git log
commit 4c7750fe18f1d579cc9c250dfa0253e377c5eb4c (HEAD -> master)
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 09:56:40 2018 +0200

    Pierwsza wersja pliku README
tester@tester-m:~/nauka_gita$ git add README.md
tester@tester-m:~/nauka_gita$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   README.md

tester@tester-m:~/nauka_gita$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   README.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

tester@tester-m:~/nauka_gita$ git add README.md
tester@tester-m:~/nauka_gita$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   README.md

tester@tester-m:~/nauka_gita$ git commit -m "Modyfikuj"
[master 65df245] Modyfikuj
 1 file changed, 10 insertions(+)
tester@tester-m:~/nauka_gita$ git log
commit 65df2450603844b4f9e4300150d335c05b96c225 (HEAD -> master)
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 10:05:30 2018 +0200

    Modyfikuj

commit 4c7750fe18f1d579cc9c250dfa0253e377c5eb4c
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 09:56:40 2018 +0200

    Pierwsza wersja pliku README
tester@tester-m:~/nauka_gita$ git add README.md
tester@tester-m:~/nauka_gita$ git log
commit 65df2450603844b4f9e4300150d335c05b96c225 (HEAD -> master)
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 10:05:30 2018 +0200

    Modyfikuj

commit 4c7750fe18f1d579cc9c250dfa0253e377c5eb4c
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 09:56:40 2018 +0200

    Pierwsza wersja pliku README
tester@tester-m:~/nauka_gita$ git status
On branch master
nothing to commit, working tree clean
tester@tester-m:~/nauka_gita$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
tester@tester-m:~/nauka_gita$ git add README.md
tester@tester-m:~/nauka_gita$ git commit -m "kolejna modyfikacja"
[master ca04f6a] kolejna modyfikacja
 1 file changed, 2 insertions(+)
tester@tester-m:~/nauka_gita$ git status
On branch master
nothing to commit, working tree clean
tester@tester-m:~/nauka_gita$ git log
commit ca04f6a3effd2051e3903a82703eb1c78e2f27e8 (HEAD -> master)
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 10:07:55 2018 +0200

    kolejna modyfikacja

commit 65df2450603844b4f9e4300150d335c05b96c225
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 10:05:30 2018 +0200

    Modyfikuj

commit 4c7750fe18f1d579cc9c250dfa0253e377c5eb4c
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 09:56:40 2018 +0200

    Pierwsza wersja pliku README
tester@tester-m:~/nauka_gita$ git log
commit ca04f6a3effd2051e3903a82703eb1c78e2f27e8 (HEAD -> master)
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 10:07:55 2018 +0200

    kolejna modyfikacja

commit 65df2450603844b4f9e4300150d335c05b96c225
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 10:05:30 2018 +0200

    Modyfikuj

commit 4c7750fe18f1d579cc9c250dfa0253e377c5eb4c
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 09:56:40 2018 +0200

    Pierwsza wersja pliku README
tester@tester-m:~/nauka_gita$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
tester@tester-m:~/nauka_gita$ git add README.md
tester@tester-m:~/nauka_gita$ git commit -m "ostatnia modyfikacja"
[master 0b63122] ostatnia modyfikacja
 1 file changed, 2 insertions(+)
tester@tester-m:~/nauka_gita$ git log
commit 0b63122a35e01e92ca53b19b8b69e213a1c57ac2 (HEAD -> master)
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 10:08:50 2018 +0200

    ostatnia modyfikacja

commit ca04f6a3effd2051e3903a82703eb1c78e2f27e8
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 10:07:55 2018 +0200

    kolejna modyfikacja

commit 65df2450603844b4f9e4300150d335c05b96c225
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 10:05:30 2018 +0200

    Modyfikuj

commit 4c7750fe18f1d579cc9c250dfa0253e377c5eb4c
Author: luuc13 <luuc13@users.noreply.github.com>
Date:   Sun Oct 7 09:56:40 2018 +0200

    Pierwsza wersja pliku README
tester@tester-m:~/nauka_gita$ gitk
tester@tester-m:~/nauka_gita$ gitg

(gitg:5755): GLib-GIO-CRITICAL **: 10:21:02.226: g_converter_convert: assertion 'outbuf_size > 0' failed

** (gitg:5755): WARNING **: 10:21:02.226: gitg-resource.vala:33: Error while loading resource: style-unix.css:1:0Failed to import: The resource at “/org/gnome/gitg/ui/style-unix.css” failed to decompress
^C
tester@tester-m:~/nauka_gita$ git remote add origin https://github.com/luuc13/nauka_gita.git
tester@tester-m:~/nauka_gita$ git push -u origin master
Username for 'https://github.com': luuc13
Password for 'https://luuc13@github.com':
Counting objects: 12, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (7/7), done.
Writing objects: 100% (12/12), 1.05 KiB | 1.05 MiB/s, done.
Total 12 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
remote:
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/luuc13/nauka_gita/pull/new/master
remote:
To https://github.com/luuc13/nauka_gita.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
tester@tester-m:~/nauka_gita$ git add README.md
tester@tester-m:~/nauka_gita$ git commit -m "ostatnia modyfikacja"
[master 91a5c86] ostatnia modyfikacja
 1 file changed, 7 insertions(+), 1 deletion(-)
tester@tester-m:~/nauka_gita$ git push
Username for 'https://github.com': luuc13
Password for 'https://luuc13@github.com':
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 319 bytes | 319.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/luuc13/nauka_gita.git
   0b63122..91a5c86  master -> master
tester@tester-m:~/nauka_gita$ git diff
tester@tester-m:~/nauka_gita$ it g
it: command not found
tester@tester-m:~/nauka_gita$ git g
git: 'g' is not a git command. See 'git --help'.

The most similar commands are
	grep
	gc
tester@tester-m:~/nauka_gita$ gitg

(gitg:5989): GLib-GIO-CRITICAL **: 10:45:44.035: g_converter_convert: assertion 'outbuf_size > 0' failed

** (gitg:5989): WARNING **: 10:45:44.035: gitg-resource.vala:33: Error while loading resource: style-unix.css:1:0Failed to import: The resource at “/org/gnome/gitg/ui/style-unix.css” failed to decompress
^C  
tester@tester-m:~/nauka_gita$ gitk
^C
tester@tester-m:~/nauka_gita$ git checkout -b eksperyment
Switched to a new branch 'eksperyment'
tester@tester-m:~/nauka_gita$ git branch
* eksperyment
  master
tester@tester-m:~/nauka_gita$ git add README.md
tester@tester-m:~/nauka_gita$ git status
On branch eksperyment
nothing to commit, working tree clean
tester@tester-m:~/nauka_gita$ git add README.md
tester@tester-m:~/nauka_gita$ git status
On branch eksperyment
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   README.md

tester@tester-m:~/nauka_gita$ git commit -m "eksperyment"
[eksperyment 33f3f09] eksperyment
 1 file changed, 2 insertions(+)
tester@tester-m:~/nauka_gita$ git status
On branch eksperyment
nothing to commit, working tree clean
tester@tester-m:~/nauka_gita$ git push
fatal: The current branch eksperyment has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin eksperyment

tester@tester-m:~/nauka_gita$ git push --set-upstream origin eksperyment
Username for 'https://github.com': luuc13
Password for 'https://luuc13@github.com':
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 293 bytes | 293.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'eksperyment' on GitHub by visiting:
remote:      https://github.com/luuc13/nauka_gita/pull/new/eksperyment
remote:
To https://github.com/luuc13/nauka_gita.git
 * [new branch]      eksperyment -> eksperyment
Branch 'eksperyment' set up to track remote branch 'eksperyment' from 'origin'.
tester@tester-m:~/nauka_gita$ gitk
tester@tester-m:~/nauka_gita$ gitg

(gitg:6194): GLib-GIO-CRITICAL **: 11:01:03.963: g_converter_convert: assertion 'outbuf_size > 0' failed

** (gitg:6194): WARNING **: 11:01:03.963: gitg-resource.vala:33: Error while loading resource: style-unix.css:1:0Failed to import: The resource at “/org/gnome/gitg/ui/style-unix.css” failed to decompress
^C
tester@tester-m:~/nauka_gita$ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
tester@tester-m:~/nauka_gita$ git merge eksperyment
Updating 91a5c86..33f3f09
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
tester@tester-m:~/nauka_gita$ git push
Username for 'https://github.com': luuc13
Password for 'https://luuc13@github.com':
Total 0 (delta 0), reused 0 (delta 0)
To https://github.com/luuc13/nauka_gita.git
   91a5c86..33f3f09  master -> master```
