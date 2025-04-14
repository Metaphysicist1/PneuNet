

print("TensorFlow version:", tf.__version__)
print("GPU Available:", tf.config.list_physical_devices('GPU'))
if tf.config.list_physical_devices('GPU'):
    try:
        # Currently, memory growth needs to be the same across GPUs
        for gpu in tf.config.experimental.list_physical_devices('GPU'):
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(f"Physical GPUs: {len(tf.config.experimental.list_physical_devices('GPU'))}, Logical GPUs: {len(logical_gpus)}")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)
else:
    print("No GPU found. Running on CPU")

# Set random seeds for reproducibility


# Count images per class
train_labels = train_generator.classes
print("Train class distribution:", Counter(train_labels))


