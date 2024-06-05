import torch.distributed as dist
import os
import sys

def main():
    
    # Get the rank of the current process
    rank = int(os.getenv("LOCAL_RANK"))
    global_rank = int(os.getenv("RANK"))
    world_size = int(os.getenv("LOCAL_WORLD_SIZE"))
    global_world_size = int(os.getenv("WORLD_SIZE"))
    
    # Print hello world with the rank of the process
    print(f"Hello world from rank {rank}, global rank {global_rank}, world size {world_size}, global world size {global_world_size}!")

    dist_available = dist.is_available()
    dist.init_process_group(backend='nccl', init_method='env://')

    if dist_available:
        print(f"Process group initialized: {dist.is_initialized()}")

    if dist_available and dist.is_initialized():
        print(f"Process group rank: {dist.get_rank()}")
        print(f"Process group size: {dist.get_world_size()}")

        # Synchronize processes
        dist.barrier()
        
        # Clean up
        dist.destroy_process_group()


if __name__ == "__main__":    
    # Launch the main function
    main()
