# Deep Learning Fundamentals

## Neural networks
A neural network applies linear transformations and nonlinear activation functions in layers. Training adjusts weights to reduce a loss function. Backpropagation computes gradients; an optimizer uses them to update parameters.

## Core terms
- Feature/input: information supplied to the model.
- Logits: raw model scores before a probability transform.
- Loss: numeric objective minimized during training.
- Epoch: one pass through training data.
- Batch: subset used for one parameter update.
- Learning rate: size of optimizer updates.
- Overfitting: training performance improves while generalization does not.

## Training loop
Prepare data, normalize inputs when appropriate, define model and loss, train on batches, validate after epochs, use early stopping where justified, and evaluate on a test set only after choices are finalized.

## Common architectures
CNNs are often used for spatial/image patterns; RNNs and LSTMs process sequences; transformers use attention and are widely used for language, vision, and multimodal tasks. Architecture choice depends on the task and available data.

## Responsible practice
Track experiments, random seeds, compute cost, dataset permissions, and model limitations. Deep learning is not automatically better than a simpler baseline.
