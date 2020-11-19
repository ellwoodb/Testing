import os

import discord
from discord.ext import commands
from firebase import firebase
from firebase_admin import db, credentials
import firebase_admin

firebase = firebase.FirebaseApplication(
    'https://rafflescripts-key.firebaseio.com/', None)

cred = credentials.Certificate('./rafflescripts-key-firebase-adminsdk.json')
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
    await member.send("hello")


@bot.command()
async def hello(ctx):
    await ctx.send('Hello Friend')


@bot.command(name="auth", aliases=["claim", "bind"])
@commands.dm_only()
async def auth(ctx, key):
    # id = ctx.author.id
    # await ctx.send(key + " your ID: " + str(id))
    # await ctx.send(f"<@{id}>")
    await main.bind(ctx, firebase, key, id)


@bot.command(name="whobound", aliases=["boundto"])
@commands.dm_only()
async def bound_to(ctx, key):
    id = ctx.author.id
    await main.get_bound_to(ctx, firebase, key, id)

bot.run("Nzc0NjY1MzM5NDU1MDEyODY0.X6bFUQ.zQrSbr9l4mE_xrxGKTYKYiy3VmU")

# 752492641970814986
# 752492641970815000
