import os

import discord
from discord.ext import commands
from firebase import firebase
from firebase_admin import db, credentials
import firebase_admin
import random
import string

letters = string.ascii_letters


firebase = firebase.FirebaseApplication(
    'https://rafflescripts-key.firebaseio.com/', None)

cred = credentials.Certificate('./KEY.json')
firebase_admin = firebase_admin.initialize_app(
    cred, {'databaseURL': 'https://rafflescripts-key.firebaseio.com/'})


class main():
    def __init__(self):
        pass

    async def bind(ctx, firebase, key, id):
        result_keys = firebase.get('Keys', None)
        # print(result_keys)

        result_list = list(result_keys.keys())
        # print(result_list[1])

        for _ in result_list:

            in_result = firebase.get(f'Keys/{_}', None)
            # print(in_result)
            key_in_result = list(in_result.values())[1]

            if key == key_in_result:
                result_users = firebase.get(f'Keys/{_}', None)
                # print(list(result_users.keys()))
                bound_to_check = list(result_users.values())[0]
                # print(bound_to_check)

                if bound_to_check == "None":
                    ref = db.reference()
                    ref_ref = ref.child(f"Keys/{_}")
                    ref_ref.update({
                        "bound_to": f"{id}"
                    })
                    print("Bound key.")
                    await ctx.send("Bound key!")
                    return
                else:
                    # print("lol")
                    pass
            else:
                # print("lel")
                pass

        await ctx.send("Could not bind key.")

    async def get_bound_to(ctx, firebase, key, id):

        result_keys = firebase.get('Keys', None)
        # print(result_keys)

        result_list = list(result_keys.keys())
        # print(result_list[1])

        for _ in result_list:

            in_result = firebase.get(f'Keys/{_}', None)
            # print(in_result)
            key_in_result = list(in_result.values())[1]

            if key == key_in_result:
                result_users = firebase.get(f'Keys/{_}', None)
                # print(list(result_users.keys()))
                bound_to_check = list(result_users.values())[0]
                # print(bound_to_check)

                if bound_to_check == "None":
                    pass
                else:
                    if not str(id) == str(bound_to_check):
                        await ctx.send("You are not the owner of this key.")
                    else:
                        await ctx.send(f"Key bound to: <@{bound_to_check}>")
                        return
            else:
                pass

        await ctx.send("Could not find key.")

    def new_key():
        key = "RS-" + str(''.join(random.choice(letters) for i in range(4))) + "-" + str(''.join(
            random.choice(letters) for i in range(4))) + "-" + str(''.join(random.choice(letters) for i in range(4)))
        return key


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------------')


@bot.event
async def on_member_join(member):
    await member.send("hi")
    key = main.new_key()

    ref = db.reference()
    keys_ref = ref.child('Keys')
    keys_ref.push({
        "key": key,
        "bound_to": "None"
    })

    channel = bot.get_channel(779334152896905247)
    await channel.send(f"<@{member.id}> joined. Created key: [ {key} ]")


@bot.command(name="auth", aliases=["claim", "bind"])
@commands.dm_only()
async def auth(ctx, key):
    id = ctx.author.id
    await main.bind(ctx, firebase, key, id)


f = open("./token.0", "r", encoding="utf-8")
TOKEN = f.read()
bot.run(TOKEN)
