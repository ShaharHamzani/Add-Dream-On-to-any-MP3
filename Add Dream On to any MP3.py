from moviepy.editor import concatenate_audioclips, AudioFileClip

def concatenate_audio_moviepy(audio_clip_paths, output_path):
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)



input_file1 = r"C:--path--\Add Dream On to any MP3\sorces\file.mp3"
input_file2 = r"C:--path--\Add Dream On to any MP3\its-not-over-until-i-win-x-sing-for-the-moment-video-singforthemoment-itsnotoveruntiliwin.mp3"
output_file = r"C:--path--\Add Dream On to any MP3\outputs\output"
str_mp3 = ".mp3"

with open(r"C:\Users\shaha\OneDrive\מסמכים\קבצים חשובים\vs codes\Add Dream On to any MP3\number_out.txt", "r") as source_file:
        source_data = source_file.read()
        source_data = int(source_data) + 1
        source_data = str(source_data)

output_file = output_file + source_data + str_mp3

with open(r"C:\Users\shaha\OneDrive\מסמכים\קבצים חשובים\vs codes\Add Dream On to any MP3\number_out.txt", "w") as destination_file:
        destination_file.write(source_data)


concatenate_audio_moviepy([input_file1, input_file2], output_file)
