Exercise 9: Block or not

# advance level exercise

def bot8(pbot, p8_bot, p8_human):
    p8=p8_bot*pbot+p8_human*(1-pbot)
    pbot_8 = p8_bot*pbot/p8
    print(pbot_8)


pbot = 0.1
p8_bot = 0.8
p8_human = 0.05

bot8(pbot, p8_bot, p8_human)
