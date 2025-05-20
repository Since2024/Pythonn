import random

def get_playlist(mood):
    playlists = {
        "happy": [
            "🎶 Happy - Pharrell Williams",
            "🎶 Can't Stop the Feeling - Justin Timberlake",
            "🎶 Good Life - OneRepublic",
        ],
        "sad": [
            "🎧 Someone Like You - Adele",
            "🎧 Fix You - Coldplay",
            "🎧 Let Her Go - Passenger",
        ],
        "angry": [
            "🔥 Numb - Linkin Park",
            "🔥 Break Stuff - Limp Bizkit",
            "🔥 Killing In The Name - Rage Against The Machine",
        ],
        "relaxed": [
            "🌿 Weightless - Marconi Union",
            "🌿 Ocean Eyes - Billie Eilish",
            "🌿 Better Together - Jack Johnson",
        ],
        "romantic": [
            "❤️ Perfect - Ed Sheeran",
            "❤️ All of Me - John Legend",
            "❤️ Just the Way You Are - Bruno Mars",
        ]
    }

    mood = mood.lower()
    if mood in playlists:
        print(f"\nBased on your mood ({mood}), here are some songs you might enjoy:")
        for song in random.sample(playlists[mood], 3):
            print(f"• {song}")
    else:
        print("\nSorry, I don't recognize that mood. Try: happy, sad, angry, relaxed, or romantic.")

def main():
    print("🎧 Welcome to the Mood-Based Music Recommender 🎧")
    mood = input("How are you feeling today? (happy/sad/angry/relaxed/romantic): ")
    get_playlist(mood)

if __name__ == "__main__":
    main()
