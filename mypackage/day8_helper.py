# module
participants = []

MENU = """
    ============MENU=================
    1. Add new participant
    2. Remove existing participant
    3. Show all participants
    Q. Quit
    =================================
"""


def add_participant():
    new_name = input("Name of participant >>> ")
    participants.append(new_name)
    

def remove_participant():
    remove_name = input("Name of participant to remove >>>  ")
    if remove_name in participants:
        participants.remove(remove_name)
        # print("Participant removed successfully")
        return "Participant removed successfully"

    return "Participant not found in list"


def show_participant():
    print("===============List of participants==============")
    for num, name in enumerate(participants, start=1):
        print(num, name)
    print("=================================================")


# print("name of file ", __name__)

# if this file/module is running directly
if __name__ == "__main__":
    print("this file is running directly")
else:
    print("This file is running due to import in another main file")