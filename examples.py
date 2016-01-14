from __future__ import print_function
import time, subprocess, sys
from utils import call_repo_command, color_it, change_file, cleanup


#py2/3 hack
try:
    input = raw_input
except NameError:
    pass

def call_example(num):
    if num == 1:
        example_one()
    elif num == 2:
        example_two()
    elif num == 3:
        example_three()
    elif num == 4:
        example_four()
    else:
        return sys.exit()

def example_one():
    '''Example for git commit --amend'''

    text = """\nExample #1: Amending a commit\n
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
    text = "\nFirst, we'll make some changes to the README and save 'em...."
    print(color_it(text, 'white'))
    change_file('README.md', "The time is now: "+ time.strftime('%c',
                                                                time.localtime()))
    print(color_it("\nNow we'll check our git status..."))
    input(color_it('\nPress enter to continue...', 'yellow'))
    call_repo_command(['git', 'status'], wait=True)
    print(color_it("\nNow let's add the file"))
    time.sleep(1)
    call_repo_command(['git', 'add', 'README.md'], wait=True)
    print(color_it("\nWe'll commit that file; go ahead and add a commit message"))
    input(color_it('\nPress enter to commit...', 'yellow'))
    print(color_it("\nRunning command: ", 'red') + color_it('git commit'))
    time.sleep(1)
    subprocess.call(['git', 'commit'], cwd='repo')
    print(color_it("\nCool. Let's look at our git log..."))
    input(color_it('Press enter to continue...', 'yellow'))
    call_repo_command(['git', 'log'])
    print(color_it("There's our first commit"))
    input(color_it('\nPress enter to continue...', 'yellow'))
    print(color_it("\nRad, now let's make another change..."))
    change_file('README.md', "READ ME! The time is now: "+ time.strftime('%c',
                                                                time.localtime()))
    input(color_it('\nPress enter to continue...', 'yellow'))
    print(color_it("\nNow let's add the file again"))
    call_repo_command(['git', 'add', 'README.md'], wait=True)
    print(color_it("\nAnd this time we'll use git commit --amend\n"))
    print(color_it("Change your message if you like."))
    input(color_it('\nPress enter to commit...', 'yellow'))
    print(color_it("\nRunning command: ", 'red') + color_it('git commit --amend'))
    time.sleep(1)
    subprocess.call(['git', 'commit', '--amend'], cwd='repo')
    print(color_it("\nLet's look at our git log..."))
    input(color_it('\nPress enter to continue...', 'yellow'))
    call_repo_command(['git', 'log'])
    print(color_it("\nAnd we see just the one commit"))
    print(color_it("git commit --amend is cool!"))
    time.sleep(0.5)
    print(color_it("\nThat's the end of example 1"))
    key = input(color_it("Press enter to move to the next example or 'q' to quit",
                         'yellow'))
    if key == 'q':
        print(color_it("Cleaning up..."))
        cleanup()
        sys.exit()
    else:
        call_example(2)

def example_two():
    """ rebase edit """

    text = """\nExample #2: Interactive Rebasing: editing\n
              let's edit a commit message with rebase -i.
           """
    print(color_it(text, 'white'))
    input(color_it('\nPress enter to continue...', 'yellow'))
    text = "\nFirst, we'll make some changes to file1.txt and save 'em...."
    print(color_it(text, 'white'))
    change_file('file1.txt', "This change is cool")
    input(color_it('\nPress enter to continue...', 'yellow'))
    print(color_it("Now let's add the file"))
    call_repo_command(['git', 'add', 'file1.txt'], wait=True)
    print(color_it("And we'll commit that file; go ahead and add a commit message"))
    input(color_it('\nPress enter to commit...', 'yellow'))
    print(color_it("\nRunning command: ", 'red') + color_it('git commit'))
    time.sleep(1)
    subprocess.call(['git', 'commit'], cwd='repo')
    print(color_it("\nGreat. Let's look at our git log..."))
    input(color_it('\nPress enter to continue...', 'yellow'))
    call_repo_command(['git', 'log'])
    print(color_it("Cool, now let's make another change..."))
    change_file('file2.txt', "This change is also cool")
    input(color_it('\nPress enter to continue...', 'yellow'))
    print(color_it("\nNow let's add the file"))
    call_repo_command(['git', 'add', 'file2.txt'], wait=True)
    print(color_it("\nAnd we'll commit that file; go ahead and add a commit message"))
    input(color_it('\nPress enter to commit...', 'yellow'))
    print(color_it("\nRunning command: ", 'red') + color_it('git commit'))
    time.sleep(1)
    subprocess.call(['git', 'commit'], cwd='repo')
    print(color_it("\nLet's look at our git log again...", 'yellow'))
    input(color_it('\nPress enter to continue...', 'yellow'))
    call_repo_command(['git', 'log'])
    input(color_it('\nPress enter to continue...', 'yellow'))
    text = """
            We're going to run an interactive rebase using git rebase -i.\n
            Rebasing essentially rewrites history by rewinding to a
            certain point in the git history and then playing commits
            'on top' of that point. With an interactive rebase you can
            alter the commits before they are applied.
           """
    print(color_it(text, 'white'))
    text = """
           We need to specify at what point in history we want to start
           our rebase. We can specify a commit hash or use the HEAD
           pointer. We'll go back two commits by running:\n
           git rebase -i HEAD~2
           """
    print(color_it(text, 'white'))
    input(color_it('Press enter to continue...', 'yellow'))
    text = """
           The interactive rebase session will open your configured
           editor. Each line is a separate commit on which you can
           perform certain operations (there are even nice instructions
           included). Change the word 'pick' to 'edit' and save.
           The rebase will rewind and then let you amend your commit.
           You will be given an opportunity to edit the commit message.
         """
    print(color_it(text, 'white'))
    input(color_it('Press enter to start rebasing...', 'yellow'))
    print(color_it("Running command: ", 'red') + color_it('git rebase -i HEAD~2'))
    time.sleep(1)
    subprocess.call(['git', 'rebase', '-i', 'HEAD~2'], cwd='repo')
    print(color_it("We'll go ahead and amend that commit...", 'white'))
    print(color_it("Running command: ", 'red') + color_it('git commit --amend'))
    time.sleep(1)
    subprocess.call(['git', 'commit', '--amend'], cwd='repo')
    text = """\nNow we'll finish the rebase using:
        git rebase --continue"""
    print(color_it(text, 'white'))
    input(color_it('\nPress enter to continue...', 'yellow'))
    print(color_it("\nRunning command: ", 'red') + color_it('git rebase --continue'))
    call_repo_command(['git', 'rebase', '--continue'])
    print(color_it("Neat", 'white'))
    input(color_it('Press enter to check the git log...', 'yellow'))
    call_repo_command(['git', 'log'])
    text = """
        Wait a second. That was just like git commit --amend except we
        were able to travel further back in time.
        """
    print(color_it(text, 'white'))
    print(color_it("You're like a time traveler or something.", 'white'))
    time.sleep(1)
    print(color_it("\nThat's the end of example 2"))
    key = input(color_it("Press enter to move to the next example or 'q' to quit",
                         'yellow'))
    if key == 'q':
        print(color_it("Cleaning up...."))
        cleanup()
        sys.exit()
    else:
        call_example(3)


def example_three():
    """ git rebase -i changing order of commits """

    text = """\nExample #3: Interactive Rebasing: changing order\n
            In this example, we'll perform an interactive rebase
            to change the order of the commits.\n
           """
    print(color_it(text, 'white'))
    input(color_it('\nPress enter to continue...', 'yellow'))
    print(color_it("\nLet's look at our git log\n", 'white'))
    call_repo_command(['git', 'log'])
    text = """
            Okay. So now we decide it makes more sense for the second change
            to come before the first change. This is a rather contrived
            example but, let's see how it works.
            """
    print(color_it(text, 'white'))
    input(color_it('\nPress enter to continue...', 'yellow'))
    text = """
           We need to specify at what point in history we want to start
           our rebase. We can specify a commit hash or use the HEAD
           pointer. We'll go back two commits by running:\n
           git rebase -i HEAD~2
           """
    print(color_it(text, 'white'))
    input(color_it('\nPress enter to continue...', 'yellow'))
    text = """
           The interactive rebase session will open your configured
           editor. To change the order simply copy/paste the lines in
           the order you'd like to have them and save.
           The changes will be applied from top to bottom.
         """
    print(color_it(text, 'white'))
    input(color_it('\nPress enter to start rebasing...', 'yellow'))
    print(color_it("\nRunning command: ", 'red') + color_it('git rebase -i HEAD~2'))
    time.sleep(1)
    subprocess.call(['git', 'rebase', '-i', 'HEAD~2'], cwd='repo')
    input(color_it('\nPress enter to check the git log...', 'yellow'))
    call_repo_command(['git', 'log'])
    print(color_it("\nDid you change the order? Cool.", 'white'))
    print(color_it("\nYou are like Dr. Who: travelling through time and doing good.", 'white'))
    time.sleep(1)
    print(color_it("\nThat's the end of example 3"))
    key = input(color_it("\nPress enter to move to the next example or 'q' to quit",
                         'yellow'))
    if key == 'q':
        print(color_it("Cleaning up...."))
        cleanup()
        sys.exit()
    else:
        call_example(4)


def example_four():
    """ git rebase -i squash commits """

    text = """\nExample #4: Interactive Rebasing: SQUASHING!\n
            In this example, we'll combine the contents of two commits
            into one commit using git rebase -i.
           """
    print(color_it(text, 'white'))
    input(color_it('\nPress enter to continue...', 'yellow'))
    text = """
            Okay, let's say we decided that the last two commits are
            very closely related and they should really be squashed
            together. We'll run git rebase -i again to 'squash' the
            commits together.
           """
    print(color_it(text, 'white'))
    input(color_it('\nPress enter to continue...', 'yellow'))
    text = """
            We'll go back two commits again, but this time we'll 'pick'
            the first commit and squash the second into it. When the
            interactive rebase is opened in your editor, change the word
            'pick' to 'squash' in front of the commit you wish to
            combine into the previous one.\n
            You will be given an opportunity to alter your commit
            message for the combined commits.
            Remember the changes will be applied from top to bottom.
           """
    print(color_it(text, 'white'))
    input(color_it('\nPress enter to SQUASH...', 'yellow'))
    print(color_it("\nRunning command: ", 'red') + color_it('git rebase -i HEAD~2'))
    time.sleep(1)
    subprocess.call(['git', 'rebase', '-i', 'HEAD~2'], cwd='repo')
    input(color_it("\nLet's check the git log. Press enter...", 'yellow'))
    call_repo_command(['git', 'log'])
    print(color_it("\nThere should just be two commits now. Did you combine the commits? Coolness.", 'white'))
    input(color_it('\nPress enter to continue...', 'yellow'))
    text = """WARNING\n
           Remember to never change history that has already been
           consumed by others. For example you should not change the
           history of commits that have already been merged into a
           master or develop branch because other developers may have
           based their own changes off of this history. This will cause
           very bad headaches.
           Be a responsible time traveller."""
    print(color_it(text, 'red'))
    time.sleep(1)
    print(color_it("\nThat's currently the end of the walkthrough"))
    input(color_it('Press enter to cleanup and exit...', 'yellow'))
    print(color_it("Cleaning up...."))
    cleanup()
    sys.exit()
