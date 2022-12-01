import discord
from discord import File
from discord.utils import get
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font



bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Bot now online")

@bot.listen()
async def on_member_join(member):


  channel = bot.get_channel("Channel Id")



  pos = sum(m.joined_at < member.joined_at for m in member.guild.members if m.joined_at is not None)

  lastnum = int(str(pos)[-1])

  if lastnum == 1:
    te = "st"
  elif lastnum == 2:
    te = "nd"
  elif lastnum == 3:
    te = "rd"
  else: te = "th"

  background = Editor("Image Location")
  profile_image = await load_image_async(str(member.avatar_url))

  profile = Editor(profile_image).resize((150, 150)).circle_image()
  poppins = Font.poppins(size=30, variant="bold")

  poppins_small = Font.poppins(size=20, variant="light")

  background.paste(profile, (325, 90))
  background.ellipse((325, 90), 150, 150, outline="purple", stroke_width=4)

  background.text((400, 260), f"WELCOME TO {member.guild.name}", color="white", font=poppins, align="center")
  background.text((400, 325), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")
  background.text((400, 360), f"You Are The {pos}{te} Member", color="#0BE7F5", font=poppins_small, align="center")

  file = File(fp=background.image_bytes, filename="Image Location")
  welcomemessage = f"Hey {member.mention}! Welcome To **{member.guild.name}**"
  filemessage = file=file


  await channel.send(f"Hey {member.mention}! Welcome To **{member.guild.name}**", file=file)


@bot.listen()
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=Role ID)
    await member.add_roles(role)
    
@bot.listen()
async def on_ready():
  await bot.change_presence(status=discord.Status.online , activity=discord.Activity(type = discord.ActivityType.watching, name = 'for !help'))
  
bot.run("token here")
