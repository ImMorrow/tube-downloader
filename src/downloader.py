from pytube import YouTube, Playlist
import sys, os, subprocess

def download_playlist(app, path, link, _type, only_audio=False):
    p = Playlist(link)
    i = 0
    for video in p.videos:
        try:
            # remove forbidden characters
            raw_title = video.title
            clean_title = "".join(j for j in raw_title if j not in '\/:*?<>|"\'')

            print('downloading...')
            app.debug('downloading...')
            stream = video.streams.filter(only_audio=only_audio).first()
            stream.download(output_path=path, filename=f'{str(i)}.{_type}')

            downloaded_file_path = os.path.join(path, f"{str(i)}.{_type}")
            converted_file_path = os.path.join(path, f"{clean_title}.{_type}")

            # check if file already exists
            if os.path.isfile(converted_file_path):
                value = app.askyesnocancel("Warning", f"{converted_file_path} already exists, Do you want to replace it?")
                if value == True: os.remove(converted_file_path)
                elif value == False:
                    n = 1
                    converted_file_path = os.path.join(path, f"{clean_title}({n}).{_type}")
                    while os.path.isfile(converted_file_path):
                        n += 1
                        converted_file_path = os.path.join(path, f"{clean_title}({n}).{_type}")
                else:
                    os.remove(downloaded_file_path)
                    app.debug('stopped download process')
                    return


            # convert to acutal mp3 - important if you want tags
            print('converting...')
            app.debug('converting...')
            #                           "file_to_convert_path"  "output_path" - make sure to specify file type in path -
            subprocess.run(f'ffmpeg -i "{downloaded_file_path}" "{converted_file_path}"')
            # removing old file
            os.remove(downloaded_file_path)
            print('successfully downloaded file')
            app.debug(f"downloaded file to {converted_file_path}")
        except Exception as e:
            app.debug(str(e))
        
    app.debug("successfully downloaded playlist")

def download(app, path, link, _type, only_audio=False):
    try:
        i = 0
        video = YouTube(link)

        # remove forbidden characters
        raw_title = video.title
        clean_title = "".join(j for j in raw_title if j not in '\/:*?<>|"\'')

        print('downloading...')
        app.debug('downloading...')

        # get the video to download
        stream = video.streams.filter(only_audio=only_audio).first()
        stream.download(output_path=path, filename=f'{str(i)}.{_type}')

        downloaded_file_path = os.path.join(path, f"{str(i)}.{_type}")
        converted_file_path = os.path.join(path, f"{clean_title}.{_type}")

        # check if file already exists
        if os.path.isfile(converted_file_path):
            value = app.askyesnocancel("Warning", f"{converted_file_path} already exists, Do you want to replace it?")
            if value == True: os.remove(converted_file_path)
            elif value == False:
                n = 1
                converted_file_path = os.path.join(path, f"{clean_title}({n}).{_type}")
                while os.path.isfile(converted_file_path):
                    n += 1
                    converted_file_path = os.path.join(path, f"{clean_title}({n}).{_type}")
            else:
                os.remove(downloaded_file_path)
                app.debug('stopped download process')
                return

        # convert to wanted type - important if you want tags to work
        print('converting...')
        app.debug('converting...')
        #                           "file_to_convert_path"  "output_path" - make sure to specify file type in path -
        subprocess.run(f'ffmpeg -i "{downloaded_file_path}" "{converted_file_path}"')

        # removing old file
        os.remove(downloaded_file_path)
        print('successfully downloaded file')

        app.debug(f"downloaded file to {converted_file_path}")

    except Exception as e:
        app.debug(str(e))