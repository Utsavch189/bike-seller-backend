import os

class FileHandel:

    @staticmethod
    def write(filename:str="",decoded_data:str="",subdir="")->str:
        try:
            if not os.path.exists(f'media/{subdir}'):
                os.mkdir(f'media/{subdir}')

            with open(f'media/{subdir}/{filename}','wb') as f:
                f.write(decoded_data)
                f.close()
            return f'/media/{subdir}/{filename}'
            
        except Exception as e:
            raise Exception(str(e))
    
    @staticmethod
    def delete(path="")->str:
        try:
            path=path[1:]
            if os.path.exists(path):
                os.remove(path)
                return ""
            else:
                raise Exception("file not found!")
        except Exception as e:
            raise Exception(str(e))
