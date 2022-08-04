
# import sys
# sys.path.insert(1, '/home/furqan/.pyenv/versions/3.8.5/lib/python3.8/site-packages')

from flask import Flask, render_template, url_for, request, jsonify, make_response, flash, redirect, send_file, Response
from flask_restful import Api, Resource
import time
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import requests
import re
import os, signal
import io
from multiprocessing import Process
from selenium import webdriver
import glob
import time
import youtube_dl, subprocess
from google_drive_downloader import GoogleDriveDownloader as gdd


app = Flask(__name__)
api = Api(app)

ppid = 0
scr_process = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    if ppid != 0:
        print("ppid: ", ppid)
        # os.kill(ppid, 0)
        scr_process.kill()
        # os.killpg(os.getpgid(ppid), signal.SIGTERM)
        return render_template('index.html')
        
    else:
        pass
    return render_template('index.html')

###########
def background_remove(path):
    task = Process(target=rm(path))
    task.start()

def rm(path):
    os.remove(path)
###########

########### For video ####
sv_path = "$HOME/Video/%(title)s.%(ext)s"
# sv_path = "$HOME/khtube_app/Video/%(title)s.%(ext)s"
def single_video(link, quality_in_words="Vbest", quality=136, output=sv_path, verbose = 2, subprocess=subprocess):
    
    if quality_in_words == "Vbest":
        print("Downloading in progress ......")
        global ppid
        global scr_process
        subprocess = subprocess.Popen(f'exec youtube-dl --no-part -f "bestvideo+bestaudio/best"  -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        ppid = subprocess.pid
        scr_process = subprocess
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")

    elif quality_in_words == "Best":
        print("Downloading in progress ......")
        # global ppid
        # global scr_process
        subprocess = subprocess.Popen(f'exec youtube-dl --no-part -f "best"  -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        ppid = subprocess.pid
        scr_process = subprocess
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")


    elif quality_in_words == "Low":
        print("Downloading in progress ......")
        # global ppid
        # global scr_process
        subprocess = subprocess.Popen(f'exec youtube-dl --no-part -f "worst"  -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        ppid = subprocess.pid
        scr_process = subprocess
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
            
    else:
        print("Downloading in progress ......")
        # global ppid
        # global scr_process
        subprocess = subprocess.Popen(f'exec youtube-dl --no-part -f {quality}+140 -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        ppid = subprocess.pid
        scr_process = subprocess
        print("Please wait...")

        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
#################### end here #########


##### FOr audio ###########

sa_path = "$HOME/Audio/%(title)s.%(ext)s"
# sv_path = "$HOME/khtube_app/Audio/%(title)s.%(ext)s"
def only_music(link, quality=251, best=True, output=sa_path, verbose=2, subprocess = subprocess):
    if best == True:
        print("Downloading in progress ......")
        global ppid
        global scr_process
        subprocess = subprocess.Popen(f'exec youtube-dl --no-part -f "bestaudio/best" -o "{output}" "{link}"', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        ppid = subprocess.pid
        scr_process = subprocess
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
            
    else:
        print("Downloading in progress ......")
        subprocess = subprocess.Popen(f'exec youtube-dl --no-part -f {quality} -o "{output}" {link}', shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        ppid = subprocess.pid
        scr_process = subprocess
        print("Please wait...")
        
        if verbose == 2:
            while True:
                subprocess_return = subprocess.stdout.readline()
                if not subprocess_return:
                    break
                else:
                    print(subprocess_return.strip())
        elif verbose == 1:
            print("Download Complete")
        elif verbose == 3:
            subprocess_return = subprocess.stdout.read()
            print("Download Complete.")
############ End here ###############

####### Crop Video ######

def crop_video(link, fromm, to, quality = "best", subprocess = subprocess):
#     A way to import 
#     FROM = "00:02:06"
#     TO = "00:03:45"
    """
    - Remeber only 3 quality types are available i.e.
    - best -> best of 720p
    - worst -> almost around 240-430p
    """

    TARGET = "video.mp4"

    with youtube_dl.YoutubeDL({'format': quality}) as ydl:
        result = ydl.extract_info(link, download=False)
        video = result['entries'][0] if 'entries' in result else result

    url = video['url']
    print("Please wait......")
    subprocess.run('ffmpeg -i "%s" -ss %s -to %s -c:v copy -c:a copy "%s"' % (url, fromm, to, TARGET), shell=True)
    print("Downloading successfull")

########### End here ###########

@app.route('/vbest', methods=['GET', 'POST'])
def Vbest():
    if request.method == 'POST':
        
        video_link = request.form["url"]

        single_video(link=video_link, quality_in_words="Vbest")
        cwd = os.getcwd()
        files = glob.glob("/home/furqan/Video/*")
        #files = glob.glob(cwd+"/Video/*")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######

        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)


@app.route('/best', methods=['GET', 'POST'])
def Best():
    if request.method == 'POST':
        
        video_link = request.form["url"]

        single_video(link=video_link, quality_in_words="Best")
        cwd = os.getcwd()
        files = glob.glob("/home/furqan/Video/*")
        #files = glob.glob(cwd+"/Video/*")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######


        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)

@app.route('/low', methods=['GET', 'POST'])
def Low():
    if request.method == 'POST':
        
        video_link = request.form["url"]

        single_video(link=video_link, quality_in_words="Low")
        cwd = os.getcwd()
        files = glob.glob("/home/furqan/Video/*")
        #files = glob.glob(cwd+"/Video/*")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######

        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)



@app.route('/audio', methods=['GET', 'POST'])
def audio():
    if request.method == 'POST':

        audio_link = request.form["url"]
        
        only_music(link=audio_link)

        cwd = os.getcwd()
        files = glob.glob("/home/furqan/Audio/*")
        #files = glob.glob(cwd+"/Audio/*")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######

        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)


@app.route('/crop_vid', methods=['GET', 'POST'])
def crop_vid():
    if request.method == 'POST':
        
        video_link = request.form["url"]
        start_time = request.form["initial_time"]
        end_time = request.form["final_time"]

        crop_video(link=video_link, fromm=start_time, to=end_time)

        files = glob.glob("./*.mp4")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        #######

        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)

@app.route('/scrape', methods=['GET', 'POST'])
def call_scrape():
    if request.method == 'POST':
        
        user_kw = request.form["user_kw"]
        
        # code changes here.
        cwd = os.getcwd()
        print(cwd)
        global ppid
        global scr_process
        proc = subprocess.Popen(f'exec python {cwd}/yt_original.py --user_kw="{user_kw}"', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # proc = subprocess.Popen(f'exec python3 {cwd}/yt_original.py --user_kw="{user_kw}"', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ppid = proc.pid
        scr_process = proc
        proc.communicate()[0]
        proc.wait()
        #####
        
        # files = glob.glob("/home/furqan/Desktop/python_work/kodershub/*.xlsx")
        files = glob.glob(cwd+"/*.xlsx")
        print("Length: ", len(files))
        p = files[0]
        updated_path = p.split("/")[-1]

        # ######
        return_data = io.BytesIO()
        with open(p, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)   

        background_remove(p)
        
        return send_file(return_data, as_attachment=True, attachment_filename=updated_path)


# changes here
# @app.route('/download')
# def download_file():
#     # sv_path = "$HOME/Video/%(title)s.%(ext)s"
#     # files = os.listdir()
#     files = glob.glob("/home/furqan/Video/*")

#     p = files[0]
#     return send_file(p, as_attachment=True)

# url = https://www.youtube.com/watch?v=3ps1YL_Bmeo 
# https://www.youtube.com/watch?v=BRAMZwdakTg
# how to get skinny at home by just drinking some herbs # 79
# How to get lean at home without going to gym  # 503 sth
# how to save electricity in multiple garages 50
 
# if __name__ == "__main__":
#     app.run(debug=True)


