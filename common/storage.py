

# common/storage.py

import os

import csv

from typing import List

from common.models import PostItem


class CSVStorage:


    def __init__(

            self,

            filename="data/raw/all_posts.csv"

    ):


        self.filename=filename


        self._ensure_dir()


        self._init_file()


        self.existing_ids=self._load_existing_ids()



    def _ensure_dir(self):


        dirname=os.path.dirname(

            self.filename

        )


        os.makedirs(

            dirname,

            exist_ok=True

        )



    def _init_file(self):


        if os.path.exists(

            self.filename

        ):

            return


        with open(

                self.filename,

                "w",

                newline="",

                encoding="utf-8-sig"

        ) as f:


            writer=csv.writer(f)


            writer.writerow([

                "uid",

                "post_id",

                "platform",

                "title",

                "content",

                "author",

                "publish_time",

                "url",

                "like_num",

                "comment_num",

                "share_num",

                "view_num",

                "media_type",

                "media_urls",

                "tags",

                "keyword",

                "crawled_at"

            ])



    def _load_existing_ids(self):


        ids=set()


        if not os.path.exists(

                self.filename

        ):

            return ids


        with open(

                self.filename,

                "r",

                encoding="utf-8-sig"

        ) as f:


            reader=csv.DictReader(f)


            for row in reader:


                ids.add(

                    row["uid"]

                )


        return ids



    def save(self,item:PostItem):


        if item.uid in self.existing_ids:

            return False


        with open(

                self.filename,

                "a",

                newline="",

                encoding="utf-8-sig"

        ) as f:


            writer=csv.writer(f)


            writer.writerow([

                item.uid,

                item.post_id,

                item.platform,

                item.title or "",

                item.content,

                item.author,

                item.publish_time.isoformat(),

                item.url,

                item.like_num,

                item.comment_num,

                item.share_num,

                item.view_num,

                item.media_type,

                "|".join(

                    item.media_urls

                ),

                "|".join(

                    item.tags

                ),

                item.keyword,

                item.crawled_at.isoformat()

            ])


        self.existing_ids.add(

            item.uid

        )


        return True



    def save_batch(

            self,

            items:List[PostItem]

    ):


        count=0


        with open(

                self.filename,

                "a",

                newline="",

                encoding="utf-8-sig"

        ) as f:


            writer=csv.writer(f)


            for item in items:


                if item.uid in self.existing_ids:

                    continue


                writer.writerow([

                    item.uid,

                    item.post_id,

                    item.platform,

                    item.title or "",

                    item.content,

                    item.author,

                    item.publish_time.isoformat(),

                    item.url,

                    item.like_num,

                    item.comment_num,

                    item.share_num,

                    item.view_num,

                    item.media_type,

                    "|".join(

                        item.media_urls

                    ),

                    "|".join(

                        item.tags

                    ),

                    item.keyword,

                    item.crawled_at.isoformat()

                ])


                self.existing_ids.add(

                    item.uid

                )


                count+=1


        return count



    def count_by_platform(self):


        stats={}


        with open(

                self.filename,

                "r",

                encoding="utf-8-sig"

        ) as f:


            reader=csv.DictReader(f)


            for row in reader:


                p=row["platform"]


                stats[p]=stats.get(

                    p,

                    0

                )+1


        return stats



    def total_count(self):


        return len(

            self.existing_ids

        )
