import os
import base64

class FileWrite:

    @staticmethod
    def write(filename:str="",decoded_data:str="",subdir="")->str:
        try:
            if len(decoded_data.split(','))>1:
                decoded_data=decoded_data.split(',')[1]
                
            decoded_data=base64.b64decode(decoded_data)
            if not os.path.exists(f'media/{subdir}'):
                os.mkdir(f'media/{subdir}')

            with open(f'media/{subdir}/{filename}','wb') as f:
                f.write(decoded_data)
                f.close()
            return f'/media/{subdir}/{filename}'
            
        except Exception as e:
            raise Exception(str(e))
