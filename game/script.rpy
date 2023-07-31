default preferences.text_cps = 40
define config.name = _('Fuwa Fuwa Haato Sensei')

init:
    image black = Solid((0, 0, 0, 255))
    image white = Solid((255, 255, 255, 255))
    image grey = Solid((128, 128, 128, 255))

#MEI
init python:
    """
    import random
        

    def request_gallery_permission():
        if renpy.android:
            try:
                import jnius
                activity = jnius.autoclass("org.renpy.android.PythonActivity").mActivity
                permission = jnius.autoclass("android.Manifest$permission").READ_EXTERNAL_STORAGE
                result = activity.requestPermissions([permission], 1)
                return result[0] == 0  # 0 means permission granted
            except Exception as e:
                print("Error requesting permission:", e)

        return False

    def get_random_picture_from_gallery():
        if renpy.android:
            if request_gallery_permission():
                try:
                    import jnius
                    build.android_permissions = ["android.permission.READ_EXTERNAL_STORAGE"]
                    mActivity = jnius.autoclass("org.renpy.android.PythonSDLActivity").mActivity

                    # Query the user's gallery for images
                    resolver = mActivity.getContentResolver()
                    uri = jnius.autoclass("android.provider.MediaStore$Images$Media").EXTERNAL_CONTENT_URI
                    projection = [jnius.autoclass("android.provider.MediaStore$Images$Media").DATA]
                    cursor = resolver.query(uri, projection, None, None, None)

                    # Check if there are images in the gallery
                    if cursor.getCount() > 0:
                        # Get a random index to select a random image
                        random_index = random.randint(0, cursor.getCount() - 1)

                        # Move the cursor to the selected index
                        cursor.moveToPosition(random_index)

                        # Get the image path from the cursor
                        image_path = cursor.getString(cursor.getColumnIndex(jnius.autoclass("android.provider.MediaStore$Images$Media").DATA))

                        # Return the image path
                        if image_path:
                            return image_path
                except Exception as e:
                    print("Error accessing gallery:", e)

            return None
"""
python:
    """
    import random
    if renpy.android:
        import jnius
        build.android_permissions = ["android.permission.READ_EXTERNAL_STORAGE"]
        mActivity = jnius.autoclass("org.renpy.android.PythonSDLActivity").mActivity
        def get_random_picture_from_gallery():
            # Get the main activity
            mActivity = jnius.autoclass("org.renpy.android.PythonSDLActivity").mActivity

            # Query the user's gallery for images
            resolver = mActivity.getContentResolver()
            uri = jnius.autoclass("android.provider.MediaStore$Images$Media").EXTERNAL_CONTENT_URI
            projection = [jnius.autoclass("android.provider.MediaStore$Images$Media").DATA]
            cursor = resolver.query(uri, projection, None, None, None)

            # Check if there are images in the gallery
            if cursor.getCount() > 0:
                # Get a random index to select a random image
                random_index = random.randint(0, cursor.getCount() - 1)

                # Move the cursor to the selected index
                cursor.moveToPosition(random_index)

                # Get the image path from the cursor
                image_path = cursor.getString(cursor.getColumnIndex(jnius.autoclass("android.provider.MediaStore$Images$Media").DATA))

                # Return the image path
                return image_path

            return None
    else:
        mActivity = None
        """
        

init python:
    import random
    rand_in = random.randint(0, 2)
    

define gui.show_name = True

define config.version = "1.0"

define gui.choice_button_text_idle_color = '#888888'

define m = Character("Michika")
define TA = Character("Teaching Assistant")
define h = Character("Han")
define m_m = Character("????")
define Horie = Character("Horie")
image Sagano = "Sagano.jpg"
image M = "Matsumoto.png"
image Mshy = "Mshy.png"
image m_m = "Matsumoto.png"
image Mblush = "Mblush.png"
image Horie = "Horie.png"
image Cutscene1 = "Cutscene1.png"
image Cutscene2 = "Cutscene2.png"
image Cutscene3 = "Cutscene3.png"
image tbd1 = "tbd1.png"
image tbd2 = "tbd2.png"
image tbd3 = "tbd3.png"
image curse_im1 = "cur1.jpg"
image curse_im2 = "cur2.jpg"

label cursed:
    scene curse_im1 with fade

label start:
    $ myname = renpy.input("What is your name?, If you don't input your name your name will be Han")

    $ myname = myname.strip()

    if myname == "":
        $ myname = "Hann"

#MEI
#    $ image_path = get_random_picture_from_gallery()

#    if image_path:
#        show image image_path
#    else:
#        "No image found in the gallery."


label Prologue:

    
    play music "audio/normal_bg.mp3"

    scene Sagano
    with fade

