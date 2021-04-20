# create an auth session file when user is logged in
# delete the file when user logs out

auth_session_path = "data/auth_session/"

f1 = open(auth_session_path + "loginsession.txt", "w")
f1.write("User Blank is logged in")
