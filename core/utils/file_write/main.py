import os

class FileWrite:

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
