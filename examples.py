from __future__ import print_function
import time, subprocess
from utils import call_repo_command, color_it, change_file


#py2/3 hack
try:
    input = raw_input
except NameError:
    pass


def example_one():
    '''Example for git commit --amend'''

    text = """Example #1: Amending a commit\n
            In this example, we'll modify a file, stage the file,
            commit the changes and then make further changes. These
            changes are related to the first commit and should just be
            lumped in there. We'll add the file again and run:
            git commit --amend to alter our last commit. We'll see later
            how git commit --amend is really just a special case of git
            rebase -i.
           """
    print(color_it(text, 'white'))
    input(color_it('Press enter to continue...', 'yellow'))
    text = "First, we'll make some changes to the README and save 'em...."
    print(color_it(text, 'white'))
    change_file('README.md', "The time is now: "+ time.strftime('%c',
                                                                time.localtime()))
    input(color_it('\nPress enter to continue...', 'yellow'))
    print(color_it("Now we'll check our git status..."))
    call_repo_command(['git', 'status'], wait=True)
    print(color_it("Now let's add the file"))
    time.sleep(1)
    call_repo_command(['git', 'add', 'README.md'], wait=True)
    print(color_it("We'll commit that file; go ahead and add a commit message"))
    input(color_it('Press enter to continue...', 'yellow'))
    print(color_it("Running command: ", 'red') + color_it('git commit'))
    time.sleep(1)
    subprocess.call(['git', 'commit'], cwd='repo')
    input(color_it('Press enter to continue...', 'yellow'))
    print(color_it("Let's look at our git log..."))
    call_repo_command(['git', 'log'])
    print(color_it("There's our first commit"))
    input(color_it('Press enter to continue...', 'yellow'))
    print(color_it("Rad, now let's make another change..."))
    change_file('README.md', "READ ME! The time is now: "+ time.strftime('%c',
                                                                time.localtime()))
    input(color_it('Press enter to continue...', 'yellow'))
    print(color_it("Now let's add the file again"))
    call_repo_command(['git', 'add', 'README.md'], wait=True)
    print(color_it("And this time we'll use git commit --amend\n"))
    print(color_it("Change your message if you like."))
    print(color_it("Running command: ", 'red') + color_it('git commit --amend'))
    time.sleep(1)
    subprocess.call(['git', 'commit', '--amend'], cwd='repo')
    input(color_it('Press enter to continue...', 'yellow'))
    print(color_it("Let's look at our git log..."))
    call_repo_command(['git', 'log'])
    print(color_it("And we see just the one commit"))
    print(color_it("git commit --amend is cool!"))
    time.sleep(1)
    print(color_it("That's the end of example 1"))
    input(color_it('Press enter to move to the next example...', 'yellow'))


def example_two():
    """ git rebase -i changing order of commits """
    pass


def example_three():
    """ git rebase -i changing order of commits """
    pass


def example_four():
    """ git rebase -i change order, squash etc """
    pass


