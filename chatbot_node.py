#!/usr/bin/env python3

import rospy
import os
from dialogflow_ros_msgs.msg import DialogflowResult

# FIXED path to match your folder
TASKS_FILE = os.path.expanduser("~/hri_course_ws/src/homework3-cziebarth-4/tasks.txt")


class ChatbotNode:
    def __init__(self):
        rospy.init_node("chatbot_node")

        self.sub = rospy.Subscriber(
            "/dialogflow_client/results",
            DialogflowResult,
            self.callback
        )

        rospy.loginfo("chatbot_node is running...")
        rospy.spin()

    def load_tasks(self):
        if not os.path.exists(TASKS_FILE):
            return []

        with open(TASKS_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]

    def save_tasks(self, tasks):
        with open(TASKS_FILE, "w") as f:
            for task in tasks:
                f.write(task + "\n")

    # NEW helper to fix your error
    def normalize_value(self, value):
        if isinstance(value, list):
            if len(value) == 0:
                return ""
            value = value[0]
        return str(value).strip()

    def callback(self, msg):
        rospy.loginfo("Received Dialogflow result")

        intent_name = msg.intent
        raw_parameters = msg.parameters

        rospy.loginfo("Intent: %s", intent_name)
        rospy.loginfo("Parameters: %s", str(raw_parameters))

        # Convert list → dict
        parameters = {}
        for p in raw_parameters:
            parameters[p.param_name] = p.value

        tasks = self.load_tasks()

        if intent_name == "AddTask":
            task = self.normalize_value(parameters.get("task", ""))

            if task:
                tasks.append(task)
                self.save_tasks(tasks)
                rospy.loginfo("Added task: %s", task)
            else:
                rospy.logwarn("No task provided for AddTask")

        elif intent_name == "ShowTasks":
            if len(tasks) == 0:
                rospy.loginfo("No tasks saved")
            else:
                rospy.loginfo("Saved tasks:")
                for i, task in enumerate(tasks, start=1):
                    rospy.loginfo("%d. %s", i, task)

        elif intent_name == "DeleteTask":
            task = self.normalize_value(parameters.get("task", ""))

            if task in tasks:
                tasks.remove(task)
                self.save_tasks(tasks)
                rospy.loginfo("Deleted task: %s", task)
            else:
                rospy.logwarn("Task not found: %s", task)

        else:
            rospy.loginfo("Intent not handled by backend")


if __name__ == "__main__":
    try:
        ChatbotNode()
    except rospy.ROSInterruptException:
        pass
