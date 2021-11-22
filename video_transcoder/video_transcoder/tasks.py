from celery import shared_task
import subprocess

@shared_task()
def add(x, y):
    return x + y

@shared_task()
def video_converter(file):
    #print('Request: {0!r}'.format(self.request))
    print(file)
    ffmpeg_command = ["ffmpeg", "-i", "./video_transcoder/{0}.mp4".format(file),"{0}.mov".format(file) ]
    #ffmpeg_command = ["ffplay", "melek.mp4"]
    print(ffmpeg_command)
    pipe = subprocess.run(ffmpeg_command,stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**8)
    
    #pipe = subprocess.run("ls",stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=10**8)
    #print(pipe.stdout)       
    #print(pipe)
    #print(pipe.stderr)  
