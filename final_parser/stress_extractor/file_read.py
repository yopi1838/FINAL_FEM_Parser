import os

def file_read():
    # List all subdirectories using os.listdir
    basepath = os.path.join(os.getcwd(),'data')
    for entry in os.listdir(basepath):
        if os.path.isdir(os.path.join(os.getcwd(), 'data/{}'.format(entry))):
            print(entry)
        print('Parsing {}. Please wait...'.format(entry))
        return os.path.join(basepath,entry)
