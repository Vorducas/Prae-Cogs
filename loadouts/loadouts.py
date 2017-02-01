import random
import discord
from discord.ext import commands

Tactical = ['Cloak', 'Pulse Blade', 'Grapple', 'Stim', 'A-Wall', 'Phase Shift',
            'Holo Pilot']
            
Primary = ['R-201 Carbine', 'Hemlok BF-R', 'G2A5', 'V-47 Flatline', 'CAR', 'Alternator', 'Volt',
           'R-97 Compact SMG', 'Spitfire', 'L-STAR', 'X-55 Devotion', 'Kraber-AP Sniper', 'D-2 Double Take',
           'Longbow-DMR', 'EVA-8 Shotgun', 'Mastiff', 'EM-4 Cold War', 'R-6P Softball', 'Sidewinder SMR', 'EPG-1']
           
Secondary = ['Archer', 'MGL Mag Launcher', 'LG-97 Thunderbolt', 'Charge Rifle', 'RE-45 Auto',
             'P2016', 'Wingman Elite', 'SA-3 Mozambique', 'B3 Wingman']
             
Ordnance = ['Frag Grenade', 'Arc Grenade', 'Firestar', 'Gravity Star',
            'Electric Smoke Grenade', 'Satchel']
            
Kit1 = ['Power Cell', 'Fast Regen', 'Ordance Expert', 'Phase Embark']

Kit2 = ['Kill Report', 'Wallhang', 'Hover', 'Low Profile']

Titan = ['Ion', 'Tone', 'Legion', 'Ronin', 'Scorch', 'Northstar']

Boost = ['Amped Weapons', 'Ticks', 'Pilot Sentry', 'Map Hack', 'Battery Back-Up',
         'Radar Jammer', 'Titan Sentry', 'Smart Pistol', 'Phase Rewind', 
         'Hard Cover', 'Holo Pilot Nova', 'Dice Roll']

class loadouts:
    """Titanfall 2 loadout generator"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def loadout(self):
        """Generates random loadout"""

        list = '\n'.join(loadout())

        await self.bot.say(list)


def loadout():
    list = []
    list.append('Tactical: ' + str(random.choice(Tactical)))
    list.append('Primary: ' + str(random.choice(Primary)))
    list.append('Secondary: ' + str(random.choice(Secondary)))
    list.append('Ordanance: ' + str(random.choice(Ordnance)))
    list.append('Kit 1: ' + str(random.choice(Kit1)))
    list.append('Kit 2: ' + str(random.choice(Kit2)))
    list.append('Titan: ' + str(random.choice(Titan)))
    list.append('Boost: ' + str(random.choice(Boost)))
    return list


def setup(bot):
    """Adds the cog"""
    bot.add_cog(loadouts(bot))
