import os
import re

def extract_usernames(file_content):
    pattern = r"\n([a-zA-Z0-9._]+)\n"
    return re.findall(pattern, file_content)

current_directory = os.path.dirname(os.path.realpath(__file__))

follower_file_path = os.path.join(current_directory, 'follower_list.txt')
following_file_path = os.path.join(current_directory, 'following_list.txt')

with open(follower_file_path, 'r') as f:
    follower_list_content = f.read()

with open(following_file_path, 'r') as f:
    following_list_content = f.read()

followers = set(extract_usernames(follower_list_content))
following = set(extract_usernames(following_list_content))

not_following_back = followers - following
not_followed_back = following - followers

output_file_path = os.path.join(current_directory, 'usernames_only.txt')

with open(output_file_path, "w") as file:
    file.write("Usernames who follow you but are not followed back:\n")
    file.write("\n".join(sorted(not_following_back)))
    file.write("\n\nUsernames you follow but are not following you back:\n")
    file.write("\n".join(sorted(not_followed_back)))

print(f"Output saved to: {output_file_path}")
