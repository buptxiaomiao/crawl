# coding: utf-8

from random import randint
from const import CONST


class HeaderTool(object):
    """请求头基类"""

    @classmethod
    def get_user_agent(cls):
        i = randint(0, len(CONST.user_agent_list))
        return CONST.user_agent_list[i]
