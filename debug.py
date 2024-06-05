import torch.distributed as dist
from datetime import datetime, timedelta

dist.init_process_group(backend="nccl", init_method="env://", timeout=timedelta(seconds=7200))

print("hello from debug.py")

dist.barrier()
