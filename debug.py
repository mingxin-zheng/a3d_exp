import torch.distributed as dist


def main():
    # Initialize the process group
    dist.init_process_group(backend='nccl', init_method='env://')
    
    # Get the rank of the current process
    rank = dist.get_rank()
    
    # Print hello world with the rank of the process
    print(f"Hello world from rank {rank}")

    # Synchronize processes
    dist.barrier()
    
    # Clean up
    dist.destroy_process_group()

if __name__ == "__main__":    
    # Launch the main function
    main()
