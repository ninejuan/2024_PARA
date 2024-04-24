# from pytube import YouTube
# from nextcord import *
# import asyncio
# import os
# import datetime
# from dotenv import load_dotenv

# TOKEN = "your token"
# # 이건 따리치지 마세요
# with open("./token.txt") as file: TOKEN = file.readline()

# try:
#     os.mkdir("mp4")
# except:
#     pass

# load_dotenv()
# CLIENT = Client()


# @CLIENT.event
# async def on_ready():
#     print(f"Bot is ready as {CLIENT.user}")


# @CLIENT.slash_command(name="youtube")
# async def youtube(inter: Interaction): ...


# @youtube.subcommand(name="mp4", description="Extracts video from YouTube to mp4")
# async def mp4(inter: Interaction, url: str):
#     await inter.response.defer()

#     timestamp = int(datetime.datetime.now().timestamp())

#     async def down(url: str) -> str:
#         file_name = await asyncio.to_thread(YouTube(url).streams.filter(only_audio=False).first().download,
#                                             filename=f"mp4/{timestamp}.mp4")
#         return file_name

#     file_name = await asyncio.create_task(down(url))
#     await inter.followup.send(file=File(f"{file_name}"))
#     os.remove(file_name)


# if __name__ == "__main__":
#     CLIENT.run(TOKEN)

# # 환경변수가 맛이 간 관계로 중단됨