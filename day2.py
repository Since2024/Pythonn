# import threading 
# def add_numbers(x, y):
#    print(x + y)
# t = threading.Thread(target=add_numbers, args=(5, 7))
# t.start()
# t.join()


# import time
# from plyer import notification

# if __name__ == "__main__":
#     while True:
#         notification.notify(
#             title="ALERT!!",
#             message="Take a break!",
#             timeout=10
#         )
#         time.sleep(3600)


name = "Hasan"
age = 999
race = "drAGON"

F_formattedSting = f"{name} is a ancient {race} from {age} years ago."
print(F_formattedSting)

