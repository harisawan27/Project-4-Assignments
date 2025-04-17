import time

def countdown_timer(seconds):
    print(f"\n⏱️ Starting countdown for {seconds} seconds...")

    while seconds > 0:
        minutes, secs = divmod(seconds, 60)
        time_format = f"{minutes:02d}:{secs:02d}"
        print(f"\r⏳ Time left: {time_format}", end="")
        time.sleep(1)
        seconds -= 1

    print("\n\n⏰ Ding! Time's up!")

if __name__ == "__main__":
    try:
        user_input = int(input("⏸️ Enter the number of seconds you want to countdown: "))
        countdown_timer(user_input)
    except ValueError:
        print("⚠️ Please enter a valid number only.")
