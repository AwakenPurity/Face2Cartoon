import tensorflow as tf
result = tf.image.non_max_suppression(boxes, scores, max_output_size=5)
print(result)
