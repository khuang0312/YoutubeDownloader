#Features...
#make it more functional...

#allow option to donwload videos as mp3s, oggs, or wavs
#allow downloading videos as different formats as well
#allow downloading as playlists...
#make front end
#set it up so it's download and play... pytube is a weird dependency to have

#allow piping?


#This is a short Python script meant to mass download YouTube videos
#for my family's karaoke machine...

#assumes pytube is set up...



from pytube import YouTube


while True:
    try: 
        user_input = input("Do you want to quit? (Y/N) ")
        
        if user_input in ['Y', 'y', 'yes', 'yeah', 'YES', 'YEAH']:
            break
        
        file_name = input("Input file name: ")
        file = open(file_name)
        target_location = input("Input destination folder name: ")
    
    except KeyboardInterrupt:
        print("Invalid input.")
        continue
    
    except FileNotFoundError:
        print("File \'{}\' doesn\'t exist.".format(file_name))
        continue
    
    else:
        if user_input in ['Y', 'y', 'yes', 'yeah', 'YES', 'YEAH']:
            break
        
        for counter, link in enumerate(file, 1):
            link = link.rstrip()
            
            try:
                YouTube(link).streams.first().download(target_location)
            except:
                print("Unknown error. This link couldn't be processed...")
                continue
            else:
                print(counter, "files processed.")
        
        print("All links in this file processed.")
        file.close()
