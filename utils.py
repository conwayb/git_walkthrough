from __future__ import print_function
import subprocess


#py2/3 hack
try:
    input = raw_input
except NameError:
    pass


def call_repo_command(proc_args=[], wait=False):
    text = color_it("Running command: ", "red")
    command = color_it(" ".join(proc_args))
    print(text + command)
    process = subprocess.Popen(proc_args, cwd='repo', stdin=subprocess.PIPE,
                                             stderr=subprocess.PIPE,
                                             stdout=subprocess.PIPE,)
    (stdout, stderr) = process.communicate()
    print(stdout.decode("utf-8"))
    if wait:
        input(color_it('Press enter to continue...', 'yellow'))


def color_it(text, color="white"):
    colors = {
            "green": 32,
            "white": 37,
            "blue": 34,
            "red": 31,
            "yellow": 33,
            }
    return "\033[0;{0}m{1}\033[0m".format(colors[color], text)


def change_file(filename, text):
    f = open("repo/" + filename, 'w')
    f.write(text)
    f.close()
    text = "Writing to: %s..." % filename
    print(color_it(text))
    call_repo_command(['cat', filename])
