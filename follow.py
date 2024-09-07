import scratchattach as attach
import time


print("Creating session")
session = attach.login("huh", "huh")
print("Connecting studio")
studio = session.connect_studio("34868267")
off = 14480
index = 0
while True:
    print(f"Fetching projects with offset of {off}")
    projects = studio.projects(limit=20, offset=off)
    for project_info in projects:
        index += 1
        project = session.connect_project(project_info['id'])
        project.get_author().follow()
        print(f"{index}: Followed author {project.get_author().username} from project {project.title}")
        user = session.connect_user({project.get_author().username})
        user.post_comment("my script says i followed you! i am Act3nium for more info on me go to my profile. (sometimes this script is wrong! this bot might not have followed you!)")
    off += 20
    time.sleep(60)
