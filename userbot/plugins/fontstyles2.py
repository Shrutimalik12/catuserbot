import re
import time
import requests
from telethon import events
from userbot import CMD_HELP
from userbot.utils import register, admin_cmd
import asyncio
import random

normaltext = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
illuminatifont = "a⃤ b⃤ c⃤ d⃤ e⃤ f⃤ g⃤ h⃤ i⃤ j⃤ k⃤ l⃤ m⃤ n⃤ o⃤ p⃤ q⃤ r⃤ s⃤ t⃤ u⃤ v⃤ w⃤ x⃤ y⃤ z⃤ a⃤ b⃤ c⃤ d⃤ e⃤ f⃤ g⃤ h⃤ i⃤ j⃤ k⃤ l⃤ m⃤ n⃤ o⃤ p⃤ q⃤ r⃤ s⃤ t⃤ u⃤ v⃤ w⃤ x⃤ y⃤ z⃤ 1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
circlecutfont = "a⃠ b⃠ c⃠ d⃠ e⃠ f⃠ g⃠ h⃠ i⃠ j⃠ k⃠ l⃠ m⃠ n⃠ o⃠ p⃠ q⃠ r⃠ s⃠ t⃠ u⃠ v⃠ w⃠ x⃠ y⃠ z⃠ a⃠ b⃠ c⃠ d⃠ e⃠ f⃠ g⃠ h⃠ i⃠ j⃠ k⃠ l⃠ m⃠ n⃠ o⃠ p⃠ q⃠ r⃠ s⃠ t⃠ u⃠ v⃠ w⃠ x⃠ y⃠ z⃠ 1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
rectangletext = "a⃟ b⃟ c⃟ d⃟ e⃟ f⃟ g⃟ h⃟ i⃟ j⃟ k⃟ l⃟ m⃟ n⃟ o⃟ p⃟ q⃟ r⃟ s⃟ t⃟ u⃟ v⃟ w⃟ x⃟ y⃟ z⃟ a⃟ b⃟ c⃟ d⃟ e⃟ f⃟ g⃟ h⃟ i⃟ j⃟ k⃟ l⃟ m⃟ n⃟ o⃟ p⃟ q⃟ r⃟ s⃟ t⃟ u⃟ v⃟ w⃟ x⃟ y⃟ z⃟ 1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
egyptfont = "ค๒ς๔єŦﻮђเןкl๓ภ๏קợгรtยשฬץאzค๒ς๔єŦﻮђเןкl๓ภ๏קợгรtยשฬץאz1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
ancienttext = "₳Ƀ€ƉɆ₣₲ĦƗɈԞⱠⲘ₦Ø₱Q̶Ɍ$₮Ʉ⩔₩Ӿ¥Ƶ₳Ƀ€ƉɆ₣₲ĦƗɈԞⱠⲘ₦Ø₱Q̶Ɍ$₮Ʉ⩔₩Ӿ¥Ƶ1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
hwsl="𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
bluetext = "🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿 🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯 🇰 🇱 🇲 🇳 🇴 🇵 🇶 🇷 🇸 🇹 🇺 🇻 🇼 🇽 🇾 🇿 1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
nightmare ="𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
ghostfont="𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
hwcapital = "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
tantext="ᎯᏰᏣᎴᏋᎴᎶᏂiᏠᏦlmᏁᏫᎵᏄᖇᎦᎿᏌᏉᏯﾒᎩᏃᎯᏰᏣᎴᏋᎴᎶᏂiᏠᏦlmᏁᏫᎵᏄᖇᎦᎿᏌᏉᏯﾒᎩᏃ1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
liteboxtext="🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
boxtext="🅰️🅱️🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾️🅿️🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰️🅱️🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾️🅿️🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
doubletext="ᎯℬℂⅅℰℱᎶℋℐᎫᏦℒℳℕᎾℙℚℛЅᏆUᏉᏇXᎽℤᎯℬℂⅅℰℱᎶℋℐᎫᏦℒℳℕᎾℙℚℛЅᏆUᏉᏇXᎽℤ1234567890\"'#$%&()*+,-./:;<=>?@[\\]^_`{|}~"


@borg.on(admin_cmd(pattern="illuminatifont ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            illuminatifontcharacter = illuminatifontfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, illuminatifontcharacter)
    await event.edit(string) 



@borg.on(admin_cmd(pattern="circlecutfont ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            circlecutfontcharacter = circlecutfontfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, circlecutfontcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="rectangletext ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            rectangletextcharacter = rectangletextfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, rectangletextcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="egyptfont ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            egyptfontcharacter = egyptfontfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, egyptfontcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="anicenttext ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            anicenttextcharacter = anicenttextfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, anicenttextcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="hwsl ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            hwslcharacter = hwslfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, hwslcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="bluetext ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            bluetextcharacter = bluetextfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, bluetextcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="nightmare ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            nightmarecharacter = nightmarefont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, nightmarecharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="ghostfont ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            ghostfontcharacter = ghostfontfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, ghostfontcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="hwcapital ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            hwcapitalcharacter = hwcapitalfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, hwcapitalcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="tantext ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            tantextcharacter = tantextfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, tantextcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="littleboxtext ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            littleboxtextcharacter = littleboxtextfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, littleboxtextcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="boxtext ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            boxtextcharacter = boxtextfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, boxtextcharacter)
    await event.edit(string) 

@borg.on(admin_cmd(pattern="doubletext ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in normaltext:
            doubletextcharacter = doubletextfont[normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, doubletextcharacter)
    await event.edit(string) 
