import torch

# Check if CUDA (GPU support) is available
if torch.cuda.is_available():
    # Get the number of available GPUs
    num_gpus = torch.cuda.device_count()
    print(f"PyTorch can utilize {num_gpus} GPU(s).")
    
    # Get the name of the current GPU
    current_gpu = torch.cuda.get_device_name(0)  # Assuming you have at least one GPU
    print(f"Current GPU: {current_gpu}")
else:
    print("PyTorch does not have GPU support on this system.")
