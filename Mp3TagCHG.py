import os
import eyed3
import operator

prefix = r".mp3"
path = os.getcwd()

# iterate each file in the folder
for eachfile in os.listdir(path):
    file_len = len(eachfile)

    # if the file extension is exactly same as the prefix
    if operator.eq(prefix, eachfile[file_len - 4 : file_len]) == True:
        # re-construct the file title
        title = u"" + eachfile[0 : file_len - 4]
        print(title)
        print(eachfile)

        # get the sound track number. the assumption is that the file name 
        # follows convention : track_num + space + title
        track_num = eachfile[0 : eachfile.find(" ")]
        print(track_num)

        # contruct the new file name
        new_name = str(track_num) + ".mp3"

        os.rename(os.path.join(path, eachfile), os.path.join(path, new_name))

        # load the audio name for further update for audio tags
        audio_file = eyed3.load(new_name)
        audio_file.initTag()
        audio_file.tag.album = u""
        audio_file.tag.track_num = int(track_num)
        audio_file.tag.artist = u""
        audio_file.tag.album_artist = u""
        audio_file.tag.title = title
        audio_file.save()

        # rename back 
        os.rename(os.path.join(path, new_name), os.path.join(path, eachfile))

