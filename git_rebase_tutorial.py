from shutit_module import ShutItModule

class git_rebase_tutorial(ShutItModule):

	def build(self, shutit):
		shutit.send('cd /myproject')
		shutit.challenge(
			'Just initialise a git repository in this folder (do not add or commit any files), then hit CTRL-] to continue.',
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
			'Create a file called "afile" with the line "Line1" in it, add and commit it to the git repository.',
			'b3d7557d0111e9f609ccc0a9697cf6cd',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['"echo Line1 > afile" will create the file.','add','"git add afile" to add the file','commit',"""'git commit -am "adding afile"' to commit the file"""],
			congratulations='OK, file create and committed!',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_5',
				'ok_container_name':'imiell/git-rebase-tutorial:step_8'
			}
		)
		shutit.challenge(
			'Add line "Line2" to file "afile", and commit it to the git repository.',
			'ad16df00e2cbe96ca966924ee9e522fd',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['"echo Line2 >> afile" will add the line to the file','"git commit -am line2added" to commit the file'],
			congratulations='OK! Line2 added and committed.',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_8',
				'ok_container_name':'imiell/git-rebase-tutorial:step_10'
			}
		)
		shutit.challenge(
			'Create a branch called feature_1, but stay on the master branch!',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['git branch feature_1'],
			congratulations='OK! feature_1 branch created.',
			follow_on_context={
				'check_command':'git branch | grep feature_1 | wc -l',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_10',
				'ok_container_name':'imiell/git-rebase-tutorial:step_11'
			}
		)
		shutit.challenge(
			'Continuing on master, add a Line3 to "afile" and commit it',
			'fd43955a1b0b8ef6231f9cf0370a07c9',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['echo Line3 >> afile, then git commit -am Line3added'],
			congratulations='OK! Line3 added and committed.',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_11',
				'ok_container_name':'imiell/git-rebase-tutorial:step_13'
			}
		)
		shutit.challenge(
			'Checkout the feature_1 branch',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['git checkout feature_1'],
			congratulations='OK! feature_1 branch checked out.',
			follow_on_context={
				'check_command':'git status -b | grep ^On.branch | grep feature_1 | wc -l',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_12',
				'ok_container_name':'imiell/git-rebase-tutorial:step_13'
			}
		)
		shutit.challenge(
			'Add a line "FeatureLine1" to this branch and commit it',
			'c049eb2a7f7f8a2fb8b3753f417f6aeb',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[],
			congratulations='OK! Line added and committed.',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_13',
				'ok_container_name':'imiell/git-rebase-tutorial:step_16'
			}
		)
		shutit.challenge(
			'Check out master, and merge feature_1 into it. Do not resolve the conflict!',
			'33b1f78c48283141013ba1108cb15f6f',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git checkout master, then git merge feature_1'],
			congratulations='OK! Un-resolved merge performed.',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_16',
				'ok_container_name':'imiell/git-rebase-tutorial:step_18'
			}
		)
		shutit.challenge(
			'Resolve the conflict, placing FeatureLine1 after Line3, and commit',
			'f950d22727f62b4c9c1a80624291e11f',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[],
			congratulations='OK! Merge done correctly.',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_18',
				'ok_container_name':'imiell/git-rebase-tutorial:step_20'
			}
		)
		shutit.challenge(
			'Now have a look at the history graph with "git log --graph --decorate --oneline", and observe that it is quite messy.',
			'f950d22727f62b4c9c1a80624291e11f',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git log --graph --decorate --oneline'],
			congratulations='OK! You might want to run the same command in future to see the state of the git repository.',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_20',
				'ok_container_name':'imiell/git-rebase-tutorial:step_20'
			}
		)
		shutit.challenge(
			'Check out the parent commit. This is a trickier one, there are at least ways to achieve this.',
			'fd43955a1b0b8ef6231f9cf0370a07c9',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git log to see the history','git checkout HEAD^'],
			congratulations='OK! Parent commit checked out.',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_20',
				'ok_container_name':'imiell/git-rebase-tutorial:step_21'
			}
		)
		shutit.challenge(
			'Force the master branch to revert back to this point.',
			'fd43955a1b0b8ef6231f9cf0370a07c9',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['You might want to try git branching with the already-used branch name. But you might need to be forceful.','git branch -f master'],
			congratulations='OK! Master branch moved.',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_21',
				'ok_container_name':'imiell/git-rebase-tutorial:step_22'
			}
		)
		shutit.challenge(
			'Check out the feature_1 branch, and rebase master against it',
			'f950d22727f62b4c9c1a80624291e11f',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git checkout feature_1, then git rebase master'],
			congratulations='OK! master re-based against feature_1',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_22',
				'ok_container_name':'imiell/git-rebase-tutorial:step_27'
			}
		)
		shutit.challenge(
			'Check out master and merge feature_1 against it',
			'f950d22727f62b4c9c1a80624291e11f',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git checkout master, then git merge feature_1'],
			congratulations='OK! Master merged with feature_1',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_27',
				'ok_container_name':'imiell/git-rebase-tutorial:step_29'
			}
		)
		shutit.challenge(
			'Now have a look at the history graph with "git log --graph --decorate --oneline", comparing it with before. It is a lot cleaner!',
			'f950d22727f62b4c9c1a80624291e11f',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git log --graph --decorate --oneline'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_20',
				'ok_container_name':'imiell/git-rebase-tutorial:step_20'
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
