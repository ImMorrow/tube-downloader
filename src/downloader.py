from pytube import YouTube, Playlist
import sys, os, subprocess


def download_mp4(app, path, link):
    try:
        i = 0
        video = YouTube(link)

        # remove forbidden characters
        raw_title = video.title
        clean_title = "".join(j for j in raw_title if j not in '\/:*?<>|"\'')

        print('downloading...')
        app.debug('downloading...')

        # get the video to download
        stream = video.streams.filter().first()
        stream.download(output_path=path, filename=f'{str(i)}.mp4')

        downloaded_file_path = os.path.join(path, f"{str(i)}.mp4")
        converted_file_path = os.path.join(path, f"{clean_title}.mp4")

        # convert to acutal mp4
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

def download_mp3(app, path, link):
    try:
        i = 0
        video = YouTube(link)

        # remove forbidden characters
        raw_title = video.title
        clean_title = "".join(j for j in raw_title if j not in '\/:*?<>|"\'')

        print('downloading...')
        app.debug('downloading...')

        # get the video to download
        stream = video.streams.filter(only_audio=True).first()
        stream.download(output_path=path, filename=f'{str(i)}.mp3')

        downloaded_file_path = os.path.join(path, f"{str(i)}.mp3")
        converted_file_path = os.path.join(path, f"{clean_title}.mp3")

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

def download_mp3_playlist(app, path, link):
    p = Playlist(link)
    i = 0
    for video in p.videos:
        try:
            # remove forbidden characters
            raw_title = video.title
            clean_title = "".join(j for j in raw_title if j not in '\/:*?<>|"\'')

            print('downloading...')
            app.debug('downloading...')
            stream = video.streams.filter(only_audio=True).first()
            stream.download(output_path=path, filename=f'{str(i)}.mp3')

            downloaded_file_path = os.path.join(path, f"{str(i)}.mp3")
            converted_file_path = os.path.join(path, f"{clean_title}.mp3")

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
        

def download_mp4_playlist(app, path, link):
    p = Playlist(link)
    i = 0
    for video in p.videos:
        try:
            # remove forbidden characters
            raw_title = video.title
            clean_title = "".join(j for j in raw_title if j not in '\/:*?<>|"\'')

            print('downloading...')
            app.debug('downloading...')

            # get the video to download
            stream = video.streams.filter().first()
            stream.download(output_path=path, filename=f'{str(i)}.mp4')


            downloaded_file_path = os.path.join(path, f"{str(i)}.mp4")
            converted_file_path = os.path.join(path, f"{clean_title}.mp4")

            # convert to acutal mp4
            print('converting...')
            app.debug('converting...')
            #                           "file_to_convert_path"  "output_path" - make sure to specify file type in path -
            subprocess.run(f'ffmpeg -i "{downloaded_file_path}" "{converted_file_path}"')

            # removing old file
            os.remove(downloaded_file_path)

            print('successfully downloaded file')
            app.debug(f"successfully downloaded file to {converted_file_path}")

        except Exception as e:
            app.debug(str(e))
    
    app.debug("successfully downloaded playlist")