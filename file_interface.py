import os
import json
import base64
from glob import glob


class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self,params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK',data=filelist)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def get(self, params = []):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            fp = open(f"{filename}",'rb')
            isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK',
                        data_namafile=filename,
                        data_file=isifile)
        except Exception as e:
            return dict(status='ERROR',data=str(e))

    def upload(self, params = []):
        try:
            filename = params[0]
            if (filename == ''):
                return None
            if (len(params) == 2):
                filecontent = params[1]
            else: # if empty
                filecontent = ''

            fp = open(f"{filename}",'wb')
            fp.write(base64.b64decode(filecontent))
            fp.close()
            return dict(status = 'OK',
                        data = 'Upload successful.')
        except Exception as e:
            return dict(status = 'ERROR',
                        data = str(e))

    def delete(self, params = []):
        try:
            filename = params[0]
            if (filename == '')
                return None
            os.remove(filename)
            return dict(status = 'OK',
                        data = 'File deleted successfully.')
        except Exception as e:
            return dict(status = 'ERROR',
                        data = str(e))

if __name__=='__main__':
    f = FileInterface()
    print(f.list())
    print(f.get(['pokijan.jpg']))
