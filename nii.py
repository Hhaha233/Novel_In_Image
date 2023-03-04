import sys
import enc
import dec
import time

args = sys.argv
rds = ['-e', '-d','-h']
no_cmdarg=False

def layout_help():
    help_content = '''
    Novel_In_Image v1.0

    Usage: python {} [[-e|-d filename]|-h|-i]

    -e : Encode the file
    -d : Decode the file
    -h : View this help page
    
    Or you can also start now, just input the parameter of mode you need below. (Press enter directly to exit)
    '''.format(sys.argv[0])
    print(help_content)
    return

def raise_err():
    help_content = '''
    Unknown argument: "{}"
    Type "python {} -h" to see the usage.
    '''.format(mode, sys.argv[0])
    print(help_content)
    return

def slp_exit(sec):
    time.sleep(sec)
    exit()

if __name__ == '__main__':
        if len(args) <= 2 :
            if len(args) == 1 or args[1] == rds[2]:
                layout_help()                
                no_cmdarg=True
            else:
                raise_err()
        elif len(args) == 3 and args[1] in rds:
            mode=args[1]
            file=args[2]
        else:
            raise_err()

        if no_cmdarg:
            mode=input("")
            if not mode:
                exit()
            elif not (mode in rds):
                raise_err()
                slp_exit(6)
            elif mode == rds[2] :
                print("The help is above.You can only use this parameter when you start it from command line.")
                slp_exit(10)
            else:
                file=input("Name of the file:")

        if mode == rds[0]:
            enc.main(file)
            print("Done, you can see the encode result in the Output folder")
        else:
            dec.main(file)
            print("Done, you can see the decode result in the Output folder")
        slp_exit(5)
