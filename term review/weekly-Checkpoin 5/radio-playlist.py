def main():
    playlist = ["Boston", "Dracula", "I Knew It, I Knew You", "hate that i made you love me", "Risk It All"]
    playlist.append("Be By You")
    print(playlist)
    playlist.insert(0, "Bohemian Rhapsody")
    print(playlist)
    playlist.pop(4)
    print(playlist)
    print(playlist.index("Risk It All"))
    print("Number of songs in the playlist:", len(playlist))
    playlist.reverse()#
    print(playlist)
    playlist.sort()
    print(playlist)

    repeat = 10
    while repeat > 0:
        print(playlist)
        son_played=playlist[]

if __name__ == "__main__":
    main()
