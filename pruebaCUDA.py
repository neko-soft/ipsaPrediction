import torch
#import tensorflow as tf

print("Torch CUDA Available:", torch.cuda.is_available())
print("Torch CUDA Device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU found")




print(torch.__version__) 
print(torch.version.cuda)
print(torch.backends.cudnn.version()) 
print(torch.cuda.is_available())
print(torch.cuda.device_count())


#print("TensorFlow GPU Devices:", tf.config.list_physical_devices('GPU'))