TA  "Welcome to the KUAB university!  How is the opening ceremony?"

myname"(This place is looking great, I have been waiting to come here for a long time.) "

myname  "So.. .May I ask what day is our first class?"

TA "Tomorrow, you and the rest of 150 students will go to the Sagano hall for the first class."

TA "Check your class schedule on Sentan Navi. For today, I will take you to familiarize yourself with the environment here."

myname"Sounds great, thanks."

myname "(The staff took me to explore the campus, meet the other students and introduce some important rules for living here.)"

myname "(After that, I and the TA disperse from each other. While I was walking back to my dormitory, my eyes were focused on one student, who just walked past.)"
show Mshy
m_m "…"

m_m "You have a problem?"

myname "Oh nothing, it’s nice to meet you. My name is “Han” Sorry for staring at you for a moment"

myname "(Right in front of me is a blonde girl, dressed in a pink high school uniform with a long-sleeves shirt, and a long skirt. She glared at me and gave me a sense that I should back off from her. This is somewhat an awkward moment.)"

m_m " …"
show Mshy
hide Mshy with dissolve
myname  "(Just as I thought, she just walked away from me, and she didn't even introduce herself. This is starting to hurt my feeling for a bit)"

myname "Well at least, I knew that she is living in the same dormitory as mine."

myname "…"

myname " (I hope I will have an enjoyable life here.)"

stop music
label Chapter1:
    scene black with dissolve

    show text "{size=+12}Chapter 1{/size}" with Pause(1.5)


    scene black with dissolve
    scene Sagano
    with fade
    
play music "audio/normal_bg.mp3"
myname"I was sitting in the large hall, surrounded by several hundred tables and a large stadium in front of me. I bet they are using this place for regular lectures."
myname "(A lot of people are coming through the hall entrance, checking their attendance with the TA, and sit down one by one. They are ready for the class and I could see that they are pretty excited for the first class, same goes for me."
myname  "(However, I didn’t expect that….)"
show Mshy with vpunch
m_m "Tch!"
myname "Oh… it’s you again!"
myname "( A blonde girl, who is the same as the one that I met yesterday, gives me another scary look.)"
m_m "How long are you going to linger by my side, go away.. Will you?"
myname "So harsh… I didn’t do anything to you yet! Where did that come from?"
m_m "...."
myname "The two of us were silent for a while, what was a bit abnormal was that the blonde girl broke the silence first."
m "Well… the name is Michika Moriyama"
myname "Moriyama san?"
m  "Yes, now you heard it. Keep that inside your head."
myname "Ouch…"
m "Anyway, let’s see how is the first class today"
myname "(An hour and a half past, everyone expresses disappointment for today's class. Our first class is mechanics, we firstly study some of the essential topics for Physics. It surely was hard."
m  "What’s wrong, you look pale."
myname "This is too much. Am I going to pass the exam? I know that we just went over the essential topics to study, but this is harder than I thought."
m "This is just getting started, What are you doubting yourself?"
myname "Huh?"
m "Sigh ,I’m getting used to this already, many people that I met usually said this after trying something new for the first time."
myname "Ah sorry, I’m just worried that the learning content will be so hard that it is difficult for me to focus."
m "Of course, it will be hard. Now stop whining, keep your chin up and focus for the next class. K?"

m "Alright, now stop staring at me and go take a break! That gives me a lot of creeps."
m "I’m leaving, don't try to follow me."
show Mshy
hide Mshy with dissolve
myname "Wait!"

myname "(She just turned around, being careless and walked away. I wanted to discuss it with her more, but in the end, I had to let her go without much progressive talk.)"

myname "(How could I become closer with someone like her? With these complicated feelings, I stood in my place blankly for a moment, then decided to get on my way)"

stop music
label Chapter2:
     scene black with dissolve

     show text "{size=+12}Chapter 2{/size}" with Pause(1.5)


     scene black with dissolve
     scene Sagano
     with fade
     
play music "audio/normal_bg.mp3"
myname "Time flies quickly, I have been at this college for almost a month."

myname "Although the days in college were busy and a bit boring, overall it was very fulfilling and smooth."

myname "Not to mention that I’m still struggling with that mechanic stuff."
show Mshy with dissolve

m "…"

myname "!!"

m "Hey"

myname "There is another thing recently that made me feel a little concerned."

myname "Does she really think of me as her friend?"

m "Another creepy look, if you don’t want to sit next to me, just let it out. I’m not going to stop you anyways."

myname "Yeah, you are right"

myname "(Well she is right, whenever I sat next to her and studied together. She always scolds me that I couldn’t focus for the class enough, and complains how I couldn’t solve the in-class quiz and homework, regardless of my limited knowledge."

