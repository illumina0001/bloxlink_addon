# bloxlink_addon
An addon for Bloxlink that check's the user's roblox and discord account age for additional security

## Setup
1. Make a Discord bot and add it to your server
2. Download/open [main.py](https://github.com/illumina0001/bloxlink_addon/blob/main/main.py)
3. Adjust the necessary values (token, verification_channel_id, verified_role, min_age) with the setup you prefer. I recommend setting the minimum age to 30 days
4. Run the bot

## Notes

**IMPORTANT:** Make sure that you:
a) Disable the "Change Nickname" permission for @everyone and your role that you're using for bloxlink verification. If left enabled, members will be able to change their username into any roblox username, making the bot check the wrong account

b) Restrict the verification channel to only members who have verified with bloxlink. Otherwise, as Bloxlink has not changed their username to their roblox username, the bot will verify their user with their account's display name.

Other notes:
- Make sure that you have your Bloxlink settings set to the person's Discord name being changed to only their roblox username and not their display name
- I know this entire thing has been rather tailored towards Bloxlink, but Bloxlink has an extremely accessive amount of ads, some of which promote child gambling websites i. e. Bloxflip, so I encourage you to use alternatives  if possible

*made by illumina*
