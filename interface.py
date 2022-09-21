import cmd
import generator

#Object for command line-based interface
class interface(cmd.Cmd):

    #Runs a function to create a strong password and gives the option to choose password length ex. "generate 12". Default is 12
    def do_generate(self, length):
        if length == '':
            length = 12
        print(generator.password(length).generate_strong())

    #Breaks the command-loop and exits the program
    def do_exit(self, line):
        return True

if __name__ == "__main__":
    interface().cmdloop()