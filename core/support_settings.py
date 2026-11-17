"""用于回复和服务界面的客服品牌配置。"""

import os


def support_brand() -> str:
    return os.getenv("ECHOMIND_BRAND", "").strip() or "EchoMind"


def handoff_contact() -> str:
    return os.getenv("ECHOMIND_HANDOFF_CONTACT", "").strip() or "现有客服渠道"
