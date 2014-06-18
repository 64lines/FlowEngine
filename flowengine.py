#!/usr/bin/python
from datetime import datetime
from properties import *


class Utilities:
    def slide_text(self, text, size):
        try: text = text[0:size]
        except: pass
        text += "..." 
        return text

class Activity:
    __dict_status = {
        "I": "Incomplete",
        "C": "Complete"
    }

    def __init__(self):
        self.title = ""
        self.description = ""
        self.date = datetime.now()
        self.status = "I"
        self.time = "00:00"

    def full_status(self):
        status = ""
        try: status = self.__dict_status[self.status]
        except KeyError: pass
        return status

class ActivityManager:
    __list_activities = []

    def new_activity(self):
        print TITLE_NEW_ACTIVITY
        activity = Activity()
        activity.title = raw_input(MESSAGE_1)
        activity.description = raw_input(MESSAGE_2)
        self.__list_activities.append(activity)

    def delete_activity(self):
        act_id = raw_input(MESSAGE_7)
        act_id = int(act_id)

        confirmation = raw_input("Are you sure? (Y/N)")
        if confirmation == "Y":
            self.__list_activities.remove(act_id)
            print " (!) Activity was deleted."

    def update_activity(self):
        act_id = raw_input(MESSAGE_7)
        act_id = int(act_id)

        activity = self.__list_activities[act_id]
        activity.title = raw_input(MESSAGE_1)
        activity.description = raw_input(MESSAGE_2)
        self.__list_activities[act_id] = activity

    def update_activity_status(self):
        act_id = raw_input(MESSAGE_7)
        act_id = int(act_id)

        activity = self.__list_activities[act_id]
        activity.status = raw_input(MESSAGE_4)
        self.__list_activities[act_id] = activity

    def update_activity_time(self):
        act_id = raw_input(MESSAGE_7)
        act_id = int(act_id)

        activity = self.__list_activities[act_id]
        hours = raw_input(MESSAGE_9)
        minutes = raw_input(MESSAGE_10)
        activity.time = MESSAGE_5 % (hours, minutes)
        self.__list_activities[act_id] = activity

    def activity_list(self):
        index = 0
        utilities = Utilities()
        print TITLE_LIST
        for activity in self.__list_activities:
            act_date = activity.date
            act_title = activity.title
            act_descr = activity.description
            act_status = activity.status
            print MESSAGE_3 % (
                index, 
                act_date, 
                act_title, 
                utilities.slide_text(act_descr, 32), 
                "(%s)" % activity.full_status(), 
                "%s" % activity.time
            )
            print SEPARATOR
            index += 1

    def show_activity(self):
        act_id = raw_input(MESSAGE_7)
        act_id = int(act_id)

        activity = self.__list_activities[act_id]
        print """
            == ACTIVITY %d ==
        
        (+) Title: %s
        (+) Description: %s
        (+) Date: %s
        (+) Status: %s
        (+) Time: %s
        """ % (act_id, activity.title, activity.description, activity.date, activity.status, activity.time)

    def save_activities(self):
        file_activities = open(FILE_NAME_SAVE, "wb")
        index = 0
        for activity in self.__list_activities:
            act_date = activity.date
            act_title = activity.title
            act_descr = activity.description
            act_status = activity.status
            act_time = activity.time
            file_activities.write("%d;%s;%s;%s;%s;%s;\n" 
                    % (index, act_date, act_title, act_descr, act_status, act_time))
            
            index += 1

    def load_activities(self):
        file_activities = None
        
        try: file_activities = open(FILE_NAME_SAVE, "rb")
        except: pass
        
        if not file_activities: return

        list_lines = file_activities.readlines()
        for line in list_lines:
            activity_list = line.split(";")
            
            activity = Activity()
            activity.title = activity_list[2]
            activity.description = activity_list[3]
            activity.date = activity_list[1]
            activity.status = activity_list[4]
            activity.time = activity_list[5]

            self.__list_activities.append(activity)

def main():
    activity_manager = ActivityManager()
    activity_manager.load_activities()
    
    option = 1 
   
    while(option != 0):
        option = raw_input(MESSAGE_6)
        option = int(option)

        if option == 1:
            activity_manager.activity_list()
        elif option == 2:
            activity_manager.new_activity()
            activity_manager.save_activities()
        elif option == 3:
            activity_manager.activity_list()
            activity_manager.update_activity_status()
            activity_manager.save_activities()
        elif option == 4:
            activity_manager.activity_list()
            activity_manager.update_activity_time()
            activity_manager.save_activities()
        elif option == 5:
            activity_manager.activity_list()
            activity_manager.delete_activity()
            activity_manager.save_activities()
        elif option == 6:
            activity_manager.activity_list()
            activity_manager.show_activity()
            activity_manager.save_activities()
            

if __name__ == "__main__":
    main()