myname "Well you are absolutely right, I’m going to leave."

m "Huh?!"

myname "(I will go sit alone and handle everything by myself, that will be much better)"

m "Wait! Don’t!"

myname "(I just heard a sudden soft voice coming from behind, not really expecting that the origin of the voice is coming from her mouth)"

stop music
hide Mshy with dissolve
myname "(That was.. a cute voice… obviously…)"
scene Cutscene1 with fade
play music "audio/music2.mp3"
myname "(When I turned around, she blushed for a bit, playing with her hair and subconsciously looking sideways. She is trying to avoid direct eye contact)"

myname "(Return to the serious voice] Ahem, how brave of you to say that, learn your manner!)"

myname "But when I just look at you while I’m speaking, you look irritated and uncomfortable. Whenever I’m approaching you, you become aware of my presence."

myname "What did I do to you? I just want to be friends with everyone."

m "…"

myname "(She was just silent for a while… and then return to her calm expression)"
m "I’m not good at socializing."

myname "Huh?"

m "I’m not good about hanging out with other people. Most of the time I just spend time studying, locking myself in a room and isolating myself from the group. Whenever I talked to someone, I gained a lot of pressure because I didn't know how to speak with friends appropriately."

myname "(I see… that is another personality of her, she is quite shy and reserved. Although having a lack of skills to socialize, she worked her way toward being the bright student solely through hard effort.)"

m "Tch! Why did I blurt out my personal story to you? Well.. if you want to leave–"

myname "Let’s just pretend that I didn’t say that. For the next class, let’s study together. It’s your favorite subject! The mechanic! I really need your help for this thing."

m "Uhh…"

myname "I will sit next to you. For now, let me go to the bathroom real quick. Also, you don’t need to worry about that, because I already considered you as a friend from the start."

m "!!!"

myname "She blushes instantly, but I pretend to look in the other direction."

myname "Well.. I will be back?"

m "Idiot…"

myname "?"

myname "She is mumbling about something and I can’t hear what she says, but she looks away and seems to smile for a bit."

myname "(Well at least I was able to ease her burden down, and our relationship returned to normal. I understand that she feels lonely, but maybe if we keep spending our time together, that will clear her anxiety away…. Hopefully…)"

myname  "(I took some time sympathizing with Michika, and then used the remaining time to prepare for the next class.)"

menu:
    "Want to continue with Michika":
        jump ending1
    "No! Michika is not the girl I want. Move to the next girl":
        jump chapter1H


label ending1:
     scene black with dissolve
     stop music

     show text "{size=+12}End of Michika route{/size}" with Pause(5)
     show text "{size=+20}To be continued{/size}" with Pause(5)


     scene black with fade
     scene tbd1
     myname "Thank you for playing"
     scene tbd2
     myname "Good luck finding someone who you trust the most"
     return
label chapter1H:
    scene black with dissolve
    stop music

    show text "{size=+12}Chapter 1(Horie's Route){/size}" with Pause(1.5)


    scene black with dissolve
    scene Sagano
    with fade
    
play music "audio/normal_bg.mp3"
myname "(I was sitting in the large hall, surrounded by several hundred tables and a large stadium in front of me. I bet they are using this place for regular lectures.)"

myname "(A lot of people are coming through the hall entrance, checking their attendance with the TA, and sit down one by one. They are ready for the class and I could see that they are pretty excited for the first class, same goes for me.)"

myname "Suddenly, a tall figure approach me from the front of the table, looking down and giggling.)"

Horie "……………………."
show Horie with dissolve:
    zoom 0.5
myname "........................."

Horie "............................"

myname "Um….. Horie?"

Horie "..........?"

myname "Are you alright? Why are you staring at me? You can sit here, I don’t mind that"

Horie "Yeah… I will sit next to you."

myname "(Oh great, at least she saying something, the class is going to begin soon.)"

Horie "Our first class…. is Physics…?"

myname "Yeah! We should get all things ready."

Horie "............"

myname "(For God’s sake, why is she so unwilling to speak? Should I talk with her more in order to open herself more?)"

myname "Hey! What do you think about physics? I bet that you really like this subject, right?"
Horie ".........."

Horie "Yes……….. It is one of my favorite subjects….."

myname "(Here we go again…. a long awkward silence. Was that even a conversation? At least I got her to say something more, but her expression tells me that she wants to spacing out.)"

Horie "It’s started…"

myname "(Now the class has begun, there are too many complicated math formulas that I just saw in today's lecture. You need to have a strong base in math to understand this…. I barely understand anything about today’s class.)"

myname "(Nevertheless, Horie, who barely speaks to the other, writes down a detailed note and multiple strategies to solve each of the problems. While she has no intention to engage in a conversation, she possesses great intellectual abilities and always stays composed.)"

