## Get your daily VISA consumptions sent as a telegram message
# install
* First of all, you should configure your VISA Home service to send you an email every time you spend a dime.
* Follow [these steps](https://codehandbook.org/how-to-read-email-from-gmail-api-using-python/) to get your credentials downloaded.
* The first time you run this script, Gmail will ask you to give your permissions and it will download a `token.json` file. This file, along with the credentials you downloaded before will be needed to access your Gmail account.
* Both these files should be in the same directory as `GMAIL/readEmail.py`.
* Clone this repository.
* Run `pip install -r /path/to/repo/GMAIL/requirements.txt`.
* Export variable BOT_TOKEN to your .bashrc (If you don't have a Telegram bot token you can simply create it by talking to @BotFather in Telegram).
* In line 45 of `/path/to/repo/GMAIL/readEmail.py` insert your CHAT_ID. (You can get it by talking to @RawDataBot in Telegram. It will answer you a JSON that will have your chat id under `message.chat.id`).
--------------------------------------
# run
`python /path/to/repo/GMAIL/readEmail.py`
--------------------------------------
**To get more ease of use, you can add it to your croned tasks with `crontab -e`, e.g.**
`0 0 * * * /usr/bin/python /path/to/repo/GMAIL/readEmail.py` if you'd like to get notified every midnight.
# Remember that your croned tasks won't have visibility to your environment variables (BOT_TOKEN). One solution is to add your variable to the crontab file before the line that will notify your expenses, e.g.
# `BOT_TOKEN='xxxxxxx'`