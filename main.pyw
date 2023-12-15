

import shelve
import pyperclip
import sys


class Main:


    def __init__(self) -> None:

        self.keeper = shelve.open('local')


    def main(self):

        if len(sys.argv) == 3 and sys.argv[2].lower() == 'save':

            self.keeper[-1] = pyperclip.paste()

        else:

            if len(sys.argv) == 2 and sys.argv[-1].lower() == 'list':

                for key , val in self.keeper.items():

                    print(f'{key} : {val}')

            elif sys.argv[-1] in self.keeper:

                pyperclip.copy(self.keeper[sys.argv[-1]])


    def close(self):

        self.keeper.close()



if __name__ == '__main__':
    
    obj = Main()
    obj.main()
    obj.close()