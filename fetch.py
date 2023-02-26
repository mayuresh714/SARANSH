from youtube_transcript_api import YouTubeTranscriptApi

class youtubeSubtitles:
    def __init__(self):
        pass

    @staticmethod
    def fetch_id(link):
        return link[-11:]
    
    @staticmethod
    def fetch_srt(vid_id):
        try:
            srt = YouTubeTranscriptApi.get_transcript(vid_id)
            error = False
        except:
            error = True
        
        if error:
            print("error occured while fetching transcript")
            return None
        else:
            return srt
    
    @staticmethod
    def fetch_text(srt):
        try:
            return ' '.join(dic['text'] for dic in srt)
        except:
            print("ERROR while reading text from srt file")
            return None
    

    @staticmethod
    def get_plain_transcript(link):
        vid_id = youtubeSubtitles.fetch_id(link)
        srt= youtubeSubtitles.fetch_srt(vid_id)
        text = youtubeSubtitles.fetch_text(srt) if srt else None
        return text
    

# link = 'https://youtu.be/aCaTUryjWrw'
# youtubeSubtitles.get_plain_transcript(link)
    
