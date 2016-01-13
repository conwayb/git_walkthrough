from __future__ import print_function
import subprocess
from utils import call_repo_command, color_it, cleanup
from examples import *

#py2/3 hack
try:
    input = raw_input
except NameError:
    pass

def introduction():
    text = """Welcome to the git walkthrough. \n
            This script allows for a guided tour of certain git
            commands. First up: git rebase -i \n
            git rebase --interactive or (git rebase -i)
            starts an interactive rebasing session. This allows you
            to rewrite history by changing the order of commits,
            amending commit messages, splitting commits, and/or
            combining commits together (squashing). The following
            walkthrough is meant to demonstrate these ideas with
            simple examples."""

    print(color_it(text, 'white'))
    input(color_it('Press enter to start Example 1...', 'yellow'))

def setup_repo():
    print(color_it("First, we'll create a working directory called 'repo'"))
    subprocess.call(['mkdir', 'repo'])
    time.sleep(0.5)
    print(color_it("And setup a repo"))
    call_repo_command(['git', 'init'])
    time.sleep(0.5)
    text = "...and make a couple files"
    print(color_it(text, 'white'))
    call_repo_command(['touch', 'README.md', 'file1.txt', 'file2.txt'],
                 wait=True)

def main():
    cleanup()
    introduction()
    setup_repo()
    call_example(1)


if __name__ == '__main__':
    main()
