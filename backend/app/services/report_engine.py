#==================================================
# OCR REPORT
#==================================================

def get_ocr_report(ocr):


    if ocr["text"] == "":

        return(

            "Video içerisinde "
            "herhangi bir "
            "metin tespit "
            "edilmemiştir."

        )


    return(

        "Tespit Edilen "

        "Metinler :\n\n"

        f"{ocr['text']}\n\n"


        "OCR analizleri "
        "video içerisinde "
        "yazılı bir anlatım "
        "bulunduğunu "
        "göstermektedir."

    )


#==================================================
# SPEECH REPORT
#==================================================

def get_speech_report(speech):


    if speech == {}:

        return(

            "Video içerisinde "
            "herhangi bir "
            "konuşma tespit "
            "edilmemiştir."

        )


    language = speech["language"]


    if language == "tr":

        language = "Türkçe"


    elif language == "en":

        language = "İngilizce"



    return(

        f"Konuşma Dili : "

        f"{language}\n\n"


        f"Tespit Edilen "

        f"Konuşma : \n\n"

        f"{speech['text']}\n\n"


        "Konuşma analizleri "
        "videonun sözlü "
        "bir anlatıma "
        "sahip olduğunu "
        "göstermektedir."

    )


#==================================================
# OBJECT REPORT
#==================================================

def get_object_report(objects):


    if(

        objects["total_object"]

        == 0

    ):

        return(

            "Video içerisinde "
            "herhangi bir "
            "nesne tespit "
            "edilmemiştir."

        )


    return(

        "Tespit Edilen "

        "Nesneler :\n\n"

        f"{', '.join(objects['result'])}\n\n"


        "Nesne analizleri "
        "videonun görsel "
        "bir anlatıma "
        "sahip olduğunu "
        "göstermektedir."

    )


#==================================================
# VIDEO REPORT
#==================================================

def get_video_information(features):


    return(

        f"Bu video "

        f"{features['duration']} "

        f"saniye uzunluğundadır.\n\n"


        f"Video "

        f"{features['scene_count']} "

        f"adet sahneden "

        f"oluşmaktadır.\n\n"


        "Video analiz için "
        "uygun uzunluğa "
        "sahiptir."

    )


#==================================================
# SCENE REPORT
#==================================================

def get_scene_report(scene):

    if scene["scene_count"] == 1:

        return(

            "Video tek bir "
            "sahneden oluşmaktadır."

        )


    return(

        f"Video toplam "

        f"{scene['scene_count']} "

        f"sahneden "

        f"oluşmaktadır."

    )


#==================================================
# SIMILARITY REPORT
#==================================================

def get_similarity_report(similarity):

    if len(similarity) == 0:

        return(

            "Bu video için "
            "henüz benzer video "
            "tespit edilmemiştir."

        )


    return(

        f"Bu video "

        f"{len(similarity)} adet "

        f"benzer video ile "

        f"eşleştirilmiştir."

    )

#==================================================
# DOMINANT OBJECT REPORT
#==================================================

def get_dominant_object_report(features):

    if(

        features[
        "dominant_object"
        ] == ""

    ):

        return(

            "Videoda baskın "
            "bir nesne "
            "tespit edilmemiştir."

        )


    return(

        f"Videoda en fazla "

        f"{features['dominant_object']} "

        f"nesnesi "

        f"tespit edilmiştir."

    )

#==================================================
# DAHI INSIGHT REPORT
#==================================================

def get_dahi_insight(video_id):


    metadata = get_metadata(
        video_id,
    )


    return(

        f"{metadata['title']} "

        "başlıklı video "

        "başarıyla analiz "

        "edilmiştir.\n\n"


        "OCR, konuşma ve "

        "görsel analizler "

        "birlikte "

        "değerlendirilmiştir.\n\n"


        "DAHI analiz motoru "

        "video içerisinde "

        "yer alan metin, "

        "konuşma ve nesne "

        "içeriklerini "

        "birlikte incelemiştir.\n\n"


        "Video, kullanıcıya "

        "bilgi aktarımı yapan "

        "bir yapıya "

        "sahiptir."

    )


#==================================================
# LANGUAGE
#==================================================

def convert_language(language):


    if language == "tr":

        return "Türkçe"


    if language == "en":

        return "İngilizce"


    if language == "de":

        return "Almanca"


    if language == "fr":

        return "Fransızca"


    return language


#==================================================
# KEYWORD ENGINE
#==================================================

def extract_keywords(text):


    text = text.lower()


    keywords = []


    words = text.split()


    for word in words:

        if len(word) > 3:

            keywords.append(
                word,
            )


    return list(

        set(
            keywords,
        )

    )


#==================================================
# VIDEO CATEGORY ENGINE
#==================================================

def get_video_category(

        ocr,

        speech,

):


    text = (

        ocr["text"]

        +

        speech["text"]

    ).lower()



    if(

        "python" in text

        or

        "software" in text

        or

        "developer" in text

    ):

        return "Programlama"


    if(

        "gym" in text

        or

        "fitness" in text

        or

        "sport" in text

    ):

        return "Fitness"


    if(

        "money" in text

        or

        "finance" in text

    ):

        return "Finans"


    if(

        "motivation" in text

    ):

        return "Motivasyon"


    return "Genel İçerik"