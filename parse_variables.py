import hcl

def _translate_key(key):
    return '_' + key.upper()

def main():

    with open('variables.tf', 'r') as fp:
        obj = hcl.load(fp)
    with open('.conf.sh', 'w') as write_obj:
        for key in obj['variable']:
            write_obj.write('{k}="{v}"\n'.format(
                k =_translate_key(key), v = obj['variable'][key]['default']
                ))

if __name__ == '__main__':
    main()


