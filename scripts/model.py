
import tensorflow as tf
from tensorflow import keras



MODEL_PATH = "scripts/models/best_mobilenetv2.h5"
IMG_HEIGHT = 224
IMG_WIDTH = 224
model = None

def create_model():
    """
    Create model with proper Lambda layer configuration
    """
    # Base model
    base_model = keras.applications.MobileNetV2(
        weights='imagenet',
        input_shape=(IMG_HEIGHT, IMG_WIDTH, 3),
        include_top=False
    )
    base_model.trainable = False
    
    # Define model with Lambda layer that has explicit output shape
    inputs = keras.Input(shape=(IMG_HEIGHT, IMG_WIDTH, 1))
    x = keras.layers.Lambda(
        lambda x: tf.tile(x, [1, 1, 1, 3]),
        output_shape=(IMG_HEIGHT, IMG_WIDTH, 3)  # Explicitly specify output shape
    )(inputs)
    x = base_model(x)
    x = keras.layers.GlobalAveragePooling2D()(x)
    x = keras.layers.Dropout(0.5)(x)
    x = keras.layers.Dense(128, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01))(x)
    x = keras.layers.Dropout(0.5)(x)
    outputs = keras.layers.Dense(1, activation='sigmoid')(x)
    
    # Create model
    model = keras.Model(inputs, outputs)
    
    # Compile model
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=['accuracy', keras.metrics.Precision(), keras.metrics.Recall()]
    )
    
    return model