myname "Wow Horie! I know that you are really good at this!"

Horie "..........."

myname "(Suddenly a bell rang, signaling all the students to take a lunch break. All of the students expressed their disappointment that they couldn’t understand today's class content. I’m not different from them.)"

Horie "............."

myname "It’s lunch time! Wanna go get lunch together?"

Horie "No….thanks…."

myname "W-Wait!"

myname "(Horie walked away after saying only a few words… I still don’t get what she is thinking, but I guess it’s better than nothing. I somehow managed to have a conversation-ish thing with her, so does that mean we became….. closer?)"

hide Horie


stop music
label Chapter2H:
    scene black with dissolve

    show text "{size=+12}Chapter 2(Horie's Route){/size}" with Pause(1.5)


    scene black with dissolve
    scene Sagano
    with fade
    
play music "audio/normal_bg.mp3"
myname "(Time flies quickly; I've been at this college for almost a month.)"
myname "(Although the days at college have been busy and a bit boring, overall, they have been very fulfilling and smooth.)"
myname "(Not to mention, I'm still struggling with that Physics stuff.)"
myname "(I stood idly for a while, thinking about Horie, until she suddenly appeared behind me and I was shocked.)"

myname "Waa!?!"
show Horie with dissolve:
    zoom 0.5
Horie "....................."

myname "..........."

myname "(It’s been a month and her behavior hasn't changed at all, when I invited her to go somewhere or do the activity together. She always refused and avoided me.)"

myname "Hey Horie…"

Horie "...........?"

myname "Do you not like spending time with me?"

Horie "(Shook her head)"

myname "(She shook her head. Should I take that as a sign of negation..?)"
scene Cutscene3 with fade
play music "audio/music1.mp3"
myname "I know I’m not a humorous kind of person, but you know… it would be nice if you could talk to me more…"

Horie "....."

myname "( I guess that’s not happening… Why is she so quiet? It’s not like she’s unable to speak. I’ve heard her speak on multiple occasions. Though even then, her mumbling was barely audible…)"

myname "Hey Horie… I don’t want to be nosy, but shouldn’t you try to communicate more with others?"

Horie ".......I am…."

myname "No…not with gestures. Like a normal chat…"

Horie "...... I am…. Doing it. With you… [myname]..."

myname "( Huh, she just called my name…. She said my name, now that’s something.)"

myname "Sure, we are having a conversation right now… but really, it’s mostly me talking and you replying shortly. I want you to ask me first, Horie."

Horie "I……..first?...."

myname "Yeah, I want to hear your stories. Why are you so good at studying Physics?  I want to know what type of person you are."

myname "(Gah! Now I’m just embarrassed… Why did I make it sound like some cheesy confession?!?)"

Horie "...You want to know me?..."

myname "Uh, yeah! Yes! We are friends right?"

Horie "Friends… [myname]...and..I…are..friends?"

Horie "You want to know more about me…?"

myname "Of course I will, I will listen to anything!"

Horie "........"

myname "After a short silence, she seems to blush for a little."

Horie "...[myname].... You are…."

myname "Huh…?"

Horie ".... Ow…. My head…. Hurts.."

myname "Horie! What’s wrong? Are you alright?"

Horie ".....I’m ok….Last night…. I just study too much…. Didn’t rest…."

myname "(I see, no wonder why she looks so pale and gloomy… studying is her hobby isn’t it? She really has a good responsibility for herself…)"

Horie "So that’s why… You should go take a rest! I will help you back to your dorm!"

Horie "............."

Horie "....Want…to tell,,,,my story…"

myname "Horie! It’s okay! You can do it later… You need to rest! You are practically shaking!"

Horie "Promise….. Wait… for my story… to [myname]......."

myname "Yeah! I will wait for it."
myname "(I escorted Horie to the dorms while her face grew deadly pale. She sometimes looks sick, but seeing her struggle this much in front of me is really heartbreaking…)"

myname "(But still, she called me by my name, and promised in her murmuring voice to tell me her story. That’s a big step forward in progress, compared to the first time we met.)"
menu:
    "Want to continue with Horie":
        jump ending2
    "No! Horie is not the girl I want. Move to the next girl":
        jump chapter1S
stop music

label ending2:
     scene black with dissolve

     show text "{size=+12}End of Horie route{/size}" with Pause(5)
     show text "{size=+20}To be continued{/size}" with Pause(5)


     scene black with dissolve
     scene Sagano
     with fade
     return
label chapter1S:
    scene black with dissolve

    show text "{size=+12}Thank you for playing the beta version of this game{/size}" with Pause(1.5)


    scene black with dissolve
    scene Sagano
    with fade
