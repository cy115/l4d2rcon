from a2s.exceptions import BrokenMessageError, BufferExhaustedError
from a2s.info import info, ainfo, SourceInfo, GoldSrcInfo
from a2s.players import players, aplayers, Player
from a2s.rules import rules, arules
from hoshino import Service, priv, R
from a2s import info, players

sv = Service(
    name="求生服务器查询",                 # 功能名
    visible=True,                          # 可见性
    enable_on_default=True,                # 默认启用
    bundle="娱乐",                         # 分组归类
)




@sv.on_prefix('查询服务器信息')
async def servece_info(bot, ev):
    text = str(ev.message).strip()
    if not text:
        await bot.send(ev, "查询服务器信息+ip",at_sender=True)
    else:
        ip, port = text.split(':')
        port = int(port)
        massage = str(info((ip, port)))
        await bot.send(ev, massage, at_sender=False)
        
@sv.on_prefix('查询服务器人数')
async def servece_players(bot, ev):
    text = str(ev.message).strip()
    if not text:
        await bot.send(ev, "查询服务器人数+ip",at_sender=True)
    else:
        ip, port = text.split(':')
        port = int(port)
        massage = str(players((ip, port)))
        await bot.send(ev, massage, at_sender=False)
        
