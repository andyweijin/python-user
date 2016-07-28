import getopt,sys

def get_arg():
    if len(sys.argv[1:])>=1:
        try:
            opts, args = getopt.getopt(sys.argv[1:], "hm:c:")
        except getopt.GetoptError as msg:
            raise Exception("Please enter the correct parameters, %s" % msg)
        else:
            module=None
            cla=None
            for op, value in opts:
                if op == "-m":
                    module = value
                elif op == "-c":
                    cla = value
                elif op == "-h":
                    usage()
            if not module or not cla:
                raise Exception("Incomplete parameter")
            else:
                return module,cla
    else:
        raise Exception("Parameters cannot be empty")

def run():
    try:
        module,cla = get_arg()
    except Exception as error:
        print(error)
    else:
        import importlib
        mod = importlib.import_module("knowing.crontabs.%s.%s" % (module,cla))
        main = getattr(mod,cla.capitalize())
        main.run()

def usage():
    print('application.py usage:')
    print(' -m: module name,eg: -m=user')
    print(' -a: class name,eg: -c=cip')
    print(' -h: print help message.')
