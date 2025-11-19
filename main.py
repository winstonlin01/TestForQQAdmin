import re
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.platform import AstrBotMessage
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.provider import LLMResponse

@register("error_filter", "winstonlin01", "屏蔽机器人的错误信息回复。", "1.0.0")
class ErrorFilter(Star):
    @filter.on_llm_response(priority=100000)
    async def Stop(self, event: AstrMessageEvent):
        result = event.get_result()
        message_str = result.get_plain_text()
        if '对不起，服务出现异常，请稍后再试！' in message_str:
            logger.info(message_str)
            event.stop_event() # 停止回复
