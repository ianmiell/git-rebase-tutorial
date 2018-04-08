from shutit_module import ShutItModule

class git_rebase_tutorial(ShutItModule):

	def build(self, shutit):
		import sys
		sys.exit(0)
		shutit.send('cd /myproject')
		shutit.challenge(
			'''In this tutorial you will be asked to build up a git repo and
manage a feature branch so that history can be managed cleanly.

First we'll build up a simple project with parallel feature and master
branches and do a naive merge. Then we will revert our changes and perform a
much cleaner rebase followed by a merge. This will show you the value of
rebasing to a master branch before doing a merge.

At most stages you will be shown a visualised output of git log so you can see
the state of its history.

You have a full bash shell, so can use vi, less, man etc..
________________________________________________________________________________

If any tools are missing or there are bugs raise a github request or contact
@ianmiell on twitter.
________________________________________________________________________________

CTRL-] (right angle bracket) to continue.
________________________________________________________________________________
''',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['Hit CTRL-]'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'echo 1',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_4',
				'ok_container_name':'imiell/git-rebase-tutorial:step_4'
			}
		)
		shutit.challenge(
			'''Initialise a git repository in this folder (do not add or commit any files!), then hit CTRL-] to continue.
________________________________________________________________________________''',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['init','ask again to get answer','git init'],
			congratulations='OK, repository created!',
			follow_on_context={
				'check_command':'ls -a1 .git | grep HEAD | wc -l',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_4',
				'ok_container_name':'imiell/git-rebase-tutorial:step_5'
			}
		)
		shutit.challenge(
			'''1) Create a file called "afile" with the line "Line1" in it
2) Add and commit the file to the git repository.
________________________________________________________________________________''',
			'5596bf0e157e6d7d7f0a5034e8609c13',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['"echo Line1 > afile" will create the file.','add','"git add afile" to add the file','commit',"""'git commit -am "adding afile"' to commit the file"""],
			congratulations='OK, file create and committed!',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_5',
				'ok_container_name':'imiell/git-rebase-tutorial:step_8'
			}
		)
		shutit.challenge(
			'''1) Add line "Line2" to file "afile"
2) Commit the changed file to the git repository.
________________________________________________________________________________''',
			'6657ee19dcb40c5dfcdbf91f1e45a918',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['"echo Line2 >> afile" will add the line to the file','"git commit -am line2added" to commit the file'],
			congratulations='OK! Line2 added and committed.',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_8',
				'ok_container_name':'imiell/git-rebase-tutorial:step_10'
			}
		)
		shutit.challenge(
			'''Create a branch called feature_1, but stay on the master branch!
________________________________________________________________________________''',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['git branch feature_1'],
			congratulations='OK! feature_1 branch created.',
			follow_on_context={
				'check_command':'''git branch | grep '^[^*] feature_1' | wc -l''',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_10',
				'ok_container_name':'imiell/git-rebase-tutorial:step_11'
			}
		)
		shutit.challenge(
			'''1) Continuing on master, add a Line3 to "afile"
2) Commit the change
________________________________________________________________________________''',
			'd948490d6683d647c3619c9082eac4e0',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['echo Line3 >> afile, then git commit -am Line3added'],
			congratulations='OK! Line3 added and committed.',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_11',
				'ok_container_name':'imiell/git-rebase-tutorial:step_13'
			}
		)
		shutit.challenge(
			'''Checkout the feature_1 branch
________________________________________________________________________________''',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['git checkout feature_1'],
			congratulations='OK! feature_1 branch checked out.',
			follow_on_context={
				'check_command':'git status -b | grep ^On.branch | grep feature_1 | wc -l',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_13',
				'ok_container_name':'imiell/git-rebase-tutorial:step_14'
			}
		)
		shutit.challenge(
			'''1) Add a line "FeatureLine1" to "afile" on this (feature_1) branch
2) Commit it
________________________________________________________________________________''',
			'1984e7dfbc27dfe90401a15c8b969a27',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[],
			congratulations='OK! Line added and committed.',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_14',
				'ok_container_name':'imiell/git-rebase-tutorial:step_16'
			}
		)
		shutit.challenge(
			'''1) Check out master
2) Merge feature_1 into master.
3) Resolve the conflict, placing FeatureLine1 after Line3
4) Commit the merge
________________________________________________________________________________''',
			'6caf372d723434c8ca900b2bfb9f03e5',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git checkout master, then git merge feature_1'],
			congratulations='OK! Merge done correctly.',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_16',
				'ok_container_name':'imiell/git-rebase-tutorial:step_20'
			}
		)
		shutit.challenge(
			'''Now have a look at the history graph with "git log --graph --decorate --oneline", and observe that it is quite messy.
________________________________________________________________________________''',
			'6caf372d723434c8ca900b2bfb9f03e5',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git log --graph --decorate --oneline'],
			congratulations='OK! You might want to run the same command in future to see the state of the git repository.',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_20',
				'ok_container_name':'imiell/git-rebase-tutorial:step_20'
			}
		)
		# TODO: list the other two ways
		shutit.challenge(
			'''We are going to back out this merge in the git history

Check out the commit before FeatureLine1 was added.

This is a trickier one, there are at least three ways to achieve this.
________________________________________________________________________________''',
			'6657ee19dcb40c5dfcdbf91f1e45a918',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git log to see the history','git checkout <ID>','git checkout HEAD^'],
			congratulations='OK! Parent commit checked out. The three ways were:\n\tgit checkout HEAD^\n\tgit checkout <commit id>\n\tgit checkout HEAD~1',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_20',
				'ok_container_name':'imiell/git-rebase-tutorial:step_21'
			}
		)
		shutit.challenge(
			'''Force the master branch to be pointed to the point in the history you have just checked out.\n\nOnce that is done, check out the just-moved master branch.\n\nAll you are doing here is reverting your git tree to a previous point so that we can have a cleaner git history. This is not the rebase step!
________________________________________________________________________________

If you are confused here, just use the help (CTRL-h) as it is not important to the tutorial.
________________________________________________________________________________''',
			'3b587ce6aaf50a10a82b983d194f22f8',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['You might want to try git branching with the already-used branch name. But you might need to be forceful.','git branch -f master && git checkout master'],
			congratulations='OK! Master branch moved.',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) <(git branch | wc -l) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_21',
				'ok_container_name':'imiell/git-rebase-tutorial:step_22'
			}
		)
		shutit.challenge(
			'''1) Check out the feature_1 branch
2) Rebase master against feature_1
________________________________________________________________________________''',
			'aba6936fbcef02637df5f7b07fb8084e',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git checkout feature_1, then git rebase master'],
			congratulations='OK! master re-based against feature_1',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) <(git branch | wc -l) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_22',
				'ok_container_name':'imiell/git-rebase-tutorial:step_27'
			}
		)
		shutit.challenge(
			'''1) Check out master
2) Merge feature_1 against master
________________________________________________________________________________''',
			'aba6936fbcef02637df5f7b07fb8084e',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git checkout master, then git merge feature_1'],
			congratulations='OK! Master merged with feature_1',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) <(git branch | wc -l) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_27',
				'ok_container_name':'imiell/git-rebase-tutorial:step_29'
			}
		)
		shutit.challenge(
			'''Now have a look at the history graph with "git log --graph --decorate --oneline", comparing it with before. It is a lot cleaner than it was before!
________________________________________________________________________________''',
			'aba6936fbcef02637df5f7b07fb8084e',
			'aba6936fbcef02637df5f7b07fb8084e',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git log --graph --decorate --oneline'],
			congratulations='OK!',
			follow_on_context={
				'check_command':r"echo $(cat afile <(git status -s) <(find *) <(git branch | wc -l) | tr -d '\n')",
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_29',
				'ok_container_name':'imiell/git-rebase-tutorial:step_29'
			}
		)
		return True
	
def module():
	return git_rebase_tutorial(
		'tk.shutit.git_rebase_tutorial', 1845506479.0001,
		description='Git rebase tutorial',
		maintainer='ian.miell@gmail.com',
		delivery_methods=['docker'],
		depends=['shutit.tk.setup']
	)
