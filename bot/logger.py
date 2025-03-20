import logging

import seqlog
from django.conf import settings

if settings.SEQ_URL and settings.SEQ_KEY:
    seqlog.log_to_seq(
        server_url=settings.SEQ_URL,
        api_key=settings.SEQ_KEY,
        level=logging.DEBUG,
        batch_size=10,
        auto_flush_timeout=1,
        override_root_logger=True
    )

logger = logging.getLogger('bot')
