from shutit_module import ShutItModule

class git_rebase_tutorial(ShutItModule):

	def build(self, shutit):
		shutit.send('cd /myproject')
		shutit.challenge(
			'Initialise a git repository.',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['init','ask again to get answer','git init'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'ls -a1 .git | grep HEAD | wc -l',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_4',
				'ok_container_name':'imiell/git-rebase-tutorial:step_5'
			}
		)
		shutit.challenge(
			'Create a file called "afile" with the line "Line1" in it, add commit it to the git repository.',
			'b3d7557d0111e9f609ccc0a9697cf6cd',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_5',
				'ok_container_name':'imiell/git-rebase-tutorial:step_8'
			}
		)
		shutit.challenge(
			'Create a file called "afile" with the line "Line2" in it, add commit it to the git repository.',
			'ad16df00e2cbe96ca966924ee9e522fd',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_8',
				'ok_container_name':'imiell/git-rebase-tutorial:step_10'
			}
		)
		shutit.challenge(
			'Create a branch called feature_1, but do not move to it.',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=[],
			congratulations='OK!',
			follow_on_context={
				'check_command':'git branch | grep feature_1 | wc -l',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_10',
				'ok_container_name':'imiell/git-rebase-tutorial:step_11'
			}
		)
		shutit.challenge(
			'Continuing on master, add a Line3 to afile and commit it',
			'fd43955a1b0b8ef6231f9cf0370a07c9',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[],
			congratulations='OK!',
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
			hints=[],
			congratulations='OK!',
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
			congratulations='OK!',
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
			hints=[],
			congratulations='OK!',
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
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_18',
				'ok_container_name':'imiell/git-rebase-tutorial:step_20'
			}
		)
		#git checkout HEAD^
		shutit.challenge(
			'Check out the parent commit',
			'fd43955a1b0b8ef6231f9cf0370a07c9',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_20',
				'ok_container_name':'imiell/git-rebase-tutorial:step_21'
			}
		)
		#git branch -f master
		shutit.challenge(
			'Force the master branch to revert back to this point.',
			'fd43955a1b0b8ef6231f9cf0370a07c9',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[],
			congratulations='OK!',
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
			hints=[],
			congratulations='OK!',
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
			hints=[],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat afile <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-rebase-tutorial:step_27',
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
