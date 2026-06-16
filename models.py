# common/models.py

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List


@dataclass
class PostItem:
    """
    所有平台统一输出的数据结构
    """

    # 唯一标识
    post_id: str                  # 平台原始ID
    platform: str                 # weibo/zhihu/bilibili...

    # 内容
    title: Optional[str]
    content: str

    # 作者
    author: str

    # 时间
    publish_time: datetime

    # 原始链接
    url: str

    # 互动数据

    like_num: int = 0

    comment_num: int = 0

    share_num: int = 0

    view_num: int = 0

    # 媒体

    media_type: str = "text"

    media_urls: List[str] = None

    # 标签

    tags: List[str] = None

    # 采集信息

    keyword: str = ""

    crawled_at: datetime = None

    def __post_init__(self):

        if self.media_urls is None:

            self.media_urls = []

        if self.tags is None:

            self.tags = []

        if self.crawled_at is None:

            self.crawled_at = datetime.now()

    @property

    def uid(self):

        """
        跨平台唯一ID

        weibo_12345

        zhihu_67890

        """

        return f"{self.platform}_{self.post_id}"