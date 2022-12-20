from pytube import YouTube 


def Download(link):
    Video = YouTube(link)
    UserMP = str(input("Escolha o tipo de download:\n1 - MP3\n2 - MP4\nNúmero: "))
    
    while True:
        if UserMP == "1":
            audio = Video.streams.get_audio_only()
            try:
                audio.download()
            except:
                print("Erro ao baixar MP3")
                
        elif UserChoice == "3":
            print(f"1 - Maior Qualidade:{Video.streams.get_highest_resolution()}")
            print(f"2 - Menor Qualidade:{Video.streams.get_lowest_resolution()}")
            UserChoice = str(input("Número: "))
            
            if UserChoice == "1":
                try:
                    VideoDownload = Video.streams.get_highest_resolution()
                    VideoDownload.download()
                    print("Download Concluido!")
                    break
                except:
                    print("Erro ao baixar MP4")
                    
            elif UserChoice == "2":
                try:
                    VideoDownload = Video.streams.get_lowest_resolution()
                    VideoDownload.download()
                    print("Download Concluido!")
                    break
                except:
                    print("Erro ao baixar MP4")
                    
            else:
                print("Número Inválido")
        
        else:
            print("Número Inválido!")
# Terminar
