# Reddit extractor example

- Create a Reddit account.
- `user_agent` is a unique identifier that helps Reddit determine the source of network requests.
- `client_id` and `client_secret` are needed to access Reddit’s API as a script application. We can find them by:
- - Login to the reddit account.
  - Go to:  https://www.reddit.com/prefs/apps
  - Create an app.
- Once created, the app will provide the client-id and the secret.
  <img width="1178" alt="reddit_md" src="https://github.com/langure/reddit_poc_1/assets/106360071/fdb09a4b-b5e4-4e7e-bbcb-8882283cdd32">


Clone the repository. Fill the data into a .env file as stated in the env-example file.
Install the dependencies contained in reqs.txt

Run the script. The program will read a reddit post url and obtain all the comments. It will save the results in a sqlite3 databse in the working directory.

