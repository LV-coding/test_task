import requests
from fake_useragent import UserAgent
from moviepy.editor import VideoFileClip, vfx
from time import time
from os import remove
from pathlib import Path


def tiktok_scrapper():
    video_url = input('Please, enter url:')
    #video_url = 'https://v16-webapp.tiktok.com/901e87df2b26076efea239232bcdecac/62e837b0/video/tos/useast2a/tos-useast2a-ve-0068c002/5c4ce1ce395c46e79f0377549eff4f1f/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=814&bt=407&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZWKc1we2NEv4yl7Gb&mime_type=video_mp4&qs=0&rc=OmQ1ODtkPDRlOzc6OGc1aEBpM2hvOmk6ZjtvZDMzNzczM0AxNF8zLjQvXmAxMTE2Y180YSMwbjJocjRfXmVgLS1kMTZzcw%3D%3D&l=202208011428350101920572170E36A7CC'
    
    ua = UserAgent()
    headers = {
        'User-Agent':ua.random
    }

    try:
        response = requests.get(video_url, headers=headers)
    except:
        return print('Invalid url, please try again')

    if response.status_code == 200:
        filename = f'{int(time())}'
        filename_mp4, filename_gif = f'{filename}.mp4', f'{filename}.gif'

        print('Downloading started...')
        with open(filename_mp4, 'wb') as writer:
            writer.write(response.content)
        
        # without any resize files is too big
        video_clip = VideoFileClip(filename_mp4).fx(vfx.resize, width=240)

        print('Сonversion started...')
        video_clip.write_gif(filename_gif)
        print('Done!')
        
        path = Path(filename_gif).resolve()
        print(f'Path to file {filename_gif}:\n{path}')

        video_clip.close()
        remove(filename_mp4)
    else:
        print(f'Server answer: {response.status_code} status code...')



if __name__ == '__main__':
    tiktok_scrapper()