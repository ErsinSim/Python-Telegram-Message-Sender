from telethon import TelegramClient
import asyncio
 
async def main():
    #This is just a generic api_id and api_hash!
    #Create your api_id and api_hash on https://my.telegram.org/auth
    api_id = 12345
    api_hash = '0123456789abcdef0123456789abcdef'
 
    again = 'y'
    #Login with your account
    async with TelegramClient('account', api_id, api_hash) as client:
        #Loop to send another message
        while again=='y':
            #Input username and message
            username = input(f'Enter the username to send a message to (without the @): ')
            message = input(f'Enter your message: ')
            try:
                #Send the message to the user
                await client.send_message(str(username), str(message))
                print(f'Your message {message} has been sent to {username}!')
            except:
                traceback.print_exc()
            #Redo loop to send another message
            again = input(f'Do you want to send a message again? Enter [y/n]: ')
        print(f'Done, exiting...')
asyncio.run(main())