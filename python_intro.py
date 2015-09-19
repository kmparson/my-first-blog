def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name== 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')
hi("Sonja")


def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']

for name in girls:
    hi(name)
    print('Next girl')
    
