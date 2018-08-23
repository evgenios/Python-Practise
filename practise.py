SUFFIXES = {1000 : ['KB', 'MB', 'GB', 'TB','PB','EB', 'ZB','YB'],
            1024: ['KiB', 'MiB','GiB', 'TiB', 'PiB', 'EiB', 'ZiB','YiB']}

def approximate_size(size, aKiloByteIs1024Bytes = True):
    '''Convert a file size'''
    if size < 0:
        raise ValueError('size must be bigger than 0')

    multiple = 1024 if aKiloByteIs1024Bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
        
    raise ValueError('too big bro')

if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(100000000000))